from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

class ValidateSparePartWizard(models.Model):
    _name = 'validate.spare.part.wizard'
    _description = 'Wizard to validate and consume spare parts'

    maintenance_request_id = fields.Many2one('maintenance.request', string="Request")
    line_ids = fields.One2many('validate.spare.part.wizard.line', 'wizard_id', string="Spare Parts")

    def action_confirm(self):
        self.ensure_one()
        if not self.line_ids:
            raise UserError(_("Please add at least one product."))


        lines_to_delete = self.env['maintenance.request.line'].search([
            ('maintenance_request_id', '=', self.maintenance_request_id.id)
        ]).unlink()

        for line in self.line_ids:
            product = line.product_id
            product_product = product.product_variant_id
            if not product_product:
                raise UserError(_("Product %s has no variant defined.") % product.name)

            scrap = self.env['stock.scrap'].create({
                'product_id': product_product.id,
                'product_uom_id': product_product.uom_id.id,
                'scrap_qty': line.quantity,
                'origin': self.maintenance_request_id.name or 'Maintenance',
            })
            scrap.action_validate()


            self.env['maintenance.request.line'].create({
                'maintenance_request_id': self.maintenance_request_id.id,
                'product_id': product.id,
                'quantity': line.quantity,
                'qty_available': line.qty_available,
                'done': True,
            })

        if self.maintenance_request_id:
            self.maintenance_request_id.write({'orders_spare_parts': True})
        return {'type': 'ir.actions.act_window_close'}


class ValidateSparePartWizardLine(models.TransientModel):
    _name = 'validate.spare.part.wizard.line'
    _description = 'Wizard Spare Part Line'

    wizard_id = fields.Many2one('validate.spare.part.wizard')


    product_id = fields.Many2one(
        'product.template',
        string="Product",
        domain=[('spare_parts_ok', '=', True)],
    )
    quantity = fields.Float(string="Quantity")
    qty_available = fields.Float(
        string='On Hand',
        compute='_compute_qty_available',
    )
    difference = fields.Float(
        string='After Consumption',
        compute='_compute_difference',
    )
    #

    @api.depends('quantity', 'qty_available')
    def _compute_difference(self):
        for line in self:
            line.difference = line.qty_available - line.quantity

    @api.depends('product_id')
    def _compute_qty_available(self):
        for line in self:
            line.qty_available = line.product_id.qty_available if line.product_id else 0.0


    @api.constrains('quantity', 'qty_available')
    def check_quantity(self):
        for line in self:

            if line.qty_available == 0:
                raise ValueError("you don't have stock.")
            if line.qty_available < 0:
                raise ValueError("stock must be a positive number.")
            if line.quantity <= 0:
                raise ValidationError("Quantity must be a positive number.")

            if line.quantity > line.qty_available:
                raise ValidationError("Quantity must be under vals of stock.")

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    spare_parts_ok = fields.Boolean(String='Spare Part')

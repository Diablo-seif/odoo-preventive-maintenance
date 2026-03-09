from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'


    type_of_maintenance = fields.Selection([
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('weeks', 'Weeks'),
        ('years', 'Years'),
        ('kilometers', 'KiloMeters'),
    ],
        default='days',
        string='Maintenance',
        required=True,

    )

    maintenance_equipment_plan_ids = fields.One2many(
        comodel_name="maintenance.equipment.plan",
        inverse_name="maintenance_equipment_id",
    )


from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MrpWorkCenter(models.Model):
    _inherit = 'mrp.workcenter'

    type_of_maintenance = fields.Selection([
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('weeks', 'Weeks'),
        ('years', 'Years'),
        ('kilometers', 'KiloMeters'),
    ],
    default='days',
        string='Maintenance',
    )


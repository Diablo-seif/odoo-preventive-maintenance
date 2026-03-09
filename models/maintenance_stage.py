from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MaintenanceStage(models.Model):
    _inherit = 'maintenance.stage'


    no_maintenance = fields.Boolean(string="No Maintenance",
                                    default=False)



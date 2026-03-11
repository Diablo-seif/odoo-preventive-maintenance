from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MaintenanceEquipmentPlan (models.Model):
    _name = 'maintenance.equipment.plan'
    _description = "Plan for Maintenance Equipment"
    _order = 'done asc, in_case asc'

    maintenance_equipment_id = fields.Many2one(
        comodel_name="maintenance.equipment",
        string="Maintenance Request",
    )

    tasks = fields.Char(
        string="Tasks",
    )
    in_case = fields.Integer(
        string="In Case",

    )

    in_case_unit = fields.Selection(
        string="Type",
        related = 'maintenance_equipment_id.type_of_maintenance',    )

    done = fields.Boolean(string="Done",  default=False)

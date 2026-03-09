{
    'name': 'Customization Maintenance',
    'version': '1.8',
    'summary': 'Property for Real Estate',
    'depends': [
                'base',
                'mail',
                'hr_maintenance',
                'maintenance',
                'mrp',
                'mrp_maintenance',
                ],
    'data': [
        'security/ir.model.access.csv',

        'wizard/validate_spare_part_wizard_views.xml',

        'data/maintenance_request_data.xml',

        'views/maintenance_equipment_views.xml',
        'views/mrp_workcenter_views.xml',
        'views/maintenance_request_views.xml',
        'views/product_template_view.xml',
        'views/maintenance_stage_views.xml',


    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}
# -*- coding: utf-8 -*-
{
    "name": "Almac Imports Website/Shop Customizations",
    'summary': "Web",
    'description': """
Customization for Almac Imports Ltd.
====================================
- Website customizations
- Shop Customizations
""",
    "author": "Odoo Inc",
    'website': "https://www.odoo.com",
    'category': 'Custom Development',
    'version': '0.1',
    'depends': ['base_import_module', 'website_sale'],
    'data': [
        "data/models.xml",
        'data/fields.xml',
        'views/views.xml',
        'data/actions.xml',
        'views/templates.xml'
    ],
    'license': 'OEEL-1',
}

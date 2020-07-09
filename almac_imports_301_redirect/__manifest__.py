# -*- coding: utf-8 -*-
{
    "name": "Almac Imports Link 301 Redirect",
    'summary': "Link 301 Redirect",
    'description': """
Link 301 Redirect URL
=====================
""",
    "author": "Odoo Inc",
    'website': "https://www.odoo.com",
    'category': 'Custom Development',
    'version': '0.1',
    'depends': ['website_sale'],
    'data': [
        'views/link_redirect.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'OEEL-1',
}

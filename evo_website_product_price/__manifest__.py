
{
    'name': "Website Product Price",
    'summary': """Website Product Price For Odoo 14""",
    'description': """Website Product Price Odoo 14.0""",
    'author': "",
    'website': "",    
    'category': 'website_sale',
    'version': '1.0',
    'depends': ['base_setup', 
                'web',
                'website_sale'],

    'data': [
               
               'security/ir.model.access.csv', 
                'views/product_template.xml',
                'views/product_view.xml',
    ],
    'images': [],
    'auto_install': False,
    'installable': True,
    'application':True,
}

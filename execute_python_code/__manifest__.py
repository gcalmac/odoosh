{
    "name": "Execute Python Code",
    "description": """
Installing this module, user will able to execute python code from Odoo
""",
    "category": 'Extra Tools',
    "website": '',
    "maintainer": '',
    "version": "1.0",
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        
        'view/python_code_view.xml',
    ],
    "installable": True,
}

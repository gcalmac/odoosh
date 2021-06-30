
{
    'name': "Website changes and modifications",
    'summary': """Website changes and modifications""",
    'author': "Evozard",
    'website': "http://evozard.com/",    
    'version': '1.0',            
    'depends': ['website','website_sale'],
    'data': [
        'views/assets.xml',
        'views/video_change.xml',
        'views/header_template.xml',
        'views/footer_template.xml',
        'views/inactive_template.xml',
        'views/product_description.xml',
    ],
    'auto_install': False,
    'installable': True,
    'application':True,
}

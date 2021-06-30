# -*- coding: utf-8 -*-

from odoo import  fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.attribute'
    
    website_hidden = fields.Boolean(string='Hidden in Website')
    

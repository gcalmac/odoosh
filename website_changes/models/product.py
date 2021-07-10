# -*- coding: utf-8 -*-

from odoo import models

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    def get_suggested_product_list(self):
        accessory_products = self.env['product.product']
        accessory_products |= self.accessory_product_ids.filtered(lambda product:product.website_published)
        return accessory_products
    
class ProductProduct(models.Model):
    _inherit = "product.product"
    
    def _get_product_description_list(self):
        variant_name = ''
        for product in self.sudo():
            variant_text = product.product_template_attribute_value_ids._get_combination_name()
            if product.default_code:
                variant_name = "Item: %s - %s" % (product.default_code, variant_text)
            else:
                variant_name = "Item: %s" % (variant_text)
        return variant_name
    
    def _get_product_pricelist_item(self,pricelist=False):
        current_website = False

        if self.env.context.get('website_id'):
            current_website = self.env['website'].get_current_website()
            if not pricelist:
                pricelist = current_website.get_current_pricelist()
                
        product_pricelist_item_ids = self.env['product.pricelist.item'].sudo().search([('product_id','=',self.id),
                                                                                ('pricelist_id','=',pricelist.id)],order="min_quantity ASC")
        description_list = []
        base_price = 0.0
        skip = True
        if product_pricelist_item_ids:
            if product_pricelist_item_ids[0].compute_price == 'fixed':
                base_price = product_pricelist_item_ids[0].fixed_price
            elif product_pricelist_item_ids[0].compute_price == 'percentage':
                base_price = product_pricelist_item_ids[0].percent_price
        for product_pricelist_item_id in product_pricelist_item_ids:
            if skip:
                text = "- Buy %s+ for %s" % (int(product_pricelist_item_id.min_quantity), product_pricelist_item_id.price)
                skip = False
            else:
                if product_pricelist_item_id.compute_price == 'fixed':
                    diff = base_price - product_pricelist_item_id.fixed_price
                    percentage = (diff * 100) / base_price
                    discount = int(percentage)
                    text = "- Buy %s+ for %s and save %s%%" % (int(product_pricelist_item_id.min_quantity), product_pricelist_item_id.price,discount)
                if product_pricelist_item_id.compute_price == 'percentage':
                    diff = base_price - product_pricelist_item_id.percent_price
                    percentage = (diff * 100) / base_price
                    discount = int(percentage)
                    text = "- Buy %s+ for %s and save %s%%" % (int(product_pricelist_item_id.min_quantity), product_pricelist_item_id.price,discount)
            description_list.append(text)
        return description_list
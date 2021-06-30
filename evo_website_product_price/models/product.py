from odoo import  fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    min_price = fields.Float(string='Minimum Product Price')
    max_price = fields.Float(string='Maximum Product Price')
    
    
    def _get_combination_info(self, combination=False, product_id=False, add_qty=1, pricelist=False, parent_combination=False, only_template=False):
        """Override for website, where we want to:
            - take the website pricelist if no pricelist is set
            - apply the b2b/b2c setting to the result

        This will work when adding website_id to the context, which is done
        automatically when called from routes with website=True.
        """
        self.ensure_one()

        current_website = False

        if self.env.context.get('website_id'):
            current_website = self.env['website'].get_current_website()
            if not pricelist:
                pricelist = current_website.get_current_pricelist()

        combination_info = super(ProductTemplate, self)._get_combination_info(
            combination=combination, product_id=product_id, add_qty=add_qty, pricelist=pricelist,
            parent_combination=parent_combination, only_template=only_template)

        if self.env.context.get('website_id'):
            partner = self.env.user.partner_id
            company_id = current_website.company_id
            product = self.env['product.product'].browse(combination_info['product_id']) or self

            tax_display = self.user_has_groups('account.group_show_line_subtotals_tax_excluded') and 'total_excluded' or 'total_included'
            fpos = self.env['account.fiscal.position'].get_fiscal_position(partner.id).sudo()
            taxes = fpos.map_tax(product.sudo().taxes_id.filtered(lambda x: x.company_id == company_id), product, partner)

            # The list_price is always the price of one.
            quantity_1 = 1
            price = taxes.compute_all(combination_info['price'], pricelist.currency_id, quantity_1, product, partner)[tax_display]
            if pricelist.discount_policy == 'without_discount':
                list_price = taxes.compute_all(combination_info['list_price'], pricelist.currency_id, quantity_1, product, partner)[tax_display]
            else:
                list_price = price
            has_discounted_price = pricelist.currency_id.compare_amounts(list_price, price) == 1
            pricelist_item = self.env['product.pricelist.item'].sudo().search([('product_id.product_tmpl_id','=',self.id),('pricelist_id','=',pricelist.id)])
            
            if len(pricelist_item) != 1 or len(pricelist_item) != 0:
                start_price = self.env['product.pricelist.item'].sudo().search([('product_id.product_tmpl_id','=',self.id),('pricelist_id','=',pricelist.id)],order='fixed_price asc',limit=1)
                end_price = self.env['product.pricelist.item'].sudo().search([('product_id.product_tmpl_id','=',self.id),('pricelist_id','=',pricelist.id)],order='fixed_price desc',limit=1)
            
            combination_info.update(
                price=price,
                list_price=list_price,
                has_discounted_price=has_discounted_price,
                min_price=start_price.fixed_price,
                max_price=end_price.fixed_price,
            )
        return combination_info
    
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class LinkRedirect(models.Model):
    """Generate 301 link redirect"""
    _name = "link.redirect"

    name = fields.Char(string='URL Title', default="URL Title")
    old_link = fields.Char(string='Old Link', required=True)
    current_link = fields.Char(string='Redirect Link')

    res_model = fields.Char(string='Resource Model')
    res_id = fields.Integer(string='Resource Id')
    # compute based on res_model and res_id
    reocrd_id = fields.Char(string='Record Id', compute='_compute_redirect_record', readonly=True)
    active = fields.Boolean(string='Active', default=True)

    @api.depends('res_model', 'res_id')
    def _compute_redirect_record(self):
        self.ensure_one()
        #/web#id=res_id&view_type=form&model=res_model
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        if self.res_model and self.res_id:
            model = self.env['ir.model'].search([('model', '=', self.res_model)], limit=1)
            if not model:
                raise UserError(_('Resource Model Does not Exist, Enter correct Model name eg: res.partner'))
            rec_id = self.env[model.model].search([('id', '=', self.res_id)]) or False
            if not rec_id:
                raise UserError(_('Resource Id Does not Exist'))
            self.reocrd_id = base_url+"/web?#id=%d&view_type=form&model=%s" % (self.res_id, self.res_model)
        else:
            self.reocrd_id = False

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import werkzeug

from odoo import http
from odoo.http import request
from odoo.addons.website.controllers.main import Website

# REG_EXP = "([a-zA-Z0-9\.]+?)(_[a-z]+)?(\(\d+\))?(\.html)?$"

ALMAC_REIDRECT_URL = [
    '/<old_link>',
    '/<path:old_link>.html',
    '/packaging-accessories/<path:old_link>',
    '/packaging/<path:old_link>',
    '/boxes/<path:old_link>',
    '/baskets/<path:old_link>',
    '/seasonal-promotions/<path:old_link>',
    '/about-us/<path:old_link>',
    '/by-industry/<path:old_link>',
    '/shred-and-sizzle/<path:old_link>',
    '/blog/<path:old_link>',
    ]

class LinkRedirect(Website):

    @http.route(ALMAC_REIDRECT_URL, type='http', auth="public", website=True, multilang=False)
    def redirect(self, **kw):
        old_link = request.httprequest.path
        link_redirect = request.env['link.redirect'].sudo().search(['|', ('old_link', '=', "/"+old_link), ('old_link', '=', old_link), ('active', '=', True)], limit=1)
        if link_redirect or (link_redirect.current_link and link_redirect.reocrd_id):
            return werkzeug.utils.redirect(link_redirect.current_link or link_redirect.reocrd_id, 301)
        page = '/'
        main_menu = request.env.ref('website.main_menu', raise_if_not_found=False)
        if main_menu:
            first_menu = main_menu.child_id and main_menu.child_id[0]
            if first_menu:
                if first_menu.url and (not (first_menu.url.startswith(('/page/', '/?', '/#')) or (first_menu.url == '/'))):
                    return request.redirect(first_menu.url)
                if first_menu.url and first_menu.url.startswith('/page/'):
                    return request.env['ir.http'].reroute(first_menu.url)
        return request.redirect(page)

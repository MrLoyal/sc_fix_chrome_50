# -*- coding: utf-8 -*-
from openerp import http

# class ScFixChrome50(http.Controller):
#     @http.route('/sc_fix_chrome_50/sc_fix_chrome_50/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sc_fix_chrome_50/sc_fix_chrome_50/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sc_fix_chrome_50.listing', {
#             'root': '/sc_fix_chrome_50/sc_fix_chrome_50',
#             'objects': http.request.env['sc_fix_chrome_50.sc_fix_chrome_50'].search([]),
#         })

#     @http.route('/sc_fix_chrome_50/sc_fix_chrome_50/objects/<model("sc_fix_chrome_50.sc_fix_chrome_50"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sc_fix_chrome_50.object', {
#             'object': obj
#         })
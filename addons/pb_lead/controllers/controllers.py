# -*- coding: utf-8 -*-
# from odoo import http


# class PbLead(http.Controller):
#     @http.route('/pb_lead/pb_lead', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pb_lead/pb_lead/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pb_lead.listing', {
#             'root': '/pb_lead/pb_lead',
#             'objects': http.request.env['pb_lead.pb_lead'].search([]),
#         })

#     @http.route('/pb_lead/pb_lead/objects/<model("pb_lead.pb_lead"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pb_lead.object', {
#             'object': obj
#         })

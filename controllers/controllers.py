# -*- coding: utf-8 -*-
from odoo import http

# class RealStateBroker(http.Controller):
#     @http.route('/real_state_broker/real_state_broker/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/real_state_broker/real_state_broker/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('real_state_broker.listing', {
#             'root': '/real_state_broker/real_state_broker',
#             'objects': http.request.env['real_state_broker.real_state_broker'].search([]),
#         })

#     @http.route('/real_state_broker/real_state_broker/objects/<model("real_state_broker.real_state_broker"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('real_state_broker.object', {
#             'object': obj
#         })
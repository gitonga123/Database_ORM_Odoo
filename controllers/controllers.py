# -*- coding: utf-8 -*-
from openerp import http

# class Database(http.Controller):
#     @http.route('/database/database/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/database/database/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('database.listing', {
#             'root': '/database/database',
#             'objects': http.request.env['database.database'].search([]),
#         })

#     @http.route('/database/database/objects/<model("database.database"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('database.object', {
#             'object': obj
#         })
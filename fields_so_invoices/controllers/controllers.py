# -*- coding: utf-8 -*-
from odoo import http

# class FieldsSoInvoices(http.Controller):
#     @http.route('/fields_so_invoices/fields_so_invoices/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fields_so_invoices/fields_so_invoices/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fields_so_invoices.listing', {
#             'root': '/fields_so_invoices/fields_so_invoices',
#             'objects': http.request.env['fields_so_invoices.fields_so_invoices'].search([]),
#         })

#     @http.route('/fields_so_invoices/fields_so_invoices/objects/<model("fields_so_invoices.fields_so_invoices"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fields_so_invoices.object', {
#             'object': obj
#         })
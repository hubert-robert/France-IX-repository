# -*- coding: utf-8 -*-

from odoo import models, fields, api

class po_ref_on_subscription(models.Model):

    _inherit = 'sale.subscription'

    po_reference = fields.Char(name='po_reference_on_subscription', string='PO')

    # @api.onchange('po_reference')
    # def populate_field_ref_on_invoice(self):

    #     Invoices = self.env['account.invoice'].search([])
    #     can_read = Invoices.check_access_rights('read', raise_exception=False)
    #     for sub in self:
    #         Invoices_to_modify = can_read and Invoices.search([('invoice_line_ids.subscription_id','=',sub.id)])
    #         import ipdb; ipdb.set_trace()
    #         for invoice in Invoices_to_modify:
    #             invoice.po_reference = sub.po_reference



class po_reference_on_invoice(models.Model):

    _inherit = 'account.invoice'

    # def _set_po_ref(self):
    #     for invoice in self:
    #         Invoices = self.env['account.invoice']

    po_reference_on_invoice = fields.Char(name='po_reference_on_invoice', string='PO')

class SaleSubscriptionsWithPO(models.Model):
    _inherit='sale.subscription'

    def _recurring_create_invoice(self, automatic=False):
        self.ensure_one()

        invoices = super(SaleSubscriptionsWithPO, self)._recurring_create_invoice()

        for invoice in invoices:
            sub_ids = invoice.mapped('invoice_line_ids').mapped('subscription_id')
            invoice.po_reference_on_invoice = sub_ids[:1].po_reference
            
        return invoices
        

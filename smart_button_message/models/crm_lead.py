# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Lead(models.Model):

    _inherit = 'crm.lead'

    message_count = fields.Integer("# Messages", compute='_compute_message_count')

    @api.depends('message_ids')
    def _compute_message_count(self):
        for lead in self:
            lead.message_count = len(lead.message_ids)

    @api.multi
    def edit_messages(self):
        action = self.env.ref('mail.action_view_mail_message').read()[0]
        action['domain'] = [
            ('res_id', '=', self.id),
            ('model', '=', 'crm.lead'),
        ]
        return action
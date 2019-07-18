# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Partner(models.Model):

    _inherit = 'res.partner'

    message_count = fields.Integer("# Messages", compute='_compute_message_count')

    @api.depends('message_ids')
    def _compute_message_count(self):
        for partner in self:
            partner.message_count = len(partner.message_ids)

    @api.multi
    def edit_messages(self):
        # partner_ids = self.ids
        # partner_ids.append(self.env.user.partner_id.id)
        action = self.env.ref('mail.action_view_mail_message').read()[0]
        action['domain'] = [
            ('res_id', '=', self.id),
            ('model', '=', 'res.partner'),
        ]
        return action
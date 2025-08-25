# -*- coding: utf-8 -*-
# Part of AlmightyCS. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"
    
    @api.model
    def acs_action_cash_payment(self, payment_journal=False):
        PaymentReg = self.env['account.payment.register']
        if not payment_journal:
            payment_journal = self.env['account.journal'].search([('type', '=', 'cash')], limit=1)
        for inv in self:
            if inv.state=='draft':
                inv.action_post()
            payment = PaymentReg.with_context(active_model='account.move',active_ids=[inv.id]).create({
                'journal_id': payment_journal.id,
            })
            payment._create_payments()
            
    
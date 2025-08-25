# -*- coding: utf-8 -*-

from odoo import api,fields,models,_


class AccountMove(models.Model):
    _inherit = 'account.move'

    patient_id = fields.Many2one('hms.patient', string='Patient', index=True)
    physician_id = fields.Many2one('hms.physician', string='Physician') 
    hospital_invoice_type = fields.Selection([
        ('patient','Patient')], string="Hospital Invoice Type")
    # related='patient_id.category', 
    category = fields.Selection([('General', 'General'), ('Government', 'Government'), ('Insurance', 'Insurance'), ('Healthabhi', 'Healthabhi')], string='Category',
        help="Category of the patient. It is used to determine the price of the services provided to the patient.", readonly=True, store=True)
    # related='patient_id.sub_category', 
    sub_category = fields.Selection([('ICICI', 'ICICI')], string='Sub Category',
        help="Sub Category of the patient. It is used to determine the price of the services provided to the patient.", readonly=True, store=True)

    @api.onchange('patient_id')
    def onchange_patient(self):
        if self.patient_id and not self.partner_id:
            self.partner_id = self.patient_id.partner_id.id

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

# -*- coding: utf-8 -*-
# Part of AlmightyCS. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models,_


class ResCompany(models.Model):
    _inherit = "res.company"

    acs_hospitalization_usage_location_id = fields.Many2one('stock.location', 
        string='Hospitalization Usage Location for Consumed Products')
    acs_hospitalization_stock_location_id = fields.Many2one('stock.location', 
        string='Hospitalization Stock Location for Consumed Products')
    allow_bed_reservation = fields.Boolean('Allow Bed Reservation')
    acs_death_register_qrcode = fields.Boolean(string="Print QrCode on Death Register Report", default=True)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    acs_hospitalization_usage_location_id = fields.Many2one('stock.location', 
        related='company_id.acs_hospitalization_usage_location_id',
        domain=[('usage','=','customer')],
        string='Hospitalization Usage Location for Consumed Products', 
        ondelete='cascade', help='Usage Location for Consumed Products', readonly=False)
    acs_hospitalization_stock_location_id = fields.Many2one('stock.location', 
        related='company_id.acs_hospitalization_stock_location_id',
        domain=[('usage','=','internal')],
        string='Hospitalization Stock Location for Consumed Products', 
        ondelete='cascade', help='Stock Location for Consumed Products', readonly=False)
    allow_bed_reservation = fields.Boolean('Allow Bed Reservation',
        related='company_id.allow_bed_reservation',
        help='Allow bed Reservation', readonly=False)
    acs_death_register_qrcode = fields.Boolean(related='company_id.acs_death_register_qrcode', string="Print QrCode on Death Register Report", readonly=False)
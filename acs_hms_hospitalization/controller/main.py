# -*- coding: utf-8 -*-
# Part of AlmightyCS. See LICENSE file for full copyright and licensing details.

from odoo import http, fields, _
from odoo.http import request


class ACSHms(http.Controller):

    @http.route(['/validate/patientdeathregister/<deathregister_unique_code>'], type='http', auth="public", website=True, sitemap=False)
    def deathregister_details(self, deathregister_unique_code, **post):
        if deathregister_unique_code:
            deathregister = request.env['patient.death.register'].sudo().search([('unique_code','=',deathregister_unique_code)], limit=1)
            if deathregister:
                return request.render("acs_hms_hospitalization.acs_deathregister_details", {'deathregister': deathregister})
        return request.render("acs_hms_hospitalization.acs_no_deathregister_details")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
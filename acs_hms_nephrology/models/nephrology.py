# -*- coding: utf-8 -*-
# Part of AlmightyCS. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models,_
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class ACSVascularAccess(models.Model):
    _name = 'acs.vascular.access'
    _description = "Vascular Access"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")


class ACSDialyzer(models.Model):
    _name = 'acs.dialyzer'
    _description = "Dialyzer"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")


class ACSDialysate(models.Model):
    _name = 'acs.dialysate'
    _description = "Dialysate"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")


class ACSRace(models.Model):
    _name = 'acs.race'
    _description = "Race"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")
    description = fields.Char(string="Description")


class ACSNephrologySchedule(models.Model):
    _name = 'acs.nephrology.schedule'
    _description = "Nephrology Schedule"

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")

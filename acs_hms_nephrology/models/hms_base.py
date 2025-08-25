# -*- coding: utf-8 -*-
# Part of AlmightyCS. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models,_


class ACSPatient(models.Model):
    _inherit = 'hms.patient'

    nephrology_care = fields.Boolean(string="Nephrology Care")
    debugging_treatment_start_date = fields.Date(string="Debugging Treatment Start Date")


class HrDepartment(models.Model): 
    _inherit = "hr.department"

    department_type = fields.Selection(selection_add=[('nephrology','Nephrology')])


class AcsPatientEvaluation(models.Model):
    _inherit = "acs.patient.evaluation"

    blood_flow = fields.Float(string="Blood Flow")
    venous_pressure = fields.Float(string="Venous Pressure")


class ACSProduct(models.Model):
    _inherit = 'product.template'

    hospital_product_type = fields.Selection(selection_add=[('nephrology_procedure','Nephrology Process')])


class Appointment(models.Model):
    _inherit = 'hms.appointment'

    blood_flow = fields.Float(related="evaluation_id.blood_flow" ,string="Blood Flow",readonly=True)
    venous_pressure = fields.Float(related="evaluation_id.venous_pressure",string="Venous Pressure",readonly=True)
    blood_group = fields.Selection(related="patient_id.blood_group", string='Blood Group')
    debugging_treatment = fields.Date(string="Debugging Treatment Start Date", related="patient_id.debugging_treatment_start_date")
    show_etiology = fields.Boolean(string="Show Etiology Of Chronic Renal Failure", default=False)
    etiology_of_chronic_renal_failure = fields.Text(string="Etiology Of Chronic Renal Failure")
    show_way_of_arrival = fields.Boolean(string="Show Way Of Arrival", default=False)
    way_of_arrival = fields.Text(string="Way Of Arrival")
    show_adverse_reactions = fields.Boolean(string="Show Adverse Reactions", default=False)
    adverse_reactions = fields.Text(string="Adverse Reactions")
    show_transplant_waiting_list = fields.Boolean(string="Show Transplant Waiting List", default=False)
    transplant_waiting_list = fields.Text('Transplant Waiting List')
    show_toxic_habits = fields.Boolean(string="Show Toxic Habits", default=False)
    toxic_habits = fields.Text(string="Toxic Habits")
    show_trauma = fields.Boolean(string="Show Trauma", default=False)
    trauma = fields.Text(string="Trauma")
    show_transfusions = fields.Boolean(string="Show Transfusions", default=False)
    transfusions = fields.Text(string="Transfusions")
    show_cesarean_operations = fields.Boolean(string="Show Cesarean Operations", default=False)
    cesarean_operations = fields.Text(string="Cesarean Operations")
    show_vaccinations = fields.Boolean(string="Show Vaccinations", default=False)
    vaccinations = fields.Text(string="Vaccinations")
    observation = fields.Text(string="Observation")


class AcsPatientProcedure(models.Model):
    _inherit = 'acs.patient.procedure'

    blood_group = fields.Selection(related="patient_id.blood_group", string='Blood Group')
    blood_culture = fields.Text(string="Blood Culture")
    actual_treatment = fields.Text(string="Actual Treatment")
    type_of_vascular_access = fields.Many2one('acs.vascular.access', string="Type Of Vascular Access")
    dialyzer_type = fields.Many2one('acs.dialyzer', string="Dialyzer Type", help="A dialyser is also known as an artificial kidney")
    nephrology_schedule_ids = fields.Many2many('acs.nephrology.schedule', 'acs_nephrology_schedule_rel', 'appointment_schedule_id', 'nephrology_schedule_id', string="Schedule")
    heparinization = fields.Text(string="Heparinization", help="Heparinization refers to the administration of heparin, a commonly used anticoagulant, to prevent blood clotting during renal replacement therapy")
    blood_flow = fields.Text(string="Blood Flow")
    dialysis_fluid_flow = fields.Text(string="Dialysis Fluid Flow")
    interdialysis_increase = fields.Text(string="Interdialysis Increase")
    last_ktv = fields.Float(string="Last KTV")
    type_of_dialysate = fields.Many2one('acs.dialysate', string="Type Of Dialysate")
    interdialysis_medication = fields.Text(string="Interdialysis Medication", help="occurring or carried out during hemodialysis")
    dry_weight = fields.Float(string="Dry Weight")
    dialysis_number = fields.Integer(string="Dialysis #")
    heparin_others = fields.Char(string="Heparin (others)")
    bicarbonate = fields.Char(string="Bicarbonate")
    potassium = fields.Char(string="K")
    sodium = fields.Char(string="Na")
    calcium = fields.Char(string="Ca")
    erythropoietin_units = fields.Char(string="Erythropoietin")

    def acs_consumable_line_data(self):
        data = {} 
        for line in self.consumable_line_ids:
            category = line.product_id.categ_id
            if category not in data:
                data[category] = [line]
            else:
                data[category].append(line)
        return data


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
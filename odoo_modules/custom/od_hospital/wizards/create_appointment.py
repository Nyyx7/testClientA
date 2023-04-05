from odoo import models,fields,api, _


class CreateAppointment(models.Model):
    _name = 'create.appointment'

    patient_id = fields.Many2one(
        string='patient',
    )
    
    appointment_date = fields.Date(
        string='appointment_date',
    )
    
    
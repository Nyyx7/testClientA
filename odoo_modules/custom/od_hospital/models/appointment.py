from odoo import models , fields, api ,_

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'appointment_date desc'


    def _get_default_note(self):
        return "this is the default note"


    name = fields.Char(
        string='appointment ID',
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _('New')
    )
    
    patient_id = fields.Many2one(
        'hospital.patient',
        string='patient_id',
        required=True
    )
    
    patient_age = fields.Integer(
        string='Age',
        related='patient_id.patient_age'
    )
    
    notes = fields.Text(
        string='Registration note',
        default = _get_default_note
        
    )   
    
    appointment_date = fields.Date(
        string='appointment_date',
        required=True
    )
    
    
    

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
           'hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result



    
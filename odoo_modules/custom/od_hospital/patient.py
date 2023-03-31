from odoo import models , fields , api ,_

class SalesOrderInherit(models.Model): 
    _inherit = 'sale.order'
    patient_name = fields.Char(
        string='Patient Name'
    )

class HospitalPatient(models.Model): 
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'patient record'
    _rec_name = 'patient_name'

    patient_name = fields.Char(
        string='Name', required=True
    )
    patient_age = fields.Integer(
        string='patient_age'
    )
    
    notes = fields.Text(
        string='notes'
    )
    
    image = fields.Binary(
        string='image'
    )
    
    name = fields.Char(
        string='Test',
    )
    name_seq = fields.Char(
        string='Order Reference', required=True ,copy=False,readonly=True,
        index=True,
        default=lambda self:_('New')
        
        
    )

    @api.model
    def create(self, vals):
        if vals.get('name_seq', 'New') == 'New':
            vals['name_seq'] = self.env['ir.sequence'].next_by_code(
           'hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result
    
    
    
    



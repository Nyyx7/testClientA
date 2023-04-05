from datetime import datetime, timedelta
from odoo import models, fields, api, SUPERUSER_ID
from odoo.exceptions import ValidationError


class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    LANGUAGES = [
        ('en_US', 'English'),
        ('fr_FR', 'French'),
        ('de_DE', 'German'),
        ('es_ES', 'Spanish'),
        ('it_IT', 'Italian'),
    ]

    lang_id = fields.Selection(LANGUAGES, string='Language', default='en_US')
    closing_date = fields.Date(string='Closing Date')
    
    #A la sauvegarde de l’opportunité, planifier automatiquement une activité « Reprendre contact » 1 mois avant 
    # la date de fermeture potentielle
    @api.onchange('closing_date')
    def schedule_activity(self):
        if self.closing_date:
            contact_date = datetime.strptime(self.closing_date.strftime('%Y-%m-%d'), '%Y-%m-%d') - timedelta(days=30)
            activity = self.sudo().env['mail.activity'].create({
                'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                'summary': 'Reprendre contact',
                'date_deadline': contact_date,
                'user_id': self.user_id.id,
                'res_id': self.id,
                'res_model_id': self.env.ref('crm.model_crm_lead').id,
                'note': 'This activity was automatically scheduled by the system.'
            })



#this is for 'Pistes en cours'
class ResPartner(models.Model):
    _inherit = 'res.partner'

    leads = fields.One2many('crm.lead', 'partner_id', string='Pistes en cours')
    
    @api.model
    def get_lead_view_id(self):
        view = self.env.ref('crm.lead_view_form', False)
        if not view:
            raise ValidationError('Lead view not found')
        return view.id
    
    def open_leads(self):
        view_id = self.get_lead_view_id()
        return {
            'name': 'Leads',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'tree,form',
            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
            'views': [(view_id, 'form')],
        }
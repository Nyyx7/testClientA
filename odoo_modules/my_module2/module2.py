from odoo import models, fields

class Module2(models.Model):
    _inherit = 'crm.lead'

    date_fermeture = fields.Date(string='Date de fermeture')









    """ @api.model
    def create(self, vals):
        lead = super(CrmLead, self).create(vals)
        if lead.date_fermeture:
            activity_type = self.env.ref('mail.mail_activity_data_todo')
            activity = self.env['mail.activity'].create({
                'activity_type_id': activity_type.id,
                'summary': 'Reprendre contact',
                'date_deadline': fields.Date.to_string(fields.Date.from_string(lead.date_fermeture) - relativedelta(months=1)),
                'res_model_id': self.env['ir.model']._get('crm.lead').id,
                'res_id': lead.id,
            })
        return lead """

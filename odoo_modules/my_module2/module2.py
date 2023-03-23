from odoo import fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    date_fermeture = fields.Date(string='Date de fermeture')

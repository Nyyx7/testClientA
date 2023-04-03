from odoo import models, fields, api

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
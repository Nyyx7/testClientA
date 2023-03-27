from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_lead = fields.Boolean(compute='_compute_is_lead', store=True)
    is_opportunity = fields.Boolean(compute='_compute_is_opportunity', store=True)

    @api.depends('type')
    def _compute_is_lead(self):
        for record in self:
            record.is_lead = True if record.type == 'lead' else False

    @api.depends('type')
    def _compute_is_opportunity(self):
        for record in self:
            record.is_opportunity = True if record.type == 'opportunity' else False

{
    'name': 'odoo hospital',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom module ',
    'description': 'This is new module ',
    'depends': ['base', 'mail','sale','crm'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'data/sequence2.xml',
        'views/patient.xml',
        'views/crm_lead_view_form_inherit.xml',
        'views/appointment.xml',

        
    ],
    'installable': True,
    'application':True,
    'auto_install':False,
}
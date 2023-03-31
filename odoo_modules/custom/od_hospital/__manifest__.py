{
    'name': 'odoo hospital',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom module ',
    'description': 'This is new module ',
    'depends': ['base', 'mail','sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'patient.xml',
    ],
    'installable': True,
    'application':True,
    'auto_install':False,
}
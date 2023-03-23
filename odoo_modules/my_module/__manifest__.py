{
    'name': 'My Module',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom module for managing leads',
    'description': 'This module adds custom fields and functionality to the lead model.',
    'depends': ['base', 'crm'],
    'data': [
        'views/lead_views.xml',
    ],
    'installable': True,
}
{
    'name': 'Refund',
    'version': '17.0.1.0.0',
    'summary': 'Refund',
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/refund_group.xml',
        'security/ir.model.access.csv',
        'views/refund_reason_view.xml',
        'views/reason_handler_view.xml',
        'views/refund_view.xml',
        'views/refund_student_form.xml',
        'views/refund_menu.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}

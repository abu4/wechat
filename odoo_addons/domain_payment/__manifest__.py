{
    'name': 'Payment Domain',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Payment',
    'summary': 'Centralized payment domain model and logic',
    'description': """
        This module provides the unified payment transaction model and state machine.
        All payment adapters (WeChat, Alipay, UnionPay) must map to this domain.
    """,
    'author': 'Your Team',
    'website': 'https://github.com/abu4/wechat',
    'depends': ['base', 'integration_hub', 'mail', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/payment_transaction_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

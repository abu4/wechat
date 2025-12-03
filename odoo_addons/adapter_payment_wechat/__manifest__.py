{
    'name': 'WeChat Pay Adapter',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Payment',
    'summary': 'WeChat Pay integration adapter for the payment domain',
    'description': """
        This adapter handles all interactions with WeChat Pay API.
        It subscribes to payment events and translates them into WeChat API calls.
    """,
    'author': 'Your Team',
    'website': 'https://github.com/abu4/wechat',
    'depends': ['integration_hub', 'domain_payment', 'payment'],
    'data': [
        'views/wechat_provider_views.xml',
        'data/payment_method_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

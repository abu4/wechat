{
    'name': 'Integration Hub',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Central event bus for all integrations.',
    'description': 'This module serves as the central event bus and router for all external system integrations, following the event-driven architecture.',
    'author': 'Your Team',
    'website': 'https://github.com/abu4/wechat',
    'depends': ['base', 'mail'],  # 基础依赖
    'data': [
        # 初始可以没有视图，后续添加事件定义视图等
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
    'data': [
        # 将事件模型添加到清单中
    ],
    'data': [
        # 将事件模型添加到清单中
    ],

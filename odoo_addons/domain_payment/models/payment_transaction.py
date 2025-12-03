# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class PaymentTransaction(models.Model):
    """
    支付领域统一交易模型。
    所有外部支付渠道（微信、支付宝、云闪付）的交易都必须映射到此模型。
    此模型是支付领域的“唯一真相源”。
    """
    _name = 'domain_payment.transaction'
    _description = 'Payment Transaction'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # 继承邮件跟踪功能
    _order = 'create_date desc'

    # ==== 核心字段 ====
    reference = fields.Char(
        string='Reference',
        required=True,
        readonly=True,
        index=True,
        help='内部交易参考号，通常与销售订单号关联'
    )
    amount = fields.Float(
        string='Amount',
        digits=(12, 2),
        required=True,
        tracking=True
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        required=True
    )
    partner_id = fields.Many2one(
        'res.partner',
        string='Customer',
        required=True
    )

    # ==== 统一状态机 ====
    # 这是关键设计：所有适配器都必须将外部状态映射到此状态机
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('pending', 'Pending'),      # 已请求支付，等待用户支付
            ('authorizing', 'Authorizing'), # 支付中（仅某些渠道需要）
            ('done', 'Done'),            # 支付成功
            ('cancel', 'Canceled'),      # 交易取消
            ('error', 'Error'),          # 支付失败
            ('refunding', 'Refunding'),  # 退款中
            ('refunded', 'Refunded'),    # 已退款
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
        copy=False
    )

    # ==== 渠道信息 ====
    provider_code = fields.Selection(
        selection=[],  # 将由具体适配器动态填充，如 [('wechat', 'WeChat Pay')]
        string='Payment Provider',
        required=True,
        readonly=True,
        help='标识交易来自哪个支付渠道'
    )
    provider_reference = fields.Char(
        string='Provider Transaction ID',
        readonly=True,
        help='支付平台返回的交易流水号'
    )

    # ==== 时间戳 ====
    payment_request_date = fields.Datetime(
        string='Payment Request Date',
        readonly=True
    )
    payment_received_date = fields.Datetime(
        string='Payment Received Date',
        readonly=True
    )

    # ==== 业务关联 ====
    # 注意：这里使用 Reference 字段，可以灵活关联 Sale Order、Account Invoice 等
    source_document = fields.Reference(
        selection=[
            ('sale.order', 'Sales Order'),
            ('account.move', 'Invoice'),
        ],
        string='Source Document',
        readonly=True,
        help='触发此次支付的源业务单据'
    )

    # ==== 方法 ====
    @api.model
    def create_from_event(self, event_data):
        """
        根据 'payment.required' 事件创建交易记录。
        这是支付领域服务的核心入口。
        """
        _logger.info(f"Creating transaction from event: {event_data.get('reference')}")
        
        # 这里是从事件数据创建交易的逻辑
        # 在实际实现中，需要更完整的数据验证和转换
        vals = {
            'reference': event_data.get('reference'),
            'amount': event_data.get('amount'),
            'currency_id': event_data.get('currency_id'),
            'partner_id': event_data.get('partner_id'),
            'state': 'pending',
            'payment_request_date': fields.Datetime.now(),
            # provider_code 应由具体适配器在后续步骤中设置
        }
        return self.create(vals)

    def action_confirm_payment(self, provider_code, provider_reference):
        """
        由支付适配器调用，确认支付成功。
        """
        self.ensure_one()
        if self.state != 'pending':
            raise UserError(f'Transaction {self.reference} is not in pending state.')
        
        self.write({
            'state': 'done',
            'provider_code': provider_code,
            'provider_reference': provider_reference,
            'payment_received_date': fields.Datetime.now(),
        })
        _logger.info(f"Transaction {self.reference} confirmed via {provider_code}.")
        return True

    def _get_state_display(self):
        """获取状态的显示值"""
        return dict(self._fields['state'].selection).get(self.state, self.state)

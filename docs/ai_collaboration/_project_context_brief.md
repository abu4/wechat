# Odoo 19+ 生态集成项目 - 上下文简报

## 项目状态
**日期**：2024-05-17
**阶段**：第一阶段 - 项目初始化与基础框架搭建
**当前目标**：完成支付领域核心模型 `PaymentTransaction` 的实现。

## 核心聚焦任务
1.  ~~定义并实现`integration_hub`中的基础事件（如`sale.order.confirmed`, `payment.required`）。~~ ✅ 已完成
2.  **已完成**：完成`domain_payment`中`PaymentTransaction`核心模型与状态机的草稿设计。✅ 已完成
3.  **已启动**制定首个支付适配器(`adapter_payment_wechat`)与领域层的接口契约。

## 最近关键决策 (ADR)
1.  **ADR-001：采用“集成总线+适配器”架构**：所有集成通过事件驱动，禁止直接修改Odoo核心模块。
2.  **ADR-002：支付领域统一模型**：所有支付渠道必须映射到`domain_payment`的统一状态机。
3.  **ADR-003：支付状态机设计**：采用8状态模型（draft→pending→done/cancel/error/refunding/refunded）。

## 本次会话目标
设计并实现 `domain_payment.transaction` 模型，作为支付领域的统一数据模型。

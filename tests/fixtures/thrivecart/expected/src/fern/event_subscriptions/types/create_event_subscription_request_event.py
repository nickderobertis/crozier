

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateEventSubscriptionRequestEvent(enum.StrEnum):
    """
    Event type to subscribe to. Use '*' for all events.
    """

    ALL = "*"
    ORDER_CREATED = "order_created"
    ORDER_PAYMENT_PRODUCT = "order_payment_product"
    ORDER_PAYMENT_BUMP = "order_payment_bump"
    ORDER_PAYMENT_UPSELL = "order_payment_upsell"
    ORDER_PAYMENT_DOWNSELL = "order_payment_downsell"
    ORDER_REBILL = "order_rebill"
    ORDER_REBILL_FAILED = "order_rebill_failed"
    ORDER_REBILL_COMPLETED = "order_rebill_completed"
    ORDER_REBILL_CANCELLED = "order_rebill_cancelled"
    ORDER_REFUND_PRODUCT = "order_refund_product"
    ORDER_REFUND_BUMP = "order_refund_bump"
    ORDER_REFUND_UPSELL = "order_refund_upsell"
    ORDER_REFUND_DOWNSELL = "order_refund_downsell"
    SUBSCRIPTION_PAUSED = "subscription_paused"
    SUBSCRIPTION_RESUMED = "subscription_resumed"
    CART_ABANDONED = "cart_abandoned"
    AFFILIATE_APPROVED = "affiliate_approved"
    AFFILIATE_REJECTED = "affiliate_rejected"
    AFFILIATE_COMMISSION_EARNED = "affiliate_commission_earned"
    AFFILIATE_COMMISSION_PAYOUT = "affiliate_commission_payout"
    AFFILIATE_COMMISSION_REFUND = "affiliate_commission_refund"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        order_created: typing.Callable[[], T_Result],
        order_payment_product: typing.Callable[[], T_Result],
        order_payment_bump: typing.Callable[[], T_Result],
        order_payment_upsell: typing.Callable[[], T_Result],
        order_payment_downsell: typing.Callable[[], T_Result],
        order_rebill: typing.Callable[[], T_Result],
        order_rebill_failed: typing.Callable[[], T_Result],
        order_rebill_completed: typing.Callable[[], T_Result],
        order_rebill_cancelled: typing.Callable[[], T_Result],
        order_refund_product: typing.Callable[[], T_Result],
        order_refund_bump: typing.Callable[[], T_Result],
        order_refund_upsell: typing.Callable[[], T_Result],
        order_refund_downsell: typing.Callable[[], T_Result],
        subscription_paused: typing.Callable[[], T_Result],
        subscription_resumed: typing.Callable[[], T_Result],
        cart_abandoned: typing.Callable[[], T_Result],
        affiliate_approved: typing.Callable[[], T_Result],
        affiliate_rejected: typing.Callable[[], T_Result],
        affiliate_commission_earned: typing.Callable[[], T_Result],
        affiliate_commission_payout: typing.Callable[[], T_Result],
        affiliate_commission_refund: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateEventSubscriptionRequestEvent.ALL:
            return all_()
        if self is CreateEventSubscriptionRequestEvent.ORDER_CREATED:
            return order_created()
        if self is CreateEventSubscriptionRequestEvent.ORDER_PAYMENT_PRODUCT:
            return order_payment_product()
        if self is CreateEventSubscriptionRequestEvent.ORDER_PAYMENT_BUMP:
            return order_payment_bump()
        if self is CreateEventSubscriptionRequestEvent.ORDER_PAYMENT_UPSELL:
            return order_payment_upsell()
        if self is CreateEventSubscriptionRequestEvent.ORDER_PAYMENT_DOWNSELL:
            return order_payment_downsell()
        if self is CreateEventSubscriptionRequestEvent.ORDER_REBILL:
            return order_rebill()
        if self is CreateEventSubscriptionRequestEvent.ORDER_REBILL_FAILED:
            return order_rebill_failed()
        if self is CreateEventSubscriptionRequestEvent.ORDER_REBILL_COMPLETED:
            return order_rebill_completed()
        if self is CreateEventSubscriptionRequestEvent.ORDER_REBILL_CANCELLED:
            return order_rebill_cancelled()
        if self is CreateEventSubscriptionRequestEvent.ORDER_REFUND_PRODUCT:
            return order_refund_product()
        if self is CreateEventSubscriptionRequestEvent.ORDER_REFUND_BUMP:
            return order_refund_bump()
        if self is CreateEventSubscriptionRequestEvent.ORDER_REFUND_UPSELL:
            return order_refund_upsell()
        if self is CreateEventSubscriptionRequestEvent.ORDER_REFUND_DOWNSELL:
            return order_refund_downsell()
        if self is CreateEventSubscriptionRequestEvent.SUBSCRIPTION_PAUSED:
            return subscription_paused()
        if self is CreateEventSubscriptionRequestEvent.SUBSCRIPTION_RESUMED:
            return subscription_resumed()
        if self is CreateEventSubscriptionRequestEvent.CART_ABANDONED:
            return cart_abandoned()
        if self is CreateEventSubscriptionRequestEvent.AFFILIATE_APPROVED:
            return affiliate_approved()
        if self is CreateEventSubscriptionRequestEvent.AFFILIATE_REJECTED:
            return affiliate_rejected()
        if self is CreateEventSubscriptionRequestEvent.AFFILIATE_COMMISSION_EARNED:
            return affiliate_commission_earned()
        if self is CreateEventSubscriptionRequestEvent.AFFILIATE_COMMISSION_PAYOUT:
            return affiliate_commission_payout()
        if self is CreateEventSubscriptionRequestEvent.AFFILIATE_COMMISSION_REFUND:
            return affiliate_commission_refund()

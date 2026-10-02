

import typing

CreateEventSubscriptionRequestEvent = typing.Union[
    typing.Literal[
        "*",
        "order_created",
        "order_payment_product",
        "order_payment_bump",
        "order_payment_upsell",
        "order_payment_downsell",
        "order_rebill",
        "order_rebill_failed",
        "order_rebill_completed",
        "order_rebill_cancelled",
        "order_refund_product",
        "order_refund_bump",
        "order_refund_upsell",
        "order_refund_downsell",
        "subscription_paused",
        "subscription_resumed",
        "cart_abandoned",
        "affiliate_approved",
        "affiliate_rejected",
        "affiliate_commission_earned",
        "affiliate_commission_payout",
        "affiliate_commission_refund",
    ],
    typing.Any,
]

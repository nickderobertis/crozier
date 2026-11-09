

import typing

IntentTraceReasonCode = typing.Union[
    typing.Literal[
        "price_sensitivity",
        "shipping_cost",
        "shipping_speed",
        "product_fit",
        "trust_security",
        "returns_policy",
        "payment_options",
        "comparison",
        "timing_deferred",
        "other",
    ],
    typing.Any,
]



import typing

CheckoutOptionsPaymentType = typing.Union[
    typing.Literal[
        "CARD_PRESENT", "MANUAL_CARD_ENTRY", "FELICA_ID", "FELICA_QUICPAY", "FELICA_TRANSPORTATION_GROUP", "FELICA_ALL"
    ],
    typing.Any,
]

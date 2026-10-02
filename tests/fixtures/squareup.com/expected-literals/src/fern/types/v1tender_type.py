

import typing

V1TenderType = typing.Union[
    typing.Literal[
        "CREDIT_CARD", "CASH", "THIRD_PARTY_CARD", "NO_SALE", "SQUARE_WALLET", "SQUARE_GIFT_CARD", "UNKNOWN", "OTHER"
    ],
    typing.Any,
]

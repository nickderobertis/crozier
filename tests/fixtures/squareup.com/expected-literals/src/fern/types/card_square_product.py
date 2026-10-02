

import typing

CardSquareProduct = typing.Union[
    typing.Literal[
        "UNKNOWN_SQUARE_PRODUCT",
        "CONNECT_API",
        "DASHBOARD",
        "REGISTER_CLIENT",
        "BUYER_DASHBOARD",
        "WEB",
        "INVOICES",
        "GIFT_CARD",
        "VIRTUAL_TERMINAL",
        "READER_SDK",
    ],
    typing.Any,
]

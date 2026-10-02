

import typing

GiftCardActivityType = typing.Union[
    typing.Literal[
        "ACTIVATE",
        "LOAD",
        "REDEEM",
        "CLEAR_BALANCE",
        "DEACTIVATE",
        "ADJUST_INCREMENT",
        "ADJUST_DECREMENT",
        "REFUND",
        "UNLINKED_ACTIVITY_REFUND",
        "IMPORT",
        "BLOCK",
        "UNBLOCK",
        "IMPORT_REVERSAL",
    ],
    typing.Any,
]

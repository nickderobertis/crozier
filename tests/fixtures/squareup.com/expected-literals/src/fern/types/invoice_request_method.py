

import typing

InvoiceRequestMethod = typing.Union[
    typing.Literal[
        "EMAIL",
        "CHARGE_CARD_ON_FILE",
        "SHARE_MANUALLY",
        "CHARGE_BANK_ON_FILE",
        "SMS",
        "SMS_CHARGE_CARD_ON_FILE",
        "SMS_CHARGE_BANK_ON_FILE",
    ],
    typing.Any,
]



import typing

TransactionFullSimplePaymentType = typing.Union[
    typing.Literal[
        "CASH",
        "CC_SIGNATURE",
        "ELV",
        "ELV_WITHOUT_SIGNATURE",
        "CC_CUSTOMER_ENTERED",
        "MANUAL_ENTRY",
        "EMV",
        "RECURRING",
        "BALANCE",
        "MOTO",
        "BOLETO",
        "APM",
        "BITCOIN",
        "CARD",
    ],
    typing.Any,
]

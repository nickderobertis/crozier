

import typing

PaymentScheme = typing.Union[
    typing.Literal["LOCAL_DEFAULT", "LOCAL_INSTANT", "SEPA_CREDIT_TRANSFER", "SEPA_CREDIT_TRANSFER_INSTANT"], typing.Any
]

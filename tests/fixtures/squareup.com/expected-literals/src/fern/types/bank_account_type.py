

import typing

BankAccountType = typing.Union[
    typing.Literal["CHECKING", "SAVINGS", "INVESTMENT", "OTHER", "BUSINESS_CHECKING"], typing.Any
]

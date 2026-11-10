

import typing

WalletTransactionStatus = typing.Union[
    typing.Literal["AUTHORISING", "INITIATED", "EXECUTED", "SETTLED", "BLOCKED", "FAILED"], typing.Any
]

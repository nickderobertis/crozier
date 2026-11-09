

import typing

WalletTransactionType = typing.Union[
    typing.Literal["BANK_TRANSFER", "PAYOUT", "PIS_PAY_IN", "REFUND", "FUNDS_SWEEP"], typing.Any
]

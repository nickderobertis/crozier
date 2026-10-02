

import typing

TransactionType = typing.Union[
    typing.Literal["purchase", "rebill", "refund", "failed_rebill", "cancelled", "pending"], typing.Any
]

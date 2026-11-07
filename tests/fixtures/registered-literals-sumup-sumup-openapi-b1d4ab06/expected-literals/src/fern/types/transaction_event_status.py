

import typing

TransactionEventStatus = typing.Union[
    typing.Literal["FAILED", "PAID_OUT", "PENDING", "RECONCILED", "REFUNDED", "SCHEDULED", "SUCCESSFUL"], typing.Any
]

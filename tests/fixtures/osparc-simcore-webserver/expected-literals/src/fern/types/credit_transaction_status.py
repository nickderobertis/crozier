

import typing

CreditTransactionStatus = typing.Union[
    typing.Literal["PENDING", "BILLED", "IN_DEBT", "NOT_BILLED", "REQUIRES_MANUAL_REVIEW"], typing.Any
]



import typing

BankTransferEventType = typing.Union[typing.Literal["pending", "cancelled", "failed", "posted", "reversed"], typing.Any]

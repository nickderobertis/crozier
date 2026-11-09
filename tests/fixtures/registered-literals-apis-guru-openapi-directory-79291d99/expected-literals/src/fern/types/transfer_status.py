

import typing

TransferStatus = typing.Union[
    typing.Literal["pending", "posted", "settled", "cancelled", "failed", "returned"], typing.Any
]

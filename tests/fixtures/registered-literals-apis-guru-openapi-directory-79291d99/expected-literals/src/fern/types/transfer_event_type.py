

import typing

TransferEventType = typing.Union[
    typing.Literal[
        "pending", "cancelled", "failed", "posted", "settled", "returned", "swept", "swept_settled", "return_swept"
    ],
    typing.Any,
]

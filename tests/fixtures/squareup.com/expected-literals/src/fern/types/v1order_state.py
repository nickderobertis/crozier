

import typing

V1OrderState = typing.Union[
    typing.Literal["PENDING", "OPEN", "COMPLETED", "CANCELED", "REFUNDED", "REJECTED"], typing.Any
]

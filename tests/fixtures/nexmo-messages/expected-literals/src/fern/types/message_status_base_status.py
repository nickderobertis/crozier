

import typing

MessageStatusBaseStatus = typing.Union[
    typing.Literal["submitted", "delivered", "rejected", "undeliverable"], typing.Any
]



import typing

MessageStatusMessengerStatus = typing.Union[
    typing.Literal["submitted", "delivered", "rejected", "undeliverable", "read"], typing.Any
]

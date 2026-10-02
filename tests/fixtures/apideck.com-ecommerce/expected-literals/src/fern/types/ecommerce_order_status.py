

import typing

EcommerceOrderStatus = typing.Union[
    typing.Literal["active", "completed", "cancelled", "archived", "unknown"], typing.Any
]

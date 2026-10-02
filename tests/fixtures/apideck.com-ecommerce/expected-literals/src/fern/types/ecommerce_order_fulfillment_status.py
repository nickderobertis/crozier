

import typing

EcommerceOrderFulfillmentStatus = typing.Union[
    typing.Literal["pending", "shipped", "partial", "delivered", "cancelled", "returned", "unknown"], typing.Any
]

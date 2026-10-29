

import typing

RefundOrdersResponseStatus = typing.Union[
    typing.Literal["pending", "unfulfilled", "fulfilled", "disputed", "dispute-lost", "refunded"], typing.Any
]

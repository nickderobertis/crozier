

import typing

TotalType = typing.Union[
    typing.Literal["items_base_amount", "items_discount", "subtotal", "discount", "fulfillment", "tax", "fee", "total"],
    typing.Any,
]

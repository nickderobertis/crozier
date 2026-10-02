

import typing

InventorySearchRequestSortField = typing.Union[
    typing.Literal[
        "price", "list_price", "offered_price", "msrp", "mileage", "year", "make", "model", "stock", "updated_at"
    ],
    typing.Any,
]

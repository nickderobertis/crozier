

import typing

InventoryState = typing.Union[
    typing.Literal[
        "CUSTOM",
        "IN_STOCK",
        "SOLD",
        "RETURNED_BY_CUSTOMER",
        "RESERVED_FOR_SALE",
        "SOLD_ONLINE",
        "ORDERED_FROM_VENDOR",
        "RECEIVED_FROM_VENDOR",
        "IN_TRANSIT_TO",
        "NONE",
        "WASTE",
        "UNLINKED_RETURN",
        "COMPOSED",
        "DECOMPOSED",
        "SUPPORTED_BY_NEWER_VERSION",
    ],
    typing.Any,
]



import typing

TablePredicateAnyAnyItemFieldOp = typing.Union[
    typing.Literal[
        "eq",
        "ne",
        "gt",
        "gte",
        "lt",
        "lte",
        "in",
        "nin",
        "contains",
        "ncontains",
        "startsWith",
        "endsWith",
        "like",
        "ilike",
        "nlike",
        "nilike",
        "isEmpty",
        "isNotEmpty",
        "isNull",
        "isNotNull",
    ],
    typing.Any,
]

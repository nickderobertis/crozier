

import typing

QueryGroupFieldOp = typing.Union[
    typing.Literal[
        "lt",
        "lte",
        "eq",
        "neq",
        "gte",
        "gt",
        "in",
        "startsWith",
        "endsWith",
        "contains",
        "isnotnull",
        "isnull",
        "exists",
        "notexists",
        "numberof",
    ],
    typing.Any,
]

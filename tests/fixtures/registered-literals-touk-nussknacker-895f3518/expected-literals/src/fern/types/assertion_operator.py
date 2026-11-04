

import typing

AssertionOperator = typing.Union[
    typing.Literal[
        "contains",
        "equals",
        "greaterThan",
        "greaterThanOrEqual",
        "hasSize",
        "lessThan",
        "lessThanOrEqual",
        "matches",
        "notEquals",
    ],
    typing.Any,
]

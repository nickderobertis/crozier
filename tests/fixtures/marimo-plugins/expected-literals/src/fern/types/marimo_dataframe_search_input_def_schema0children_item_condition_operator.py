

import typing

MarimoDataframeSearchInputDefSchema0ChildrenItemConditionOperator = typing.Union[
    typing.Literal[
        "is_true",
        "is_false",
        "==",
        "!=",
        ">",
        ">=",
        "<",
        "<=",
        "between",
        "is_null",
        "is_not_null",
        "equals",
        "does_not_equal",
        "contains",
        "regex",
        "starts_with",
        "ends_with",
        "in",
        "not_in",
        "is_empty",
    ],
    typing.Any,
]

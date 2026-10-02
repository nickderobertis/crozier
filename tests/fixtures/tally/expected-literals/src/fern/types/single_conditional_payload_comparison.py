

import typing

SingleConditionalPayloadComparison = typing.Union[
    typing.Literal[
        "IS",
        "IS_NOT",
        "IS_ANY_OF",
        "IS_NOT_ANY_OF",
        "IS_EVERY_OF",
        "CONTAINS",
        "DOES_NOT_CONTAIN",
        "STARTS_WITH",
        "DOES_NOT_START_WITH",
        "ENDS_WITH",
        "DOES_NOT_END_WITH",
        "IS_EMPTY",
        "IS_NOT_EMPTY",
        "EQUAL",
        "NOT_EQUAL",
        "GREATER_THAN",
        "LESS_THAN",
        "GREATER_OR_EQUAL_THAN",
        "LESS_OR_EQUAL_THAN",
        "IS_BEFORE",
        "IS_AFTER",
    ],
    typing.Any,
]

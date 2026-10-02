

import typing

CommunicationModelsFieldFilterComparison = typing.Union[
    typing.Literal[
        "Equal", "NotEqual", "LessThan", "LessThanOrEqual", "GreaterThan", "GreaterThanOrEqual", "In", "NotIn"
    ],
    typing.Any,
]

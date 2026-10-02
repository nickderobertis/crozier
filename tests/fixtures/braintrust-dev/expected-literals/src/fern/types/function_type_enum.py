

import typing

FunctionTypeEnum = typing.Union[
    typing.Literal[
        "llm",
        "scorer",
        "task",
        "tool",
        "custom_view",
        "preprocessor",
        "facet",
        "classifier",
        "tag",
        "parameters",
        "sandbox",
    ],
    typing.Any,
]

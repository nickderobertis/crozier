

import typing

SpanType = typing.Union[
    typing.Literal[
        "llm",
        "score",
        "function",
        "eval",
        "task",
        "tool",
        "automation",
        "facet",
        "preprocessor",
        "classifier",
        "review",
    ],
    typing.Any,
]

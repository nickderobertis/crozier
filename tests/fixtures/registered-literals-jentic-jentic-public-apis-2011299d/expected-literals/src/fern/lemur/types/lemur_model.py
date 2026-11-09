

import typing

LemurModel = typing.Union[
    typing.Literal[
        "anthropic/claude-sonnet-4-20250514",
        "anthropic/claude-opus-4-20250514",
        "anthropic/claude-3-7-sonnet-20250219",
        "anthropic/claude-3-5-sonnet",
        "anthropic/claude-3-5-haiku-20241022",
        "anthropic/claude-3-opus",
        "anthropic/claude-3-haiku",
    ],
    typing.Any,
]

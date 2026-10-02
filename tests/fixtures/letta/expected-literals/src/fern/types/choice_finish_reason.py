

import typing

ChoiceFinishReason = typing.Union[
    typing.Literal["stop", "length", "tool_calls", "content_filter", "function_call"], typing.Any
]

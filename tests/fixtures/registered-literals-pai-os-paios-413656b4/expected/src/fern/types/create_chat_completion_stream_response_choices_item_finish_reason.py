

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateChatCompletionStreamResponseChoicesItemFinishReason(enum.StrEnum):
    """
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
    `length` if the maximum number of tokens specified in the request was reached,
    `content_filter` if content was omitted due to a flag from our content filters,
    `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
    """

    STOP = "stop"
    LENGTH = "length"
    TOOL_CALLS = "tool_calls"
    CONTENT_FILTER = "content_filter"
    FUNCTION_CALL = "function_call"

    def visit(
        self,
        stop: typing.Callable[[], T_Result],
        length: typing.Callable[[], T_Result],
        tool_calls: typing.Callable[[], T_Result],
        content_filter: typing.Callable[[], T_Result],
        function_call: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateChatCompletionStreamResponseChoicesItemFinishReason.STOP:
            return stop()
        if self is CreateChatCompletionStreamResponseChoicesItemFinishReason.LENGTH:
            return length()
        if self is CreateChatCompletionStreamResponseChoicesItemFinishReason.TOOL_CALLS:
            return tool_calls()
        if self is CreateChatCompletionStreamResponseChoicesItemFinishReason.CONTENT_FILTER:
            return content_filter()
        if self is CreateChatCompletionStreamResponseChoicesItemFinishReason.FUNCTION_CALL:
            return function_call()

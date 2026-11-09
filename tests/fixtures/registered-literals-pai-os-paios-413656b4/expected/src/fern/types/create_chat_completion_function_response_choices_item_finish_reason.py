

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateChatCompletionFunctionResponseChoicesItemFinishReason(enum.StrEnum):
    """
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence, `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was omitted due to a flag from our content filters, or `function_call` if the model called a function.
    """

    STOP = "stop"
    LENGTH = "length"
    FUNCTION_CALL = "function_call"
    CONTENT_FILTER = "content_filter"

    def visit(
        self,
        stop: typing.Callable[[], T_Result],
        length: typing.Callable[[], T_Result],
        function_call: typing.Callable[[], T_Result],
        content_filter: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateChatCompletionFunctionResponseChoicesItemFinishReason.STOP:
            return stop()
        if self is CreateChatCompletionFunctionResponseChoicesItemFinishReason.LENGTH:
            return length()
        if self is CreateChatCompletionFunctionResponseChoicesItemFinishReason.FUNCTION_CALL:
            return function_call()
        if self is CreateChatCompletionFunctionResponseChoicesItemFinishReason.CONTENT_FILTER:
            return content_filter()

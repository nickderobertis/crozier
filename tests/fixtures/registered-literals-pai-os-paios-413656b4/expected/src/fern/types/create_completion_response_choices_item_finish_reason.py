

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateCompletionResponseChoicesItemFinishReason(enum.StrEnum):
    """
    The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
    `length` if the maximum number of tokens specified in the request was reached,
    or `content_filter` if content was omitted due to a flag from our content filters.
    """

    STOP = "stop"
    LENGTH = "length"
    CONTENT_FILTER = "content_filter"

    def visit(
        self,
        stop: typing.Callable[[], T_Result],
        length: typing.Callable[[], T_Result],
        content_filter: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateCompletionResponseChoicesItemFinishReason.STOP:
            return stop()
        if self is CreateCompletionResponseChoicesItemFinishReason.LENGTH:
            return length()
        if self is CreateCompletionResponseChoicesItemFinishReason.CONTENT_FILTER:
            return content_filter()

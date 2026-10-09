

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OpenAiCompletionObject(enum.StrEnum):
    COMPLETION = "completion"
    COMPLETION_CHUNK = "completion.chunk"

    def visit(
        self, completion: typing.Callable[[], T_Result], completion_chunk: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is OpenAiCompletionObject.COMPLETION:
            return completion()
        if self is OpenAiCompletionObject.COMPLETION_CHUNK:
            return completion_chunk()

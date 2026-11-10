

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTranscriptionRequestTimestampGranularitiesItem(enum.StrEnum):
    WORD = "word"
    SEGMENT = "segment"

    def visit(self, word: typing.Callable[[], T_Result], segment: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateTranscriptionRequestTimestampGranularitiesItem.WORD:
            return word()
        if self is CreateTranscriptionRequestTimestampGranularitiesItem.SEGMENT:
            return segment()

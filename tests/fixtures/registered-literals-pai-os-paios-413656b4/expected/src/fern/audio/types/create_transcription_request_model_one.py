

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTranscriptionRequestModelOne(enum.StrEnum):
    WHISPER1 = "whisper-1"

    def visit(self, whisper1: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateTranscriptionRequestModelOne.WHISPER1:
            return whisper1()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecordingFormatContainer(enum.StrEnum):
    WAV = "wav"

    def visit(self, wav: typing.Callable[[], T_Result]) -> T_Result:
        if self is RecordingFormatContainer.WAV:
            return wav()

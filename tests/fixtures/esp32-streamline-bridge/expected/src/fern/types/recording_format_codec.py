

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RecordingFormatCodec(enum.StrEnum):
    PCM_S16LE = "pcm_s16le"

    def visit(self, pcm_s16le: typing.Callable[[], T_Result]) -> T_Result:
        if self is RecordingFormatCodec.PCM_S16LE:
            return pcm_s16le()

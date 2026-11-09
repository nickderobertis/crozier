

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TranscriptRemoveAudioTags(enum.StrEnum):
    ALL = "all"
    SPEAKER = "speaker"

    def visit(self, all_: typing.Callable[[], T_Result], speaker: typing.Callable[[], T_Result]) -> T_Result:
        if self is TranscriptRemoveAudioTags.ALL:
            return all_()
        if self is TranscriptRemoveAudioTags.SPEAKER:
            return speaker()



import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RunIntelligenceResponseItemMediaType(enum.StrEnum):
    """
    Type of media analyzed
    """

    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"

    def visit(
        self,
        audio: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunIntelligenceResponseItemMediaType.AUDIO:
            return audio()
        if self is RunIntelligenceResponseItemMediaType.VIDEO:
            return video()
        if self is RunIntelligenceResponseItemMediaType.IMAGE:
            return image()



import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetIntelligenceResponseItemMediaType(enum.StrEnum):
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
        if self is GetIntelligenceResponseItemMediaType.AUDIO:
            return audio()
        if self is GetIntelligenceResponseItemMediaType.VIDEO:
            return video()
        if self is GetIntelligenceResponseItemMediaType.IMAGE:
            return image()

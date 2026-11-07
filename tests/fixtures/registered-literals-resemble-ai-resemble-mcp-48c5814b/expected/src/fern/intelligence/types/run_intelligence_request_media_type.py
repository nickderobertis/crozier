

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RunIntelligenceRequestMediaType(enum.StrEnum):
    """
    Explicit media type (auto-detected if not provided)
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
        if self is RunIntelligenceRequestMediaType.AUDIO:
            return audio()
        if self is RunIntelligenceRequestMediaType.VIDEO:
            return video()
        if self is RunIntelligenceRequestMediaType.IMAGE:
            return image()

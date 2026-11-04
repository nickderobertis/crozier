

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ApplyWatermarkResponseItemMediaType(enum.StrEnum):
    """
    Detected media type of the source file.
    """

    AUDIO = "audio"
    IMAGE = "image"
    VIDEO = "video"

    def visit(
        self,
        audio: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApplyWatermarkResponseItemMediaType.AUDIO:
            return audio()
        if self is ApplyWatermarkResponseItemMediaType.IMAGE:
            return image()
        if self is ApplyWatermarkResponseItemMediaType.VIDEO:
            return video()



import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWatermarkDetectionResultResponseItemMediaType(enum.StrEnum):
    AUDIO = "audio"
    IMAGE = "image"
    VIDEO = "video"

    def visit(
        self,
        audio: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWatermarkDetectionResultResponseItemMediaType.AUDIO:
            return audio()
        if self is GetWatermarkDetectionResultResponseItemMediaType.IMAGE:
            return image()
        if self is GetWatermarkDetectionResultResponseItemMediaType.VIDEO:
            return video()

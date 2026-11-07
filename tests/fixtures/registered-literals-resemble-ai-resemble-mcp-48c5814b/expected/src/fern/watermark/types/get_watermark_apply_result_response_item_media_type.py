

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWatermarkApplyResultResponseItemMediaType(enum.StrEnum):
    AUDIO = "audio"
    IMAGE = "image"
    VIDEO = "video"

    def visit(
        self,
        audio: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWatermarkApplyResultResponseItemMediaType.AUDIO:
            return audio()
        if self is GetWatermarkApplyResultResponseItemMediaType.IMAGE:
            return image()
        if self is GetWatermarkApplyResultResponseItemMediaType.VIDEO:
            return video()



import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDetectionResponseItemMediaType(enum.StrEnum):
    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"

    def visit(
        self,
        audio: typing.Callable[[], T_Result],
        video: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDetectionResponseItemMediaType.AUDIO:
            return audio()
        if self is GetDetectionResponseItemMediaType.VIDEO:
            return video()
        if self is GetDetectionResponseItemMediaType.IMAGE:
            return image()

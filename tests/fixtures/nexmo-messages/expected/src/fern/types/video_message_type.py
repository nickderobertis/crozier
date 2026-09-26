

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VideoMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `video` in this field
    """

    VIDEO = "video"

    def visit(self, video: typing.Callable[[], T_Result]) -> T_Result:
        if self is VideoMessageType.VIDEO:
            return video()

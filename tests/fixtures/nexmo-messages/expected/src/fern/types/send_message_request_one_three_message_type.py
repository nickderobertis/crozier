

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SendMessageRequestOneThreeMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `video` in this field.

    For best device and network support .mp4 is recommended. Not supported for US short codes.
    """

    VIDEO = "video"

    def visit(self, video: typing.Callable[[], T_Result]) -> T_Result:
        if self is SendMessageRequestOneThreeMessageType.VIDEO:
            return video()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SendMessageRequestOneTwoMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `audio` in this field.

    For best device and network support .mp3 is recommended. Not supported for US short codes.
    """

    AUDIO = "audio"

    def visit(self, audio: typing.Callable[[], T_Result]) -> T_Result:
        if self is SendMessageRequestOneTwoMessageType.AUDIO:
            return audio()

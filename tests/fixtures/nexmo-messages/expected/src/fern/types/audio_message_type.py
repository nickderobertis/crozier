

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AudioMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `audio` in this field
    """

    AUDIO = "audio"

    def visit(self, audio: typing.Callable[[], T_Result]) -> T_Result:
        if self is AudioMessageType.AUDIO:
            return audio()

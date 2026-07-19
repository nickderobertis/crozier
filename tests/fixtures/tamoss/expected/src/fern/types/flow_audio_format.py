

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowAudioFormat(enum.StrEnum):
    """
    The primary content type URN for the Flow.
    """

    URN_X_NMOS_FORMAT_AUDIO = "urn:x-nmos:format:audio"

    def visit(self, urn_x_nmos_format_audio: typing.Callable[[], T_Result]) -> T_Result:
        if self is FlowAudioFormat.URN_X_NMOS_FORMAT_AUDIO:
            return urn_x_nmos_format_audio()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelFromWebsocketContentType(enum.StrEnum):
    AUDIO_L16RATE8000 = "audio/l16;rate=8000"
    AUDIO_L16RATE16000 = "audio/l16;rate=16000"

    def visit(
        self, audio_l16rate8000: typing.Callable[[], T_Result], audio_l16rate16000: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ChannelFromWebsocketContentType.AUDIO_L16RATE8000:
            return audio_l16rate8000()
        if self is ChannelFromWebsocketContentType.AUDIO_L16RATE16000:
            return audio_l16rate16000()

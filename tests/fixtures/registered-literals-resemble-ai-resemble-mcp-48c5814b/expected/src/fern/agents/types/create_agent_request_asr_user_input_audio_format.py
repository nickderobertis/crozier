

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateAgentRequestAsrUserInputAudioFormat(enum.StrEnum):
    PCM8000 = "pcm_8000"
    PCM16000 = "pcm_16000"
    PCM22050 = "pcm_22050"
    PCM24000 = "pcm_24000"
    PCM44100 = "pcm_44100"
    PCM48000 = "pcm_48000"
    ULAW8000 = "ulaw_8000"

    def visit(
        self,
        pcm8000: typing.Callable[[], T_Result],
        pcm16000: typing.Callable[[], T_Result],
        pcm22050: typing.Callable[[], T_Result],
        pcm24000: typing.Callable[[], T_Result],
        pcm44100: typing.Callable[[], T_Result],
        pcm48000: typing.Callable[[], T_Result],
        ulaw8000: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateAgentRequestAsrUserInputAudioFormat.PCM8000:
            return pcm8000()
        if self is CreateAgentRequestAsrUserInputAudioFormat.PCM16000:
            return pcm16000()
        if self is CreateAgentRequestAsrUserInputAudioFormat.PCM22050:
            return pcm22050()
        if self is CreateAgentRequestAsrUserInputAudioFormat.PCM24000:
            return pcm24000()
        if self is CreateAgentRequestAsrUserInputAudioFormat.PCM44100:
            return pcm44100()
        if self is CreateAgentRequestAsrUserInputAudioFormat.PCM48000:
            return pcm48000()
        if self is CreateAgentRequestAsrUserInputAudioFormat.ULAW8000:
            return ulaw8000()

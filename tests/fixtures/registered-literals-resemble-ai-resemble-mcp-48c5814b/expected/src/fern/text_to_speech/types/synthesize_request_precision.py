

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SynthesizeRequestPrecision(enum.StrEnum):
    """
    Audio precision for WAV output
    """

    MULAW = "MULAW"
    PCM16 = "PCM_16"
    PCM24 = "PCM_24"
    PCM32 = "PCM_32"

    def visit(
        self,
        mulaw: typing.Callable[[], T_Result],
        pcm16: typing.Callable[[], T_Result],
        pcm24: typing.Callable[[], T_Result],
        pcm32: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SynthesizeRequestPrecision.MULAW:
            return mulaw()
        if self is SynthesizeRequestPrecision.PCM16:
            return pcm16()
        if self is SynthesizeRequestPrecision.PCM24:
            return pcm24()
        if self is SynthesizeRequestPrecision.PCM32:
            return pcm32()

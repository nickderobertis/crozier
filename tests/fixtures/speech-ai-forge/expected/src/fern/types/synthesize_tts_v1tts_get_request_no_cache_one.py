

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SynthesizeTtsV1TtsGetRequestNoCacheOne(enum.StrEnum):
    ON = "on"
    OFF = "off"

    def visit(self, on: typing.Callable[[], T_Result], off: typing.Callable[[], T_Result]) -> T_Result:
        if self is SynthesizeTtsV1TtsGetRequestNoCacheOne.ON:
            return on()
        if self is SynthesizeTtsV1TtsGetRequestNoCacheOne.OFF:
            return off()

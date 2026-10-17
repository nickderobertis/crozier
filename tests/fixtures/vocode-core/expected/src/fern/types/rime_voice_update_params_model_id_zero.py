

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RimeVoiceUpdateParamsModelIdZero(enum.StrEnum):
    MIST = "mist"
    V1 = "v1"

    def visit(self, mist: typing.Callable[[], T_Result], v1: typing.Callable[[], T_Result]) -> T_Result:
        if self is RimeVoiceUpdateParamsModelIdZero.MIST:
            return mist()
        if self is RimeVoiceUpdateParamsModelIdZero.V1:
            return v1()

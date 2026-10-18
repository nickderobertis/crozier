

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VocodeVoiceUpdateParamsVoiceIdZero(enum.StrEnum):
    JOE = "joe"

    def visit(self, joe: typing.Callable[[], T_Result]) -> T_Result:
        if self is VocodeVoiceUpdateParamsVoiceIdZero.JOE:
            return joe()

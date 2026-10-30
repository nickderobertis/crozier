

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEqStatResponseEqStat(enum.StrEnum):
    ON = "On"
    OFF = "Off"

    def visit(self, on: typing.Callable[[], T_Result], off: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEqStatResponseEqStat.ON:
            return on()
        if self is GetEqStatResponseEqStat.OFF:
            return off()

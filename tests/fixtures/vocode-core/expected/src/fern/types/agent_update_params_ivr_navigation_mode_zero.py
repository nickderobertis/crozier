

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentUpdateParamsIvrNavigationModeZero(enum.StrEnum):
    DEFAULT = "default"
    OFF = "off"

    def visit(self, default: typing.Callable[[], T_Result], off: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentUpdateParamsIvrNavigationModeZero.DEFAULT:
            return default()
        if self is AgentUpdateParamsIvrNavigationModeZero.OFF:
            return off()

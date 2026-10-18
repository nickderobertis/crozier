

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AgentIvrNavigationMode(enum.StrEnum):
    DEFAULT = "default"
    OFF = "off"

    def visit(self, default: typing.Callable[[], T_Result], off: typing.Callable[[], T_Result]) -> T_Result:
        if self is AgentIvrNavigationMode.DEFAULT:
            return default()
        if self is AgentIvrNavigationMode.OFF:
            return off()

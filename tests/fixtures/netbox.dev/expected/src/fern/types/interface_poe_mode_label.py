

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InterfacePoeModeLabel(enum.StrEnum):
    PD = "PD"
    PSE = "PSE"

    def visit(self, pd: typing.Callable[[], T_Result], pse: typing.Callable[[], T_Result]) -> T_Result:
        if self is InterfacePoeModeLabel.PD:
            return pd()
        if self is InterfacePoeModeLabel.PSE:
            return pse()

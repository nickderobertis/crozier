

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InterfacePoeModeValue(enum.StrEnum):
    PD = "pd"
    PSE = "pse"

    def visit(self, pd: typing.Callable[[], T_Result], pse: typing.Callable[[], T_Result]) -> T_Result:
        if self is InterfacePoeModeValue.PD:
            return pd()
        if self is InterfacePoeModeValue.PSE:
            return pse()

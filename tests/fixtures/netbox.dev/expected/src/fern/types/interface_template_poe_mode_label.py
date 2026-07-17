

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InterfaceTemplatePoeModeLabel(enum.StrEnum):
    PD = "PD"
    PSE = "PSE"

    def visit(self, pd: typing.Callable[[], T_Result], pse: typing.Callable[[], T_Result]) -> T_Result:
        if self is InterfaceTemplatePoeModeLabel.PD:
            return pd()
        if self is InterfaceTemplatePoeModeLabel.PSE:
            return pse()

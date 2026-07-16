

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterfaceTemplatePoeModeLabel(str, enum.Enum):
    PD = "PD"
    PSE = "PSE"

    def visit(self, pd: typing.Callable[[], T_Result], pse: typing.Callable[[], T_Result]) -> T_Result:
        if self is InterfaceTemplatePoeModeLabel.PD:
            return pd()
        if self is InterfaceTemplatePoeModeLabel.PSE:
            return pse()

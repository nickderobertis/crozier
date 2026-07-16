

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterfacePoeModeValue(str, enum.Enum):
    PD = "pd"
    PSE = "pse"

    def visit(self, pd: typing.Callable[[], T_Result], pse: typing.Callable[[], T_Result]) -> T_Result:
        if self is InterfacePoeModeValue.PD:
            return pd()
        if self is InterfacePoeModeValue.PSE:
            return pse()

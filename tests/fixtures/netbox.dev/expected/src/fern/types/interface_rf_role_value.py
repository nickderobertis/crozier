

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterfaceRfRoleValue(str, enum.Enum):
    AP = "ap"
    STATION = "station"

    def visit(self, ap: typing.Callable[[], T_Result], station: typing.Callable[[], T_Result]) -> T_Result:
        if self is InterfaceRfRoleValue.AP:
            return ap()
        if self is InterfaceRfRoleValue.STATION:
            return station()

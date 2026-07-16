

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InterfaceRfRoleLabel(enum.StrEnum):
    ACCESS_POINT = "Access point"
    STATION = "Station"

    def visit(self, access_point: typing.Callable[[], T_Result], station: typing.Callable[[], T_Result]) -> T_Result:
        if self is InterfaceRfRoleLabel.ACCESS_POINT:
            return access_point()
        if self is InterfaceRfRoleLabel.STATION:
            return station()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataProfile(enum.StrEnum):
    FLEET = "fleet"
    END_USER = "endUser"

    def visit(self, fleet: typing.Callable[[], T_Result], end_user: typing.Callable[[], T_Result]) -> T_Result:
        if self is DataProfile.FLEET:
            return fleet()
        if self is DataProfile.END_USER:
            return end_user()

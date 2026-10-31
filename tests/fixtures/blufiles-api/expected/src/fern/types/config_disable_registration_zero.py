

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConfigDisableRegistrationZero(enum.StrEnum):
    AFTER_FIRST_USER = "afterFirstUser"

    def visit(self, after_first_user: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConfigDisableRegistrationZero.AFTER_FIRST_USER:
            return after_first_user()

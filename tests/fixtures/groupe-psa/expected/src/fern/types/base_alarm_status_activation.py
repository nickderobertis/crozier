

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BaseAlarmStatusActivation(enum.StrEnum):
    """
    Define whether the vehicle alarm is active or not.
    """

    INACTIVE = "Inactive"
    ACTIVE = "Active"

    def visit(self, inactive: typing.Callable[[], T_Result], active: typing.Callable[[], T_Result]) -> T_Result:
        if self is BaseAlarmStatusActivation.INACTIVE:
            return inactive()
        if self is BaseAlarmStatusActivation.ACTIVE:
            return active()

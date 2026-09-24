

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdasBsm(enum.StrEnum):
    """
    Blind Spot Monitoring
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"
    DISABLED = "Disabled"
    FAULT = "Fault"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        fault: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdasBsm.ACTIVE:
            return active()
        if self is AdasBsm.INACTIVE:
            return inactive()
        if self is AdasBsm.DISABLED:
            return disabled()
        if self is AdasBsm.FAULT:
            return fault()

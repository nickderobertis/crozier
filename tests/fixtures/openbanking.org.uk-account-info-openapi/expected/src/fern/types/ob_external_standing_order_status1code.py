

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObExternalStandingOrderStatus1Code(enum.StrEnum):
    """
    Specifies the status of the standing order in code form.
    """

    ACTIVE = "Active"
    INACTIVE = "Inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObExternalStandingOrderStatus1Code.ACTIVE:
            return active()
        if self is ObExternalStandingOrderStatus1Code.INACTIVE:
            return inactive()

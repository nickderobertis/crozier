

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoyaltyProgramStatus(enum.StrEnum):
    """
    Indicates whether the program is currently active.
    """

    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"

    def visit(self, inactive: typing.Callable[[], T_Result], active: typing.Callable[[], T_Result]) -> T_Result:
        if self is LoyaltyProgramStatus.INACTIVE:
            return inactive()
        if self is LoyaltyProgramStatus.ACTIVE:
            return active()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SoftwareStatementStatus(enum.StrEnum):
    """
    Is this software statement Active/Suspended/Inactive
    """

    ACTIVE = "Active"
    SUSPENDED = "Suspended"
    INACTIVE = "Inactive"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        suspended: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SoftwareStatementStatus.ACTIVE:
            return active()
        if self is SoftwareStatementStatus.SUSPENDED:
            return suspended()
        if self is SoftwareStatementStatus.INACTIVE:
            return inactive()

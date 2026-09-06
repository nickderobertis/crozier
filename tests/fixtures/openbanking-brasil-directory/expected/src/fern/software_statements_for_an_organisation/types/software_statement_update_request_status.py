

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SoftwareStatementUpdateRequestStatus(enum.StrEnum):
    """
    Should this software statement be active or suspended?
    """

    ACTIVE = "Active"
    SUSPENDED = "Suspended"

    def visit(self, active: typing.Callable[[], T_Result], suspended: typing.Callable[[], T_Result]) -> T_Result:
        if self is SoftwareStatementUpdateRequestStatus.ACTIVE:
            return active()
        if self is SoftwareStatementUpdateRequestStatus.SUSPENDED:
            return suspended()

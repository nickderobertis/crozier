

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTotalFileUserCopyrightsRequestStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetTotalFileUserCopyrightsRequestStatus.ACTIVE:
            return active()
        if self is GetTotalFileUserCopyrightsRequestStatus.INACTIVE:
            return inactive()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionSummaryResponseStatus(enum.StrEnum):
    ACTIVE = "active"
    ARCHIVED = "archived"

    def visit(self, active: typing.Callable[[], T_Result], archived: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionSummaryResponseStatus.ACTIVE:
            return active()
        if self is SessionSummaryResponseStatus.ARCHIVED:
            return archived()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewerIssueSeverity(enum.StrEnum):
    WARNING = "warning"
    CRITICAL = "critical"

    def visit(self, warning: typing.Callable[[], T_Result], critical: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReviewerIssueSeverity.WARNING:
            return warning()
        if self is ReviewerIssueSeverity.CRITICAL:
            return critical()

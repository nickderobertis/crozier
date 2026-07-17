

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LeavePeriodStatus(enum.StrEnum):
    SCHEDULED = "SCHEDULED"
    PROCESSED = "PROCESSED"

    def visit(self, scheduled: typing.Callable[[], T_Result], processed: typing.Callable[[], T_Result]) -> T_Result:
        if self is LeavePeriodStatus.SCHEDULED:
            return scheduled()
        if self is LeavePeriodStatus.PROCESSED:
            return processed()

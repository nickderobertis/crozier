

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LeavePeriodStatus(str, enum.Enum):
    SCHEDULED = "SCHEDULED"
    PROCESSED = "PROCESSED"

    def visit(self, scheduled: typing.Callable[[], T_Result], processed: typing.Callable[[], T_Result]) -> T_Result:
        if self is LeavePeriodStatus.SCHEDULED:
            return scheduled()
        if self is LeavePeriodStatus.PROCESSED:
            return processed()

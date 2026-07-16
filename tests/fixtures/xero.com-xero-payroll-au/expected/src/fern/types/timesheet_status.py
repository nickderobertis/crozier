

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TimesheetStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    PROCESSED = "PROCESSED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    REQUESTED = "REQUESTED"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        processed: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        requested: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TimesheetStatus.DRAFT:
            return draft()
        if self is TimesheetStatus.PROCESSED:
            return processed()
        if self is TimesheetStatus.APPROVED:
            return approved()
        if self is TimesheetStatus.REJECTED:
            return rejected()
        if self is TimesheetStatus.REQUESTED:
            return requested()

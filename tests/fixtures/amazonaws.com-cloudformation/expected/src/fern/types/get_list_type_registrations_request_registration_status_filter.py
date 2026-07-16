

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetListTypeRegistrationsRequestRegistrationStatusFilter(str, enum.Enum):
    COMPLETE = "COMPLETE"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"

    def visit(
        self,
        complete: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetListTypeRegistrationsRequestRegistrationStatusFilter.COMPLETE:
            return complete()
        if self is GetListTypeRegistrationsRequestRegistrationStatusFilter.IN_PROGRESS:
            return in_progress()
        if self is GetListTypeRegistrationsRequestRegistrationStatusFilter.FAILED:
            return failed()

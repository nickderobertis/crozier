

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListTypeRegistrationsInputRegistrationStatusFilter(str, enum.Enum):
    """
    <p>The current status of the extension registration request.</p> <p>The default is <code>IN_PROGRESS</code>.</p>
    """

    COMPLETE = "COMPLETE"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"

    def visit(
        self,
        complete: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListTypeRegistrationsInputRegistrationStatusFilter.COMPLETE:
            return complete()
        if self is ListTypeRegistrationsInputRegistrationStatusFilter.IN_PROGRESS:
            return in_progress()
        if self is ListTypeRegistrationsInputRegistrationStatusFilter.FAILED:
            return failed()

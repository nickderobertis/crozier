

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RegistrationStatus(str, enum.Enum):
    COMPLETE = "COMPLETE"
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"

    def visit(
        self,
        complete: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RegistrationStatus.COMPLETE:
            return complete()
        if self is RegistrationStatus.IN_PROGRESS:
            return in_progress()
        if self is RegistrationStatus.FAILED:
            return failed()

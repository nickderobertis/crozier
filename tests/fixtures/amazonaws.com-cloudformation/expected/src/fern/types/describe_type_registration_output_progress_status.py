

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DescribeTypeRegistrationOutputProgressStatus(str, enum.Enum):
    """
    The current status of the extension registration request.
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
        if self is DescribeTypeRegistrationOutputProgressStatus.COMPLETE:
            return complete()
        if self is DescribeTypeRegistrationOutputProgressStatus.IN_PROGRESS:
            return in_progress()
        if self is DescribeTypeRegistrationOutputProgressStatus.FAILED:
            return failed()

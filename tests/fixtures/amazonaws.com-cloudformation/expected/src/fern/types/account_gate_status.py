

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AccountGateStatus(str, enum.Enum):
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"

    def visit(
        self,
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        skipped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountGateStatus.SUCCEEDED:
            return succeeded()
        if self is AccountGateStatus.FAILED:
            return failed()
        if self is AccountGateStatus.SKIPPED:
            return skipped()

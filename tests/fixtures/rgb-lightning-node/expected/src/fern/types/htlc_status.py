

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HtlcStatus(enum.StrEnum):
    PENDING = "Pending"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HtlcStatus.PENDING:
            return pending()
        if self is HtlcStatus.SUCCEEDED:
            return succeeded()
        if self is HtlcStatus.FAILED:
            return failed()

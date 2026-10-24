

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SwapStatus(enum.StrEnum):
    WAITING = "Waiting"
    PENDING = "Pending"
    SUCCEEDED = "Succeeded"
    EXPIRED = "Expired"
    FAILED = "Failed"

    def visit(
        self,
        waiting: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SwapStatus.WAITING:
            return waiting()
        if self is SwapStatus.PENDING:
            return pending()
        if self is SwapStatus.SUCCEEDED:
            return succeeded()
        if self is SwapStatus.EXPIRED:
            return expired()
        if self is SwapStatus.FAILED:
            return failed()

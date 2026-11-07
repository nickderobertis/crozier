

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DiscoveryState(enum.StrEnum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DiscoveryState.PENDING:
            return pending()
        if self is DiscoveryState.IN_PROGRESS:
            return in_progress()
        if self is DiscoveryState.COMPLETED:
            return completed()
        if self is DiscoveryState.FAILED:
            return failed()

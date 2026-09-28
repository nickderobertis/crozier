

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListLogsRequestSortBy(enum.StrEnum):
    """
    Field used to sort the result. `durationMs` and `cost` are null until a run settles; those runs sort before recorded values in ascending order and after them in descending order. Only `startedAt` can order Chat and Sim-agent job runs, so any other value is rejected when job runs are included.
    """

    STARTED_AT = "startedAt"
    DURATION_MS = "durationMs"
    COST = "cost"
    STATUS = "status"

    def visit(
        self,
        started_at: typing.Callable[[], T_Result],
        duration_ms: typing.Callable[[], T_Result],
        cost: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListLogsRequestSortBy.STARTED_AT:
            return started_at()
        if self is ListLogsRequestSortBy.DURATION_MS:
            return duration_ms()
        if self is ListLogsRequestSortBy.COST:
            return cost()
        if self is ListLogsRequestSortBy.STATUS:
            return status()

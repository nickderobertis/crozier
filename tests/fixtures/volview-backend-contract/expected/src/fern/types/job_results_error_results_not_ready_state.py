

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobResultsErrorResultsNotReadyState(enum.StrEnum):
    PENDING = "pending"
    RUNNING = "running"

    def visit(self, pending: typing.Callable[[], T_Result], running: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobResultsErrorResultsNotReadyState.PENDING:
            return pending()
        if self is JobResultsErrorResultsNotReadyState.RUNNING:
            return running()

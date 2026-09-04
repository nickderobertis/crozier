

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobResultsErrorResultsUnavailableState(enum.StrEnum):
    ERROR = "error"
    CANCELLED = "cancelled"

    def visit(self, error: typing.Callable[[], T_Result], cancelled: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobResultsErrorResultsUnavailableState.ERROR:
            return error()
        if self is JobResultsErrorResultsUnavailableState.CANCELLED:
            return cancelled()

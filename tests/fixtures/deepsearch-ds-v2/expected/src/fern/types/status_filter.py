

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatusFilter(enum.StrEnum):
    PENDING = "PENDING"
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatusFilter.PENDING:
            return pending()
        if self is StatusFilter.FAILURE:
            return failure()
        if self is StatusFilter.SUCCESS:
            return success()

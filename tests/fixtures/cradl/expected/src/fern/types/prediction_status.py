

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PredictionStatus(enum.StrEnum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PredictionStatus.PENDING:
            return pending()
        if self is PredictionStatus.SUCCEEDED:
            return succeeded()
        if self is PredictionStatus.FAILED:
            return failed()

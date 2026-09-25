

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PredictionsPredictionsItemStatus(enum.StrEnum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PredictionsPredictionsItemStatus.PENDING:
            return pending()
        if self is PredictionsPredictionsItemStatus.SUCCEEDED:
            return succeeded()
        if self is PredictionsPredictionsItemStatus.FAILED:
            return failed()

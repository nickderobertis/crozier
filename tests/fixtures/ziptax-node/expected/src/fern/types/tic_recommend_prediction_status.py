

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TicRecommendPredictionStatus(enum.StrEnum):
    """
    Prediction status
    """

    SUCCESS = "success"
    FAIL = "fail"

    def visit(self, success: typing.Callable[[], T_Result], fail: typing.Callable[[], T_Result]) -> T_Result:
        if self is TicRecommendPredictionStatus.SUCCESS:
            return success()
        if self is TicRecommendPredictionStatus.FAIL:
            return fail()



import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewUpdateReviewRequestPerformance(enum.StrEnum):
    EXCELLENT = "EXCELLENT"
    VERY_GOOD = "VERY_GOOD"
    GOOD = "GOOD"
    PLAYABLE = "PLAYABLE"
    BARELY_PLAYABLE = "BARELY_PLAYABLE"
    UNPLAYABLE = "UNPLAYABLE"

    def visit(
        self,
        excellent: typing.Callable[[], T_Result],
        very_good: typing.Callable[[], T_Result],
        good: typing.Callable[[], T_Result],
        playable: typing.Callable[[], T_Result],
        barely_playable: typing.Callable[[], T_Result],
        unplayable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewUpdateReviewRequestPerformance.EXCELLENT:
            return excellent()
        if self is ReviewUpdateReviewRequestPerformance.VERY_GOOD:
            return very_good()
        if self is ReviewUpdateReviewRequestPerformance.GOOD:
            return good()
        if self is ReviewUpdateReviewRequestPerformance.PLAYABLE:
            return playable()
        if self is ReviewUpdateReviewRequestPerformance.BARELY_PLAYABLE:
            return barely_playable()
        if self is ReviewUpdateReviewRequestPerformance.UNPLAYABLE:
            return unplayable()

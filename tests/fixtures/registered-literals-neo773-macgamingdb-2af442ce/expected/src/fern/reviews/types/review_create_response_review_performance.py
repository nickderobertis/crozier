

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewCreateResponseReviewPerformance(enum.StrEnum):
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
        if self is ReviewCreateResponseReviewPerformance.EXCELLENT:
            return excellent()
        if self is ReviewCreateResponseReviewPerformance.VERY_GOOD:
            return very_good()
        if self is ReviewCreateResponseReviewPerformance.GOOD:
            return good()
        if self is ReviewCreateResponseReviewPerformance.PLAYABLE:
            return playable()
        if self is ReviewCreateResponseReviewPerformance.BARELY_PLAYABLE:
            return barely_playable()
        if self is ReviewCreateResponseReviewPerformance.UNPLAYABLE:
            return unplayable()

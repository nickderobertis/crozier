

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GameGetByIdResponseReviewsItemPerformance(enum.StrEnum):
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
        if self is GameGetByIdResponseReviewsItemPerformance.EXCELLENT:
            return excellent()
        if self is GameGetByIdResponseReviewsItemPerformance.VERY_GOOD:
            return very_good()
        if self is GameGetByIdResponseReviewsItemPerformance.GOOD:
            return good()
        if self is GameGetByIdResponseReviewsItemPerformance.PLAYABLE:
            return playable()
        if self is GameGetByIdResponseReviewsItemPerformance.BARELY_PLAYABLE:
            return barely_playable()
        if self is GameGetByIdResponseReviewsItemPerformance.UNPLAYABLE:
            return unplayable()

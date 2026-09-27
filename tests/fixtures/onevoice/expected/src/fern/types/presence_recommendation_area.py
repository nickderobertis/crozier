

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PresenceRecommendationArea(enum.StrEnum):
    """
    The composite dimension this recommendation targets.
    """

    RATING = "rating"
    SLA = "sla"
    COVERAGE = "coverage"
    SYNC = "sync"

    def visit(
        self,
        rating: typing.Callable[[], T_Result],
        sla: typing.Callable[[], T_Result],
        coverage: typing.Callable[[], T_Result],
        sync: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PresenceRecommendationArea.RATING:
            return rating()
        if self is PresenceRecommendationArea.SLA:
            return sla()
        if self is PresenceRecommendationArea.COVERAGE:
            return coverage()
        if self is PresenceRecommendationArea.SYNC:
            return sync()

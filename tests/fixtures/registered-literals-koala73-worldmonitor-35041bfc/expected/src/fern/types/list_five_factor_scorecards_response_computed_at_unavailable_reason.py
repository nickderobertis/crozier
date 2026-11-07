

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListFiveFactorScorecardsResponseComputedAtUnavailableReason(enum.StrEnum):
    SCORECARD_SNAPSHOT_UNAVAILABLE = "scorecard-snapshot-unavailable"

    def visit(self, scorecard_snapshot_unavailable: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListFiveFactorScorecardsResponseComputedAtUnavailableReason.SCORECARD_SNAPSHOT_UNAVAILABLE:
            return scorecard_snapshot_unavailable()

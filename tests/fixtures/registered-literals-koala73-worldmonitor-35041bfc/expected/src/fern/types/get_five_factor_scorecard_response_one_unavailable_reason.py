

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetFiveFactorScorecardResponseOneUnavailableReason(enum.StrEnum):
    COUNTRY_UNAVAILABLE = "country-unavailable"
    SCORECARD_SNAPSHOT_UNAVAILABLE = "scorecard-snapshot-unavailable"

    def visit(
        self,
        country_unavailable: typing.Callable[[], T_Result],
        scorecard_snapshot_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFiveFactorScorecardResponseOneUnavailableReason.COUNTRY_UNAVAILABLE:
            return country_unavailable()
        if self is GetFiveFactorScorecardResponseOneUnavailableReason.SCORECARD_SNAPSHOT_UNAVAILABLE:
            return scorecard_snapshot_unavailable()

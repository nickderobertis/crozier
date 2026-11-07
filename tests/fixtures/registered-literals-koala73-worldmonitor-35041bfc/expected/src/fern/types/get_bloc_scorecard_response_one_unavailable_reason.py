

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetBlocScorecardResponseOneUnavailableReason(enum.StrEnum):
    BLOC_MEMBERS_UNAVAILABLE = "bloc-members-unavailable"
    SCORECARD_SNAPSHOT_UNAVAILABLE = "scorecard-snapshot-unavailable"

    def visit(
        self,
        bloc_members_unavailable: typing.Callable[[], T_Result],
        scorecard_snapshot_unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetBlocScorecardResponseOneUnavailableReason.BLOC_MEMBERS_UNAVAILABLE:
            return bloc_members_unavailable()
        if self is GetBlocScorecardResponseOneUnavailableReason.SCORECARD_SNAPSHOT_UNAVAILABLE:
            return scorecard_snapshot_unavailable()

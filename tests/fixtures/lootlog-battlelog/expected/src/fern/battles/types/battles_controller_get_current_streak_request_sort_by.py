

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BattlesControllerGetCurrentStreakRequestSortBy(enum.StrEnum):
    WINS = "wins"
    LOSSES = "losses"
    TOTAL_BATTLES = "totalBattles"
    WIN_RATE = "winRate"
    LAST_BATTLE_DATE = "lastBattleDate"
    TOTAL_RATING_DELTA = "totalRatingDelta"
    AVG_RATING_DELTA = "avgRatingDelta"

    def visit(
        self,
        wins: typing.Callable[[], T_Result],
        losses: typing.Callable[[], T_Result],
        total_battles: typing.Callable[[], T_Result],
        win_rate: typing.Callable[[], T_Result],
        last_battle_date: typing.Callable[[], T_Result],
        total_rating_delta: typing.Callable[[], T_Result],
        avg_rating_delta: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BattlesControllerGetCurrentStreakRequestSortBy.WINS:
            return wins()
        if self is BattlesControllerGetCurrentStreakRequestSortBy.LOSSES:
            return losses()
        if self is BattlesControllerGetCurrentStreakRequestSortBy.TOTAL_BATTLES:
            return total_battles()
        if self is BattlesControllerGetCurrentStreakRequestSortBy.WIN_RATE:
            return win_rate()
        if self is BattlesControllerGetCurrentStreakRequestSortBy.LAST_BATTLE_DATE:
            return last_battle_date()
        if self is BattlesControllerGetCurrentStreakRequestSortBy.TOTAL_RATING_DELTA:
            return total_rating_delta()
        if self is BattlesControllerGetCurrentStreakRequestSortBy.AVG_RATING_DELTA:
            return avg_rating_delta()



import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GameGetGamesRequestPerformance(enum.StrEnum):
    ALL = "ALL"
    EXCELLENT = "EXCELLENT"
    VERY_GOOD = "VERY_GOOD"
    GOOD = "GOOD"
    PLAYABLE = "PLAYABLE"
    BARELY_PLAYABLE = "BARELY_PLAYABLE"
    UNPLAYABLE = "UNPLAYABLE"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        excellent: typing.Callable[[], T_Result],
        very_good: typing.Callable[[], T_Result],
        good: typing.Callable[[], T_Result],
        playable: typing.Callable[[], T_Result],
        barely_playable: typing.Callable[[], T_Result],
        unplayable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GameGetGamesRequestPerformance.ALL:
            return all_()
        if self is GameGetGamesRequestPerformance.EXCELLENT:
            return excellent()
        if self is GameGetGamesRequestPerformance.VERY_GOOD:
            return very_good()
        if self is GameGetGamesRequestPerformance.GOOD:
            return good()
        if self is GameGetGamesRequestPerformance.PLAYABLE:
            return playable()
        if self is GameGetGamesRequestPerformance.BARELY_PLAYABLE:
            return barely_playable()
        if self is GameGetGamesRequestPerformance.UNPLAYABLE:
            return unplayable()

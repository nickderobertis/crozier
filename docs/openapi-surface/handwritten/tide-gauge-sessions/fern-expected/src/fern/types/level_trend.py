

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LevelTrend(enum.StrEnum):
    RISING = "rising"
    FALLING = "falling"
    SLACK = "slack"

    def visit(
        self,
        rising: typing.Callable[[], T_Result],
        falling: typing.Callable[[], T_Result],
        slack: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LevelTrend.RISING:
            return rising()
        if self is LevelTrend.FALLING:
            return falling()
        if self is LevelTrend.SLACK:
            return slack()

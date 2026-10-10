

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FilterGrade(enum.StrEnum):
    SOFT = "soft"
    HARD = "hard"

    def visit(self, soft: typing.Callable[[], T_Result], hard: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilterGrade.SOFT:
            return soft()
        if self is FilterGrade.HARD:
            return hard()

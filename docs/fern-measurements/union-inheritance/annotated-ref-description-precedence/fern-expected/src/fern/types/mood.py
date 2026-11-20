

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Mood(enum.StrEnum):
    CALM = "calm"
    BRISK = "brisk"

    def visit(self, calm: typing.Callable[[], T_Result], brisk: typing.Callable[[], T_Result]) -> T_Result:
        if self is Mood.CALM:
            return calm()
        if self is Mood.BRISK:
            return brisk()

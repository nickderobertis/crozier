

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Season(enum.StrEnum):
    SPRING = "spring"
    AUTUMN = "autumn"

    def visit(self, spring: typing.Callable[[], T_Result], autumn: typing.Callable[[], T_Result]) -> T_Result:
        if self is Season.SPRING:
            return spring()
        if self is Season.AUTUMN:
            return autumn()

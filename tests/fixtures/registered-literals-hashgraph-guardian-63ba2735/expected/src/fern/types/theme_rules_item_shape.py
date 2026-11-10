

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThemeRulesItemShape(enum.StrEnum):
    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"

    def visit(
        self,
        zero: typing.Callable[[], T_Result],
        one: typing.Callable[[], T_Result],
        two: typing.Callable[[], T_Result],
        three: typing.Callable[[], T_Result],
        four: typing.Callable[[], T_Result],
        five: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThemeRulesItemShape.ZERO:
            return zero()
        if self is ThemeRulesItemShape.ONE:
            return one()
        if self is ThemeRulesItemShape.TWO:
            return two()
        if self is ThemeRulesItemShape.THREE:
            return three()
        if self is ThemeRulesItemShape.FOUR:
            return four()
        if self is ThemeRulesItemShape.FIVE:
            return five()

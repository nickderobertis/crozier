

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InputDatePayloadStartWeekOn(enum.StrEnum):
    """
    Day the week starts on in the calendar view. 0=Sunday, 1=Monday, 2=Tuesday, 3=Wednesday, 4=Thursday, 5=Friday, 6=Saturday.
    """

    ZERO = "0"
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"

    def visit(
        self,
        zero: typing.Callable[[], T_Result],
        one: typing.Callable[[], T_Result],
        two: typing.Callable[[], T_Result],
        three: typing.Callable[[], T_Result],
        four: typing.Callable[[], T_Result],
        five: typing.Callable[[], T_Result],
        six: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InputDatePayloadStartWeekOn.ZERO:
            return zero()
        if self is InputDatePayloadStartWeekOn.ONE:
            return one()
        if self is InputDatePayloadStartWeekOn.TWO:
            return two()
        if self is InputDatePayloadStartWeekOn.THREE:
            return three()
        if self is InputDatePayloadStartWeekOn.FOUR:
            return four()
        if self is InputDatePayloadStartWeekOn.FIVE:
            return five()
        if self is InputDatePayloadStartWeekOn.SIX:
            return six()

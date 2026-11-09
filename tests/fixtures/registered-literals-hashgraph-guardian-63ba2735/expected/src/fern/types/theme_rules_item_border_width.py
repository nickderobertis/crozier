

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThemeRulesItemBorderWidth(enum.StrEnum):
    ZERO_PX = "0px"
    ONE_PX = "1px"
    TWO_PX = "2px"
    THREE_PX = "3px"
    FOUR_PX = "4px"
    FIVE_PX = "5px"
    SIX_PX = "6px"
    SEVEN_PX = "7px"

    def visit(
        self,
        zero_px: typing.Callable[[], T_Result],
        one_px: typing.Callable[[], T_Result],
        two_px: typing.Callable[[], T_Result],
        three_px: typing.Callable[[], T_Result],
        four_px: typing.Callable[[], T_Result],
        five_px: typing.Callable[[], T_Result],
        six_px: typing.Callable[[], T_Result],
        seven_px: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThemeRulesItemBorderWidth.ZERO_PX:
            return zero_px()
        if self is ThemeRulesItemBorderWidth.ONE_PX:
            return one_px()
        if self is ThemeRulesItemBorderWidth.TWO_PX:
            return two_px()
        if self is ThemeRulesItemBorderWidth.THREE_PX:
            return three_px()
        if self is ThemeRulesItemBorderWidth.FOUR_PX:
            return four_px()
        if self is ThemeRulesItemBorderWidth.FIVE_PX:
            return five_px()
        if self is ThemeRulesItemBorderWidth.SIX_PX:
            return six_px()
        if self is ThemeRulesItemBorderWidth.SEVEN_PX:
            return seven_px()

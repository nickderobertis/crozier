

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BrandBugInputCorner(enum.StrEnum):
    TOP_LEFT = "top_left"
    TOP_RIGHT = "top_right"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_RIGHT = "bottom_right"

    def visit(
        self,
        top_left: typing.Callable[[], T_Result],
        top_right: typing.Callable[[], T_Result],
        bottom_left: typing.Callable[[], T_Result],
        bottom_right: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BrandBugInputCorner.TOP_LEFT:
            return top_left()
        if self is BrandBugInputCorner.TOP_RIGHT:
            return top_right()
        if self is BrandBugInputCorner.BOTTOM_LEFT:
            return bottom_left()
        if self is BrandBugInputCorner.BOTTOM_RIGHT:
            return bottom_right()

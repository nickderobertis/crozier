

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MonsterSize(enum.StrEnum):
    """
    The size of the monster ranging from Tiny to Gargantuan."
    """

    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    HUGE = "Huge"
    GARGANTUAN = "Gargantuan"

    def visit(
        self,
        tiny: typing.Callable[[], T_Result],
        small: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        large: typing.Callable[[], T_Result],
        huge: typing.Callable[[], T_Result],
        gargantuan: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonsterSize.TINY:
            return tiny()
        if self is MonsterSize.SMALL:
            return small()
        if self is MonsterSize.MEDIUM:
            return medium()
        if self is MonsterSize.LARGE:
            return large()
        if self is MonsterSize.HUGE:
            return huge()
        if self is MonsterSize.GARGANTUAN:
            return gargantuan()

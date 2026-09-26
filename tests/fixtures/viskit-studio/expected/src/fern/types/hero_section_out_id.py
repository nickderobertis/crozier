

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HeroSectionOutId(enum.StrEnum):
    H1 = "H1"
    H2 = "H2"
    H3 = "H3"
    H4 = "H4"
    H5 = "H5"

    def visit(
        self,
        h1: typing.Callable[[], T_Result],
        h2: typing.Callable[[], T_Result],
        h3: typing.Callable[[], T_Result],
        h4: typing.Callable[[], T_Result],
        h5: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HeroSectionOutId.H1:
            return h1()
        if self is HeroSectionOutId.H2:
            return h2()
        if self is HeroSectionOutId.H3:
            return h3()
        if self is HeroSectionOutId.H4:
            return h4()
        if self is HeroSectionOutId.H5:
            return h5()

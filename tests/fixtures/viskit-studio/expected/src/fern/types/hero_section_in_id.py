

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HeroSectionInId(enum.StrEnum):
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
        if self is HeroSectionInId.H1:
            return h1()
        if self is HeroSectionInId.H2:
            return h2()
        if self is HeroSectionInId.H3:
            return h3()
        if self is HeroSectionInId.H4:
            return h4()
        if self is HeroSectionInId.H5:
            return h5()

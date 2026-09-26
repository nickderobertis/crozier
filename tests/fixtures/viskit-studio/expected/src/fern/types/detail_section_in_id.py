

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailSectionInId(enum.StrEnum):
    M1 = "M1"
    M2 = "M2"
    M3 = "M3"
    M4 = "M4"
    M5 = "M5"
    M6 = "M6"
    M7 = "M7"
    M8 = "M8"
    M9 = "M9"

    def visit(
        self,
        m1: typing.Callable[[], T_Result],
        m2: typing.Callable[[], T_Result],
        m3: typing.Callable[[], T_Result],
        m4: typing.Callable[[], T_Result],
        m5: typing.Callable[[], T_Result],
        m6: typing.Callable[[], T_Result],
        m7: typing.Callable[[], T_Result],
        m8: typing.Callable[[], T_Result],
        m9: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DetailSectionInId.M1:
            return m1()
        if self is DetailSectionInId.M2:
            return m2()
        if self is DetailSectionInId.M3:
            return m3()
        if self is DetailSectionInId.M4:
            return m4()
        if self is DetailSectionInId.M5:
            return m5()
        if self is DetailSectionInId.M6:
            return m6()
        if self is DetailSectionInId.M7:
            return m7()
        if self is DetailSectionInId.M8:
            return m8()
        if self is DetailSectionInId.M9:
            return m9()

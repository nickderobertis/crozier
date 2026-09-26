

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchemeSlotSlotId(enum.StrEnum):
    H1 = "H1"
    H2 = "H2"
    H3 = "H3"
    H4 = "H4"
    H5 = "H5"
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
        h1: typing.Callable[[], T_Result],
        h2: typing.Callable[[], T_Result],
        h3: typing.Callable[[], T_Result],
        h4: typing.Callable[[], T_Result],
        h5: typing.Callable[[], T_Result],
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
        if self is SchemeSlotSlotId.H1:
            return h1()
        if self is SchemeSlotSlotId.H2:
            return h2()
        if self is SchemeSlotSlotId.H3:
            return h3()
        if self is SchemeSlotSlotId.H4:
            return h4()
        if self is SchemeSlotSlotId.H5:
            return h5()
        if self is SchemeSlotSlotId.M1:
            return m1()
        if self is SchemeSlotSlotId.M2:
            return m2()
        if self is SchemeSlotSlotId.M3:
            return m3()
        if self is SchemeSlotSlotId.M4:
            return m4()
        if self is SchemeSlotSlotId.M5:
            return m5()
        if self is SchemeSlotSlotId.M6:
            return m6()
        if self is SchemeSlotSlotId.M7:
            return m7()
        if self is SchemeSlotSlotId.M8:
            return m8()
        if self is SchemeSlotSlotId.M9:
            return m9()

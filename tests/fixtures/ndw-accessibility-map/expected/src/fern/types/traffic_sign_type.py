

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TrafficSignType(enum.StrEnum):
    """
    Traffic sign type
    """

    C1 = "C1"
    C6 = "C6"
    C7 = "C7"
    C7A = "C7a"
    C7B = "C7b"
    C8 = "C8"
    C9 = "C9"
    C10 = "C10"
    C11 = "C11"
    C12 = "C12"
    C17 = "C17"
    C18 = "C18"
    C19 = "C19"
    C20 = "C20"
    C21 = "C21"
    C22 = "C22"
    C22A = "C22a"
    C22C = "C22c"
    UNKNOWN = "unknown"

    def visit(
        self,
        c1: typing.Callable[[], T_Result],
        c6: typing.Callable[[], T_Result],
        c7: typing.Callable[[], T_Result],
        c7a: typing.Callable[[], T_Result],
        c7b: typing.Callable[[], T_Result],
        c8: typing.Callable[[], T_Result],
        c9: typing.Callable[[], T_Result],
        c10: typing.Callable[[], T_Result],
        c11: typing.Callable[[], T_Result],
        c12: typing.Callable[[], T_Result],
        c17: typing.Callable[[], T_Result],
        c18: typing.Callable[[], T_Result],
        c19: typing.Callable[[], T_Result],
        c20: typing.Callable[[], T_Result],
        c21: typing.Callable[[], T_Result],
        c22: typing.Callable[[], T_Result],
        c22a: typing.Callable[[], T_Result],
        c22c: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TrafficSignType.C1:
            return c1()
        if self is TrafficSignType.C6:
            return c6()
        if self is TrafficSignType.C7:
            return c7()
        if self is TrafficSignType.C7A:
            return c7a()
        if self is TrafficSignType.C7B:
            return c7b()
        if self is TrafficSignType.C8:
            return c8()
        if self is TrafficSignType.C9:
            return c9()
        if self is TrafficSignType.C10:
            return c10()
        if self is TrafficSignType.C11:
            return c11()
        if self is TrafficSignType.C12:
            return c12()
        if self is TrafficSignType.C17:
            return c17()
        if self is TrafficSignType.C18:
            return c18()
        if self is TrafficSignType.C19:
            return c19()
        if self is TrafficSignType.C20:
            return c20()
        if self is TrafficSignType.C21:
            return c21()
        if self is TrafficSignType.C22:
            return c22()
        if self is TrafficSignType.C22A:
            return c22a()
        if self is TrafficSignType.C22C:
            return c22c()
        if self is TrafficSignType.UNKNOWN:
            return unknown()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HighlightInfoType(enum.StrEnum):
    """
    Type of highlight
    """

    M = "M"
    MC = "MC"
    MA = "MA"
    MD = "MD"
    S = "S"
    K = "K"
    B = "B"
    C = "C"
    U = "U"
    E = "E"
    A = "A"
    I = "I"
    X = "X"
    KW = "KW"
    ANY = "any"

    def visit(
        self,
        m: typing.Callable[[], T_Result],
        mc: typing.Callable[[], T_Result],
        ma: typing.Callable[[], T_Result],
        md: typing.Callable[[], T_Result],
        s: typing.Callable[[], T_Result],
        k: typing.Callable[[], T_Result],
        b: typing.Callable[[], T_Result],
        c: typing.Callable[[], T_Result],
        u: typing.Callable[[], T_Result],
        e: typing.Callable[[], T_Result],
        a: typing.Callable[[], T_Result],
        i: typing.Callable[[], T_Result],
        x: typing.Callable[[], T_Result],
        kw: typing.Callable[[], T_Result],
        any: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HighlightInfoType.M:
            return m()
        if self is HighlightInfoType.MC:
            return mc()
        if self is HighlightInfoType.MA:
            return ma()
        if self is HighlightInfoType.MD:
            return md()
        if self is HighlightInfoType.S:
            return s()
        if self is HighlightInfoType.K:
            return k()
        if self is HighlightInfoType.B:
            return b()
        if self is HighlightInfoType.C:
            return c()
        if self is HighlightInfoType.U:
            return u()
        if self is HighlightInfoType.E:
            return e()
        if self is HighlightInfoType.A:
            return a()
        if self is HighlightInfoType.I:
            return i()
        if self is HighlightInfoType.X:
            return x()
        if self is HighlightInfoType.KW:
            return kw()
        if self is HighlightInfoType.ANY:
            return any()

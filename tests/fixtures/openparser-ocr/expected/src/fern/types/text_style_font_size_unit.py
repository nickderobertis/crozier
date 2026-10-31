

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextStyleFontSizeUnit(enum.StrEnum):
    PIXEL = "pixel"
    POINT = "point"
    INCH = "inch"
    EM = "em"
    UNKNOWN = "unknown"

    def visit(
        self,
        pixel: typing.Callable[[], T_Result],
        point: typing.Callable[[], T_Result],
        inch: typing.Callable[[], T_Result],
        em: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TextStyleFontSizeUnit.PIXEL:
            return pixel()
        if self is TextStyleFontSizeUnit.POINT:
            return point()
        if self is TextStyleFontSizeUnit.INCH:
            return inch()
        if self is TextStyleFontSizeUnit.EM:
            return em()
        if self is TextStyleFontSizeUnit.UNKNOWN:
            return unknown()

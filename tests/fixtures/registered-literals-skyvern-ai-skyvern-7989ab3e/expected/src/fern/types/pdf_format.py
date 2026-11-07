

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PdfFormat(enum.StrEnum):
    A4 = "A4"
    LETTER = "Letter"
    LEGAL = "Legal"
    TABLOID = "Tabloid"

    def visit(
        self,
        a4: typing.Callable[[], T_Result],
        letter: typing.Callable[[], T_Result],
        legal: typing.Callable[[], T_Result],
        tabloid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PdfFormat.A4:
            return a4()
        if self is PdfFormat.LETTER:
            return letter()
        if self is PdfFormat.LEGAL:
            return legal()
        if self is PdfFormat.TABLOID:
            return tabloid()

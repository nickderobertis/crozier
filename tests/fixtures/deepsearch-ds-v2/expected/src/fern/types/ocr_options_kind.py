

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OcrOptionsKind(enum.StrEnum):
    EASYOCR = "easyocr"
    TESSEROCR = "tesserocr"

    def visit(self, easyocr: typing.Callable[[], T_Result], tesserocr: typing.Callable[[], T_Result]) -> T_Result:
        if self is OcrOptionsKind.EASYOCR:
            return easyocr()
        if self is OcrOptionsKind.TESSEROCR:
            return tesserocr()

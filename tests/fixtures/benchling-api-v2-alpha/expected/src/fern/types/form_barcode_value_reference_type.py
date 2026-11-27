

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FormBarcodeValueReferenceType(enum.StrEnum):
    BARCODE_VALUE = "BARCODE_VALUE"

    def visit(self, barcode_value: typing.Callable[[], T_Result]) -> T_Result:
        if self is FormBarcodeValueReferenceType.BARCODE_VALUE:
            return barcode_value()

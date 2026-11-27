

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BarcodeScanFormInstanceProviderType(enum.StrEnum):
    BARCODE_SCAN = "BARCODE_SCAN"

    def visit(self, barcode_scan: typing.Callable[[], T_Result]) -> T_Result:
        if self is BarcodeScanFormInstanceProviderType.BARCODE_SCAN:
            return barcode_scan()

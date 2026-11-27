

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BarcodeScanFormInstanceProviderMode(enum.StrEnum):
    """
    How we differentiate between single scan mode and multiple scan mode. This will allow a user to either choose to scan and load one barcode at a time or multiple barcodes.
    """

    MULTIPLE_SCAN = "MULTIPLE_SCAN"
    SINGLE_SCAN = "SINGLE_SCAN"

    def visit(
        self, multiple_scan: typing.Callable[[], T_Result], single_scan: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BarcodeScanFormInstanceProviderMode.MULTIPLE_SCAN:
            return multiple_scan()
        if self is BarcodeScanFormInstanceProviderMode.SINGLE_SCAN:
            return single_scan()

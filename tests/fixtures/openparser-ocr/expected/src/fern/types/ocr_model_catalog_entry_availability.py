

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OcrModelCatalogEntryAvailability(enum.StrEnum):
    AVAILABLE = "available"
    DEGRADED = "degraded"
    UNAVAILABLE = "unavailable"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OcrModelCatalogEntryAvailability.AVAILABLE:
            return available()
        if self is OcrModelCatalogEntryAvailability.DEGRADED:
            return degraded()
        if self is OcrModelCatalogEntryAvailability.UNAVAILABLE:
            return unavailable()

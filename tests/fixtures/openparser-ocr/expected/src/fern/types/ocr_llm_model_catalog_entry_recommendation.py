

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OcrLlmModelCatalogEntryRecommendation(enum.StrEnum):
    SUGGESTED = "suggested"
    COMPATIBLE = "compatible"

    def visit(self, suggested: typing.Callable[[], T_Result], compatible: typing.Callable[[], T_Result]) -> T_Result:
        if self is OcrLlmModelCatalogEntryRecommendation.SUGGESTED:
            return suggested()
        if self is OcrLlmModelCatalogEntryRecommendation.COMPATIBLE:
            return compatible()

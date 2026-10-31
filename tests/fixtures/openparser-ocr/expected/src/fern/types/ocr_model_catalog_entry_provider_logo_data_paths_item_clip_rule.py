

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OcrModelCatalogEntryProviderLogoDataPathsItemClipRule(enum.StrEnum):
    EVENODD = "evenodd"
    NONZERO = "nonzero"

    def visit(self, evenodd: typing.Callable[[], T_Result], nonzero: typing.Callable[[], T_Result]) -> T_Result:
        if self is OcrModelCatalogEntryProviderLogoDataPathsItemClipRule.EVENODD:
            return evenodd()
        if self is OcrModelCatalogEntryProviderLogoDataPathsItemClipRule.NONZERO:
            return nonzero()

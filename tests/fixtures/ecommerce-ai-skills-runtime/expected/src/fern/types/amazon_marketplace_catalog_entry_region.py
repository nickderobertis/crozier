

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AmazonMarketplaceCatalogEntryRegion(enum.StrEnum):
    NA = "na"
    EU = "eu"
    FE = "fe"

    def visit(
        self, na: typing.Callable[[], T_Result], eu: typing.Callable[[], T_Result], fe: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AmazonMarketplaceCatalogEntryRegion.NA:
            return na()
        if self is AmazonMarketplaceCatalogEntryRegion.EU:
            return eu()
        if self is AmazonMarketplaceCatalogEntryRegion.FE:
            return fe()

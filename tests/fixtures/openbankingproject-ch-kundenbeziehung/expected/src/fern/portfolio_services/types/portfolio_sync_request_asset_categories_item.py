

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PortfolioSyncRequestAssetCategoriesItem(enum.StrEnum):
    EQUITIES = "equities"
    BONDS = "bonds"
    FUNDS = "funds"
    ALTERNATIVES = "alternatives"
    DERIVATIVES = "derivatives"
    CASH = "cash"

    def visit(
        self,
        equities: typing.Callable[[], T_Result],
        bonds: typing.Callable[[], T_Result],
        funds: typing.Callable[[], T_Result],
        alternatives: typing.Callable[[], T_Result],
        derivatives: typing.Callable[[], T_Result],
        cash: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PortfolioSyncRequestAssetCategoriesItem.EQUITIES:
            return equities()
        if self is PortfolioSyncRequestAssetCategoriesItem.BONDS:
            return bonds()
        if self is PortfolioSyncRequestAssetCategoriesItem.FUNDS:
            return funds()
        if self is PortfolioSyncRequestAssetCategoriesItem.ALTERNATIVES:
            return alternatives()
        if self is PortfolioSyncRequestAssetCategoriesItem.DERIVATIVES:
            return derivatives()
        if self is PortfolioSyncRequestAssetCategoriesItem.CASH:
            return cash()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportRecipeKey(enum.StrEnum):
    SALES_TRAFFIC_DAILY = "sales_traffic_daily"
    FBA_INVENTORY_DAILY = "fba_inventory_daily"
    LISTINGS_DAILY = "listings_daily"
    RETURNS_DAILY = "returns_daily"

    def visit(
        self,
        sales_traffic_daily: typing.Callable[[], T_Result],
        fba_inventory_daily: typing.Callable[[], T_Result],
        listings_daily: typing.Callable[[], T_Result],
        returns_daily: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReportRecipeKey.SALES_TRAFFIC_DAILY:
            return sales_traffic_daily()
        if self is ReportRecipeKey.FBA_INVENTORY_DAILY:
            return fba_inventory_daily()
        if self is ReportRecipeKey.LISTINGS_DAILY:
            return listings_daily()
        if self is ReportRecipeKey.RETURNS_DAILY:
            return returns_daily()

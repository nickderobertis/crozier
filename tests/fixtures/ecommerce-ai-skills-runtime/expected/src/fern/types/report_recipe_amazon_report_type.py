

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportRecipeAmazonReportType(enum.StrEnum):
    GET_SALES_AND_TRAFFIC_REPORT = "GET_SALES_AND_TRAFFIC_REPORT"
    GET_FBA_MYI_UNSUPPRESSED_INVENTORY_DATA = "GET_FBA_MYI_UNSUPPRESSED_INVENTORY_DATA"
    GET_MERCHANT_LISTINGS_ALL_DATA = "GET_MERCHANT_LISTINGS_ALL_DATA"
    GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA = "GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA"

    def visit(
        self,
        get_sales_and_traffic_report: typing.Callable[[], T_Result],
        get_fba_myi_unsuppressed_inventory_data: typing.Callable[[], T_Result],
        get_merchant_listings_all_data: typing.Callable[[], T_Result],
        get_fba_fulfillment_customer_returns_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReportRecipeAmazonReportType.GET_SALES_AND_TRAFFIC_REPORT:
            return get_sales_and_traffic_report()
        if self is ReportRecipeAmazonReportType.GET_FBA_MYI_UNSUPPRESSED_INVENTORY_DATA:
            return get_fba_myi_unsuppressed_inventory_data()
        if self is ReportRecipeAmazonReportType.GET_MERCHANT_LISTINGS_ALL_DATA:
            return get_merchant_listings_all_data()
        if self is ReportRecipeAmazonReportType.GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA:
            return get_fba_fulfillment_customer_returns_data()

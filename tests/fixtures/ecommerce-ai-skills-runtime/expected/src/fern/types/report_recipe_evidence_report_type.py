

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportRecipeEvidenceReportType(enum.StrEnum):
    AMAZON_BUSINESS_REPORT = "amazon_business_report"
    AMAZON_FBA_INVENTORY = "amazon_fba_inventory"
    AMAZON_LISTING = "amazon_listing"
    AMAZON_RETURNS = "amazon_returns"

    def visit(
        self,
        amazon_business_report: typing.Callable[[], T_Result],
        amazon_fba_inventory: typing.Callable[[], T_Result],
        amazon_listing: typing.Callable[[], T_Result],
        amazon_returns: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReportRecipeEvidenceReportType.AMAZON_BUSINESS_REPORT:
            return amazon_business_report()
        if self is ReportRecipeEvidenceReportType.AMAZON_FBA_INVENTORY:
            return amazon_fba_inventory()
        if self is ReportRecipeEvidenceReportType.AMAZON_LISTING:
            return amazon_listing()
        if self is ReportRecipeEvidenceReportType.AMAZON_RETURNS:
            return amazon_returns()

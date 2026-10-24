

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EvidenceReportType(enum.StrEnum):
    AMAZON_BUSINESS_REPORT = "amazon_business_report"
    AMAZON_ADS_SEARCH_TERM = "amazon_ads_search_term"
    AMAZON_FBA_INVENTORY = "amazon_fba_inventory"
    AMAZON_RETURNS = "amazon_returns"
    AMAZON_LISTING = "amazon_listing"
    PLATFORM_GENERIC = "platform_generic"

    def visit(
        self,
        amazon_business_report: typing.Callable[[], T_Result],
        amazon_ads_search_term: typing.Callable[[], T_Result],
        amazon_fba_inventory: typing.Callable[[], T_Result],
        amazon_returns: typing.Callable[[], T_Result],
        amazon_listing: typing.Callable[[], T_Result],
        platform_generic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EvidenceReportType.AMAZON_BUSINESS_REPORT:
            return amazon_business_report()
        if self is EvidenceReportType.AMAZON_ADS_SEARCH_TERM:
            return amazon_ads_search_term()
        if self is EvidenceReportType.AMAZON_FBA_INVENTORY:
            return amazon_fba_inventory()
        if self is EvidenceReportType.AMAZON_RETURNS:
            return amazon_returns()
        if self is EvidenceReportType.AMAZON_LISTING:
            return amazon_listing()
        if self is EvidenceReportType.PLATFORM_GENERIC:
            return platform_generic()

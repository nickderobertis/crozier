



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account_categories_updated_webhook import AccountCategoriesUpdatedWebhook
    from .account_categories_updated_webhook_data import AccountCategoriesUpdatedWebhookData
    from .account_category import AccountCategory
    from .categories import Categories
    from .categories_item import CategoriesItem
    from .categorised_account import CategorisedAccount
    from .categorised_accounts import CategorisedAccounts
    from .currency import Currency
    from .currency_rate import CurrencyRate
    from .data_integrity_details import DataIntegrityDetails
    from .data_integrity_status import DataIntegrityStatus
    from .data_integrity_summary import DataIntegritySummary
    from .details import Details
    from .enhanced_cash_flow_transactions import EnhancedCashFlowTransactions
    from .enhanced_invoices_report import EnhancedInvoicesReport
    from .enhanced_invoices_report_report_items_item import EnhancedInvoicesReportReportItemsItem
    from .enhanced_report import EnhancedReport
    from .enhanced_report_report_items_item import EnhancedReportReportItemsItem
    from .excel_status import ExcelStatus
    from .financial_metrics import FinancialMetrics
    from .financial_metrics_period_unit import FinancialMetricsPeriodUnit
    from .hal_ref import HalRef
    from .links import Links
    from .paging_info import PagingInfo
    from .report import Report
    from .status import Status
    from .summaries import Summaries
_dynamic_imports: typing.Dict[str, str] = {
    "AccountCategoriesUpdatedWebhook": ".account_categories_updated_webhook",
    "AccountCategoriesUpdatedWebhookData": ".account_categories_updated_webhook_data",
    "AccountCategory": ".account_category",
    "Categories": ".categories",
    "CategoriesItem": ".categories_item",
    "CategorisedAccount": ".categorised_account",
    "CategorisedAccounts": ".categorised_accounts",
    "Currency": ".currency",
    "CurrencyRate": ".currency_rate",
    "DataIntegrityDetails": ".data_integrity_details",
    "DataIntegrityStatus": ".data_integrity_status",
    "DataIntegritySummary": ".data_integrity_summary",
    "Details": ".details",
    "EnhancedCashFlowTransactions": ".enhanced_cash_flow_transactions",
    "EnhancedInvoicesReport": ".enhanced_invoices_report",
    "EnhancedInvoicesReportReportItemsItem": ".enhanced_invoices_report_report_items_item",
    "EnhancedReport": ".enhanced_report",
    "EnhancedReportReportItemsItem": ".enhanced_report_report_items_item",
    "ExcelStatus": ".excel_status",
    "FinancialMetrics": ".financial_metrics",
    "FinancialMetricsPeriodUnit": ".financial_metrics_period_unit",
    "HalRef": ".hal_ref",
    "Links": ".links",
    "PagingInfo": ".paging_info",
    "Report": ".report",
    "Status": ".status",
    "Summaries": ".summaries",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AccountCategoriesUpdatedWebhook",
    "AccountCategoriesUpdatedWebhookData",
    "AccountCategory",
    "Categories",
    "CategoriesItem",
    "CategorisedAccount",
    "CategorisedAccounts",
    "Currency",
    "CurrencyRate",
    "DataIntegrityDetails",
    "DataIntegrityStatus",
    "DataIntegritySummary",
    "Details",
    "EnhancedCashFlowTransactions",
    "EnhancedInvoicesReport",
    "EnhancedInvoicesReportReportItemsItem",
    "EnhancedReport",
    "EnhancedReportReportItemsItem",
    "ExcelStatus",
    "FinancialMetrics",
    "FinancialMetricsPeriodUnit",
    "HalRef",
    "Links",
    "PagingInfo",
    "Report",
    "Status",
    "Summaries",
]

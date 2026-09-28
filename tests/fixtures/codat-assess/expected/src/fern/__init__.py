



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AccountCategoriesUpdatedWebhook,
        AccountCategoriesUpdatedWebhookData,
        AccountCategory,
        Categories,
        CategoriesItem,
        CategorisedAccount,
        CategorisedAccounts,
        Currency,
        CurrencyRate,
        DataIntegrityDetails,
        DataIntegrityStatus,
        DataIntegritySummary,
        Details,
        EnhancedCashFlowTransactions,
        EnhancedInvoicesReport,
        EnhancedInvoicesReportReportItemsItem,
        EnhancedReport,
        EnhancedReportReportItemsItem,
        ExcelStatus,
        FinancialMetrics,
        FinancialMetricsPeriodUnit,
        HalRef,
        Links,
        PagingInfo,
        Report,
        Status,
        Summaries,
    )
    from . import categories, data_integrity, excel_reports, reports
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .categories import ConfirmCategoriesCategoriesItem, ConfirmCategoriesCategoriesItemAccountRef
    from .client import AsyncFernApi, FernApi
    from .data_integrity import (
        GetDataIntegrityDetailsRequestDataType,
        GetDataIntegrityStatusRequestDataType,
        GetDataIntegritySummariesRequestDataType,
    )
    from .environment import FernApiEnvironment
    from .excel_reports import (
        DownloadExcelReportRequestReportType,
        GenerateExcelReportRequestReportType,
        GetAccountingMarketingMetricsRequestPeriodUnit,
        GetExcelReportGenerationStatusRequestReportType,
        GetExcelReportRequestReportType,
    )
    from .reports import (
        GetCommerceCustomerRetentionMetricsRequestPeriodUnit,
        GetCommerceLifetimeValueMetricsRequestPeriodUnit,
        GetCommerceOrdersMetricsRequestPeriodUnit,
        GetCommerceRefundsMetricsRequestPeriodUnit,
        GetCommerceRevenueMetricsRequestPeriodUnit,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AccountCategoriesUpdatedWebhook": ".types",
    "AccountCategoriesUpdatedWebhookData": ".types",
    "AccountCategory": ".types",
    "AsyncFernApi": ".client",
    "Categories": ".types",
    "CategoriesItem": ".types",
    "CategorisedAccount": ".types",
    "CategorisedAccounts": ".types",
    "ConfirmCategoriesCategoriesItem": ".categories",
    "ConfirmCategoriesCategoriesItemAccountRef": ".categories",
    "Currency": ".types",
    "CurrencyRate": ".types",
    "DataIntegrityDetails": ".types",
    "DataIntegrityStatus": ".types",
    "DataIntegritySummary": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Details": ".types",
    "DownloadExcelReportRequestReportType": ".excel_reports",
    "EnhancedCashFlowTransactions": ".types",
    "EnhancedInvoicesReport": ".types",
    "EnhancedInvoicesReportReportItemsItem": ".types",
    "EnhancedReport": ".types",
    "EnhancedReportReportItemsItem": ".types",
    "ExcelStatus": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FinancialMetrics": ".types",
    "FinancialMetricsPeriodUnit": ".types",
    "GenerateExcelReportRequestReportType": ".excel_reports",
    "GetAccountingMarketingMetricsRequestPeriodUnit": ".excel_reports",
    "GetCommerceCustomerRetentionMetricsRequestPeriodUnit": ".reports",
    "GetCommerceLifetimeValueMetricsRequestPeriodUnit": ".reports",
    "GetCommerceOrdersMetricsRequestPeriodUnit": ".reports",
    "GetCommerceRefundsMetricsRequestPeriodUnit": ".reports",
    "GetCommerceRevenueMetricsRequestPeriodUnit": ".reports",
    "GetDataIntegrityDetailsRequestDataType": ".data_integrity",
    "GetDataIntegrityStatusRequestDataType": ".data_integrity",
    "GetDataIntegritySummariesRequestDataType": ".data_integrity",
    "GetExcelReportGenerationStatusRequestReportType": ".excel_reports",
    "GetExcelReportRequestReportType": ".excel_reports",
    "HalRef": ".types",
    "Links": ".types",
    "PagingInfo": ".types",
    "Report": ".types",
    "Status": ".types",
    "Summaries": ".types",
    "__version__": ".version",
    "categories": ".categories",
    "data_integrity": ".data_integrity",
    "excel_reports": ".excel_reports",
    "reports": ".reports",
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
    "AsyncFernApi",
    "Categories",
    "CategoriesItem",
    "CategorisedAccount",
    "CategorisedAccounts",
    "ConfirmCategoriesCategoriesItem",
    "ConfirmCategoriesCategoriesItemAccountRef",
    "Currency",
    "CurrencyRate",
    "DataIntegrityDetails",
    "DataIntegrityStatus",
    "DataIntegritySummary",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Details",
    "DownloadExcelReportRequestReportType",
    "EnhancedCashFlowTransactions",
    "EnhancedInvoicesReport",
    "EnhancedInvoicesReportReportItemsItem",
    "EnhancedReport",
    "EnhancedReportReportItemsItem",
    "ExcelStatus",
    "FernApi",
    "FernApiEnvironment",
    "FinancialMetrics",
    "FinancialMetricsPeriodUnit",
    "GenerateExcelReportRequestReportType",
    "GetAccountingMarketingMetricsRequestPeriodUnit",
    "GetCommerceCustomerRetentionMetricsRequestPeriodUnit",
    "GetCommerceLifetimeValueMetricsRequestPeriodUnit",
    "GetCommerceOrdersMetricsRequestPeriodUnit",
    "GetCommerceRefundsMetricsRequestPeriodUnit",
    "GetCommerceRevenueMetricsRequestPeriodUnit",
    "GetDataIntegrityDetailsRequestDataType",
    "GetDataIntegrityStatusRequestDataType",
    "GetDataIntegritySummariesRequestDataType",
    "GetExcelReportGenerationStatusRequestReportType",
    "GetExcelReportRequestReportType",
    "HalRef",
    "Links",
    "PagingInfo",
    "Report",
    "Status",
    "Summaries",
    "__version__",
    "categories",
    "data_integrity",
    "excel_reports",
    "reports",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .download_excel_report_request_report_type import DownloadExcelReportRequestReportType
    from .generate_excel_report_request_report_type import GenerateExcelReportRequestReportType
    from .get_accounting_marketing_metrics_request_period_unit import GetAccountingMarketingMetricsRequestPeriodUnit
    from .get_excel_report_generation_status_request_report_type import GetExcelReportGenerationStatusRequestReportType
    from .get_excel_report_request_report_type import GetExcelReportRequestReportType
_dynamic_imports: typing.Dict[str, str] = {
    "DownloadExcelReportRequestReportType": ".download_excel_report_request_report_type",
    "GenerateExcelReportRequestReportType": ".generate_excel_report_request_report_type",
    "GetAccountingMarketingMetricsRequestPeriodUnit": ".get_accounting_marketing_metrics_request_period_unit",
    "GetExcelReportGenerationStatusRequestReportType": ".get_excel_report_generation_status_request_report_type",
    "GetExcelReportRequestReportType": ".get_excel_report_request_report_type",
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
    "DownloadExcelReportRequestReportType",
    "GenerateExcelReportRequestReportType",
    "GetAccountingMarketingMetricsRequestPeriodUnit",
    "GetExcelReportGenerationStatusRequestReportType",
    "GetExcelReportRequestReportType",
]

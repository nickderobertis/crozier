



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .base_report_generation_config_api_model_cloud_type import BaseReportGenerationConfigApiModelCloudType
    from .base_report_generation_config_api_model_counts import BaseReportGenerationConfigApiModelCounts
    from .base_report_generation_config_api_model_target import BaseReportGenerationConfigApiModelTarget
    from .base_report_generation_config_api_model_type import BaseReportGenerationConfigApiModelType
    from .list_reports_request_report_frequency import ListReportsRequestReportFrequency
    from .list_reports_request_report_schedule import ListReportsRequestReportSchedule
    from .list_reports_request_report_view import ListReportsRequestReportView
_dynamic_imports: typing.Dict[str, str] = {
    "BaseReportGenerationConfigApiModelCloudType": ".base_report_generation_config_api_model_cloud_type",
    "BaseReportGenerationConfigApiModelCounts": ".base_report_generation_config_api_model_counts",
    "BaseReportGenerationConfigApiModelTarget": ".base_report_generation_config_api_model_target",
    "BaseReportGenerationConfigApiModelType": ".base_report_generation_config_api_model_type",
    "ListReportsRequestReportFrequency": ".list_reports_request_report_frequency",
    "ListReportsRequestReportSchedule": ".list_reports_request_report_schedule",
    "ListReportsRequestReportView": ".list_reports_request_report_view",
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
    "BaseReportGenerationConfigApiModelCloudType",
    "BaseReportGenerationConfigApiModelCounts",
    "BaseReportGenerationConfigApiModelTarget",
    "BaseReportGenerationConfigApiModelType",
    "ListReportsRequestReportFrequency",
    "ListReportsRequestReportSchedule",
    "ListReportsRequestReportView",
]

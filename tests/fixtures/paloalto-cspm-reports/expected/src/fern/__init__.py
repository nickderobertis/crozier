



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AbsoluteTimeRangeConfigModel,
        AbsoluteTimeRangeConfigModelValue,
        BaseReportTargetModel,
        ComplianceAggregateCount,
        FilterSuggestion,
        NameValueIntegerString,
        ParsedTableFilter,
        RelativeTimeDurationModel,
        RelativeTimeDurationModelUnit,
        RelativeTimeRangeConfigModel,
        RelativeTimeRangeConfigModelRelativeTimeType,
        RelativeTimeRangeConfigModelValue,
        RelativeTimeRangeConfigModelValueUnit,
        ReportFilterSuggestion,
        ReportFilterSuggestionAccountGroup,
        ReportFilterSuggestionCloudAccount,
        ReportFilterSuggestionCloudRegion,
        ReportFilterSuggestionCloudType,
        ReportFilterSuggestionPolicyComplianceStandard,
        ReportFilterSuggestionReportEmailRecipients,
        ReportFilterSuggestionReportFrequency,
        ReportFilterSuggestionReportSchedule,
        ReportFilterSuggestionScheduleStatus,
        ReportGenerationConfigApiModel,
        ReportGenerationConfigApiModelCloudType,
        ReportGenerationConfigApiModelCounts,
        ReportGenerationConfigApiModelTarget,
        ReportGenerationConfigApiModelTargetTimeRange,
        ReportGenerationConfigApiModelTargetTimeRange_Absolute,
        ReportGenerationConfigApiModelTargetTimeRange_Relative,
        ReportGenerationConfigApiModelTargetTimeRange_ToNow,
        ReportGenerationConfigApiModelType,
        ReportTargetModel,
        ReportTargetModelTimeRange,
        ReportTargetModelTimeRange_Absolute,
        ReportTargetModelTimeRange_Relative,
        ReportTargetModelTimeRange_ToNow,
        TimeModel,
        TimeRangeConfigModel,
        TimeRangeConfigModel_Absolute,
        TimeRangeConfigModel_Relative,
        TimeRangeConfigModel_ToNow,
        ToNowTimeRangeConfigModel,
        ToNowTimeRangeConfigModelValue,
        UiFilterModel,
        UiFilterModelOperator,
    )
    from .errors import BadRequestError, MethodNotAllowedError, NotFoundError
    from . import reports
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .reports import (
        BaseReportGenerationConfigApiModelCloudType,
        BaseReportGenerationConfigApiModelCounts,
        BaseReportGenerationConfigApiModelTarget,
        BaseReportGenerationConfigApiModelType,
        ListReportsRequestReportFrequency,
        ListReportsRequestReportSchedule,
        ListReportsRequestReportView,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AbsoluteTimeRangeConfigModel": ".types",
    "AbsoluteTimeRangeConfigModelValue": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BaseReportGenerationConfigApiModelCloudType": ".reports",
    "BaseReportGenerationConfigApiModelCounts": ".reports",
    "BaseReportGenerationConfigApiModelTarget": ".reports",
    "BaseReportGenerationConfigApiModelType": ".reports",
    "BaseReportTargetModel": ".types",
    "ComplianceAggregateCount": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FilterSuggestion": ".types",
    "ListReportsRequestReportFrequency": ".reports",
    "ListReportsRequestReportSchedule": ".reports",
    "ListReportsRequestReportView": ".reports",
    "MethodNotAllowedError": ".errors",
    "NameValueIntegerString": ".types",
    "NotFoundError": ".errors",
    "ParsedTableFilter": ".types",
    "RelativeTimeDurationModel": ".types",
    "RelativeTimeDurationModelUnit": ".types",
    "RelativeTimeRangeConfigModel": ".types",
    "RelativeTimeRangeConfigModelRelativeTimeType": ".types",
    "RelativeTimeRangeConfigModelValue": ".types",
    "RelativeTimeRangeConfigModelValueUnit": ".types",
    "ReportFilterSuggestion": ".types",
    "ReportFilterSuggestionAccountGroup": ".types",
    "ReportFilterSuggestionCloudAccount": ".types",
    "ReportFilterSuggestionCloudRegion": ".types",
    "ReportFilterSuggestionCloudType": ".types",
    "ReportFilterSuggestionPolicyComplianceStandard": ".types",
    "ReportFilterSuggestionReportEmailRecipients": ".types",
    "ReportFilterSuggestionReportFrequency": ".types",
    "ReportFilterSuggestionReportSchedule": ".types",
    "ReportFilterSuggestionScheduleStatus": ".types",
    "ReportGenerationConfigApiModel": ".types",
    "ReportGenerationConfigApiModelCloudType": ".types",
    "ReportGenerationConfigApiModelCounts": ".types",
    "ReportGenerationConfigApiModelTarget": ".types",
    "ReportGenerationConfigApiModelTargetTimeRange": ".types",
    "ReportGenerationConfigApiModelTargetTimeRange_Absolute": ".types",
    "ReportGenerationConfigApiModelTargetTimeRange_Relative": ".types",
    "ReportGenerationConfigApiModelTargetTimeRange_ToNow": ".types",
    "ReportGenerationConfigApiModelType": ".types",
    "ReportTargetModel": ".types",
    "ReportTargetModelTimeRange": ".types",
    "ReportTargetModelTimeRange_Absolute": ".types",
    "ReportTargetModelTimeRange_Relative": ".types",
    "ReportTargetModelTimeRange_ToNow": ".types",
    "TimeModel": ".types",
    "TimeRangeConfigModel": ".types",
    "TimeRangeConfigModel_Absolute": ".types",
    "TimeRangeConfigModel_Relative": ".types",
    "TimeRangeConfigModel_ToNow": ".types",
    "ToNowTimeRangeConfigModel": ".types",
    "ToNowTimeRangeConfigModelValue": ".types",
    "UiFilterModel": ".types",
    "UiFilterModelOperator": ".types",
    "__version__": ".version",
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
    "AbsoluteTimeRangeConfigModel",
    "AbsoluteTimeRangeConfigModelValue",
    "AsyncFernApi",
    "BadRequestError",
    "BaseReportGenerationConfigApiModelCloudType",
    "BaseReportGenerationConfigApiModelCounts",
    "BaseReportGenerationConfigApiModelTarget",
    "BaseReportGenerationConfigApiModelType",
    "BaseReportTargetModel",
    "ComplianceAggregateCount",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "FilterSuggestion",
    "ListReportsRequestReportFrequency",
    "ListReportsRequestReportSchedule",
    "ListReportsRequestReportView",
    "MethodNotAllowedError",
    "NameValueIntegerString",
    "NotFoundError",
    "ParsedTableFilter",
    "RelativeTimeDurationModel",
    "RelativeTimeDurationModelUnit",
    "RelativeTimeRangeConfigModel",
    "RelativeTimeRangeConfigModelRelativeTimeType",
    "RelativeTimeRangeConfigModelValue",
    "RelativeTimeRangeConfigModelValueUnit",
    "ReportFilterSuggestion",
    "ReportFilterSuggestionAccountGroup",
    "ReportFilterSuggestionCloudAccount",
    "ReportFilterSuggestionCloudRegion",
    "ReportFilterSuggestionCloudType",
    "ReportFilterSuggestionPolicyComplianceStandard",
    "ReportFilterSuggestionReportEmailRecipients",
    "ReportFilterSuggestionReportFrequency",
    "ReportFilterSuggestionReportSchedule",
    "ReportFilterSuggestionScheduleStatus",
    "ReportGenerationConfigApiModel",
    "ReportGenerationConfigApiModelCloudType",
    "ReportGenerationConfigApiModelCounts",
    "ReportGenerationConfigApiModelTarget",
    "ReportGenerationConfigApiModelTargetTimeRange",
    "ReportGenerationConfigApiModelTargetTimeRange_Absolute",
    "ReportGenerationConfigApiModelTargetTimeRange_Relative",
    "ReportGenerationConfigApiModelTargetTimeRange_ToNow",
    "ReportGenerationConfigApiModelType",
    "ReportTargetModel",
    "ReportTargetModelTimeRange",
    "ReportTargetModelTimeRange_Absolute",
    "ReportTargetModelTimeRange_Relative",
    "ReportTargetModelTimeRange_ToNow",
    "TimeModel",
    "TimeRangeConfigModel",
    "TimeRangeConfigModel_Absolute",
    "TimeRangeConfigModel_Relative",
    "TimeRangeConfigModel_ToNow",
    "ToNowTimeRangeConfigModel",
    "ToNowTimeRangeConfigModelValue",
    "UiFilterModel",
    "UiFilterModelOperator",
    "__version__",
    "reports",
]

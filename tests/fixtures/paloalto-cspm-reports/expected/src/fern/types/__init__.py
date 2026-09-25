



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .absolute_time_range_config_model import AbsoluteTimeRangeConfigModel
    from .absolute_time_range_config_model_value import AbsoluteTimeRangeConfigModelValue
    from .base_report_target_model import BaseReportTargetModel
    from .compliance_aggregate_count import ComplianceAggregateCount
    from .filter_suggestion import FilterSuggestion
    from .name_value_integer_string import NameValueIntegerString
    from .parsed_table_filter import ParsedTableFilter
    from .relative_time_duration_model import RelativeTimeDurationModel
    from .relative_time_duration_model_unit import RelativeTimeDurationModelUnit
    from .relative_time_range_config_model import RelativeTimeRangeConfigModel
    from .relative_time_range_config_model_relative_time_type import RelativeTimeRangeConfigModelRelativeTimeType
    from .relative_time_range_config_model_value import RelativeTimeRangeConfigModelValue
    from .relative_time_range_config_model_value_unit import RelativeTimeRangeConfigModelValueUnit
    from .report_filter_suggestion import ReportFilterSuggestion
    from .report_filter_suggestion_account_group import ReportFilterSuggestionAccountGroup
    from .report_filter_suggestion_cloud_account import ReportFilterSuggestionCloudAccount
    from .report_filter_suggestion_cloud_region import ReportFilterSuggestionCloudRegion
    from .report_filter_suggestion_cloud_type import ReportFilterSuggestionCloudType
    from .report_filter_suggestion_policy_compliance_standard import ReportFilterSuggestionPolicyComplianceStandard
    from .report_filter_suggestion_report_email_recipients import ReportFilterSuggestionReportEmailRecipients
    from .report_filter_suggestion_report_frequency import ReportFilterSuggestionReportFrequency
    from .report_filter_suggestion_report_schedule import ReportFilterSuggestionReportSchedule
    from .report_filter_suggestion_schedule_status import ReportFilterSuggestionScheduleStatus
    from .report_generation_config_api_model import ReportGenerationConfigApiModel
    from .report_generation_config_api_model_cloud_type import ReportGenerationConfigApiModelCloudType
    from .report_generation_config_api_model_counts import ReportGenerationConfigApiModelCounts
    from .report_generation_config_api_model_target import ReportGenerationConfigApiModelTarget
    from .report_generation_config_api_model_target_time_range import (
        ReportGenerationConfigApiModelTargetTimeRange,
        ReportGenerationConfigApiModelTargetTimeRange_Absolute,
        ReportGenerationConfigApiModelTargetTimeRange_Relative,
        ReportGenerationConfigApiModelTargetTimeRange_ToNow,
    )
    from .report_generation_config_api_model_type import ReportGenerationConfigApiModelType
    from .report_target_model import ReportTargetModel
    from .report_target_model_time_range import (
        ReportTargetModelTimeRange,
        ReportTargetModelTimeRange_Absolute,
        ReportTargetModelTimeRange_Relative,
        ReportTargetModelTimeRange_ToNow,
    )
    from .time_model import TimeModel
    from .time_range_config_model import (
        TimeRangeConfigModel,
        TimeRangeConfigModel_Absolute,
        TimeRangeConfigModel_Relative,
        TimeRangeConfigModel_ToNow,
    )
    from .to_now_time_range_config_model import ToNowTimeRangeConfigModel
    from .to_now_time_range_config_model_value import ToNowTimeRangeConfigModelValue
    from .ui_filter_model import UiFilterModel
    from .ui_filter_model_operator import UiFilterModelOperator
_dynamic_imports: typing.Dict[str, str] = {
    "AbsoluteTimeRangeConfigModel": ".absolute_time_range_config_model",
    "AbsoluteTimeRangeConfigModelValue": ".absolute_time_range_config_model_value",
    "BaseReportTargetModel": ".base_report_target_model",
    "ComplianceAggregateCount": ".compliance_aggregate_count",
    "FilterSuggestion": ".filter_suggestion",
    "NameValueIntegerString": ".name_value_integer_string",
    "ParsedTableFilter": ".parsed_table_filter",
    "RelativeTimeDurationModel": ".relative_time_duration_model",
    "RelativeTimeDurationModelUnit": ".relative_time_duration_model_unit",
    "RelativeTimeRangeConfigModel": ".relative_time_range_config_model",
    "RelativeTimeRangeConfigModelRelativeTimeType": ".relative_time_range_config_model_relative_time_type",
    "RelativeTimeRangeConfigModelValue": ".relative_time_range_config_model_value",
    "RelativeTimeRangeConfigModelValueUnit": ".relative_time_range_config_model_value_unit",
    "ReportFilterSuggestion": ".report_filter_suggestion",
    "ReportFilterSuggestionAccountGroup": ".report_filter_suggestion_account_group",
    "ReportFilterSuggestionCloudAccount": ".report_filter_suggestion_cloud_account",
    "ReportFilterSuggestionCloudRegion": ".report_filter_suggestion_cloud_region",
    "ReportFilterSuggestionCloudType": ".report_filter_suggestion_cloud_type",
    "ReportFilterSuggestionPolicyComplianceStandard": ".report_filter_suggestion_policy_compliance_standard",
    "ReportFilterSuggestionReportEmailRecipients": ".report_filter_suggestion_report_email_recipients",
    "ReportFilterSuggestionReportFrequency": ".report_filter_suggestion_report_frequency",
    "ReportFilterSuggestionReportSchedule": ".report_filter_suggestion_report_schedule",
    "ReportFilterSuggestionScheduleStatus": ".report_filter_suggestion_schedule_status",
    "ReportGenerationConfigApiModel": ".report_generation_config_api_model",
    "ReportGenerationConfigApiModelCloudType": ".report_generation_config_api_model_cloud_type",
    "ReportGenerationConfigApiModelCounts": ".report_generation_config_api_model_counts",
    "ReportGenerationConfigApiModelTarget": ".report_generation_config_api_model_target",
    "ReportGenerationConfigApiModelTargetTimeRange": ".report_generation_config_api_model_target_time_range",
    "ReportGenerationConfigApiModelTargetTimeRange_Absolute": ".report_generation_config_api_model_target_time_range",
    "ReportGenerationConfigApiModelTargetTimeRange_Relative": ".report_generation_config_api_model_target_time_range",
    "ReportGenerationConfigApiModelTargetTimeRange_ToNow": ".report_generation_config_api_model_target_time_range",
    "ReportGenerationConfigApiModelType": ".report_generation_config_api_model_type",
    "ReportTargetModel": ".report_target_model",
    "ReportTargetModelTimeRange": ".report_target_model_time_range",
    "ReportTargetModelTimeRange_Absolute": ".report_target_model_time_range",
    "ReportTargetModelTimeRange_Relative": ".report_target_model_time_range",
    "ReportTargetModelTimeRange_ToNow": ".report_target_model_time_range",
    "TimeModel": ".time_model",
    "TimeRangeConfigModel": ".time_range_config_model",
    "TimeRangeConfigModel_Absolute": ".time_range_config_model",
    "TimeRangeConfigModel_Relative": ".time_range_config_model",
    "TimeRangeConfigModel_ToNow": ".time_range_config_model",
    "ToNowTimeRangeConfigModel": ".to_now_time_range_config_model",
    "ToNowTimeRangeConfigModelValue": ".to_now_time_range_config_model_value",
    "UiFilterModel": ".ui_filter_model",
    "UiFilterModelOperator": ".ui_filter_model_operator",
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
    "BaseReportTargetModel",
    "ComplianceAggregateCount",
    "FilterSuggestion",
    "NameValueIntegerString",
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
]

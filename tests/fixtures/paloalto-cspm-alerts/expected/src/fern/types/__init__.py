



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .absolute_time_range_config_model import AbsoluteTimeRangeConfigModel
    from .absolute_time_range_config_model_value import AbsoluteTimeRangeConfigModelValue
    from .alert_attribution_model import AlertAttributionModel
    from .alert_filter_suggestion import AlertFilterSuggestion
    from .alert_filter_suggestion_alert_id import AlertFilterSuggestionAlertId
    from .alert_filter_suggestion_alert_status import AlertFilterSuggestionAlertStatus
    from .alert_filter_suggestion_cloud_type import AlertFilterSuggestionCloudType
    from .alert_filter_suggestion_policy_remediable import AlertFilterSuggestionPolicyRemediable
    from .alert_filter_suggestion_policy_subtype import AlertFilterSuggestionPolicySubtype
    from .alert_filter_suggestion_risk_grade import AlertFilterSuggestionRiskGrade
    from .alert_model import AlertModel
    from .alert_model_investigate_options import AlertModelInvestigateOptions
    from .alert_model_risk_detail import AlertModelRiskDetail
    from .alert_model_status import AlertModelStatus
    from .alert_rule_notification_config_model import AlertRuleNotificationConfigModel
    from .alert_rule_notification_config_model_frequency import AlertRuleNotificationConfigModelFrequency
    from .alert_rule_notification_config_model_type import AlertRuleNotificationConfigModelType
    from .alert_rule_policy_filter import AlertRulePolicyFilter
    from .alert_rule_policy_filter_cloud_type_item import AlertRulePolicyFilterCloudTypeItem
    from .alert_status_change_request_model import AlertStatusChangeRequestModel
    from .alert_status_change_request_model_dismissal_time_range import (
        AlertStatusChangeRequestModelDismissalTimeRange,
        AlertStatusChangeRequestModelDismissalTimeRange_Absolute,
        AlertStatusChangeRequestModelDismissalTimeRange_Relative,
        AlertStatusChangeRequestModelDismissalTimeRange_ToNow,
    )
    from .alert_status_change_request_model_filter import AlertStatusChangeRequestModelFilter
    from .alert_status_change_request_model_filter_time_range import (
        AlertStatusChangeRequestModelFilterTimeRange,
        AlertStatusChangeRequestModelFilterTimeRange_Absolute,
        AlertStatusChangeRequestModelFilterTimeRange_Relative,
        AlertStatusChangeRequestModelFilterTimeRange_ToNow,
    )
    from .async_job import AsyncJob
    from .async_job_status import AsyncJobStatus
    from .attribution_event_model import AttributionEventModel
    from .base_filter_model import BaseFilterModel
    from .cloud_resource_model import CloudResourceModel
    from .cloud_resource_model_additional_info import CloudResourceModelAdditionalInfo
    from .cloud_resource_model_additional_info_node_type import CloudResourceModelAdditionalInfoNodeType
    from .cloud_resource_model_cloud_type import CloudResourceModelCloudType
    from .compliance_metadata_model import ComplianceMetadataModel
    from .connection_detail import ConnectionDetail
    from .count_model import CountModel
    from .filter_model import FilterModel
    from .filter_model_time_range import (
        FilterModelTimeRange,
        FilterModelTimeRange_Absolute,
        FilterModelTimeRange_Relative,
        FilterModelTimeRange_ToNow,
    )
    from .filter_suggestion import FilterSuggestion
    from .history_model import HistoryModel
    from .history_model_status import HistoryModelStatus
    from .investigate_options import InvestigateOptions
    from .json_node import JsonNode
    from .json_node_node_type import JsonNodeNodeType
    from .name_value_integer_string import NameValueIntegerString
    from .paged_results_alert_model import PagedResultsAlertModel
    from .parsed_table_filter import ParsedTableFilter
    from .policy_model import PolicyModel
    from .policy_model_cloud_type import PolicyModelCloudType
    from .policy_model_policy_sub_types_item import PolicyModelPolicySubTypesItem
    from .policy_model_policy_type import PolicyModelPolicyType
    from .policy_model_remediation import PolicyModelRemediation
    from .policy_model_rule import PolicyModelRule
    from .policy_model_rule_data_criteria import PolicyModelRuleDataCriteria
    from .policy_model_rule_data_criteria_exposure import PolicyModelRuleDataCriteriaExposure
    from .policy_model_rule_type import PolicyModelRuleType
    from .policy_model_severity import PolicyModelSeverity
    from .policy_risk_score_model import PolicyRiskScoreModel
    from .policy_risk_score_model_cloud_type import PolicyRiskScoreModelCloudType
    from .policy_risk_score_model_policy_sub_types_item import PolicyRiskScoreModelPolicySubTypesItem
    from .policy_risk_score_model_policy_type import PolicyRiskScoreModelPolicyType
    from .policy_risk_score_model_remediation import PolicyRiskScoreModelRemediation
    from .policy_risk_score_model_rule import PolicyRiskScoreModelRule
    from .policy_risk_score_model_rule_data_criteria import PolicyRiskScoreModelRuleDataCriteria
    from .policy_risk_score_model_rule_data_criteria_exposure import PolicyRiskScoreModelRuleDataCriteriaExposure
    from .policy_risk_score_model_rule_type import PolicyRiskScoreModelRuleType
    from .policy_risk_score_model_severity import PolicyRiskScoreModelSeverity
    from .policy_scan_config_model import PolicyScanConfigModel
    from .policy_scan_config_model_target import PolicyScanConfigModelTarget
    from .policy_scan_config_model_target_alert_rule_policy_filter import (
        PolicyScanConfigModelTargetAlertRulePolicyFilter,
    )
    from .policy_scan_config_model_target_alert_rule_policy_filter_cloud_type_item import (
        PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem,
    )
    from .policy_scan_config_model_target_included_resource_lists import (
        PolicyScanConfigModelTargetIncludedResourceLists,
    )
    from .relative_time_duration_model import RelativeTimeDurationModel
    from .relative_time_duration_model_unit import RelativeTimeDurationModelUnit
    from .relative_time_range_config_model import RelativeTimeRangeConfigModel
    from .relative_time_range_config_model_relative_time_type import RelativeTimeRangeConfigModelRelativeTimeType
    from .relative_time_range_config_model_value import RelativeTimeRangeConfigModelValue
    from .relative_time_range_config_model_value_unit import RelativeTimeRangeConfigModelValueUnit
    from .remediation_action import RemediationAction
    from .remediation_cli_model import RemediationCliModel
    from .remediation_model import RemediationModel
    from .require_dismissal_note_config_model import RequireDismissalNoteConfigModel
    from .resource_list_ids_collection import ResourceListIdsCollection
    from .risk_detail_model import RiskDetailModel
    from .rule_criteria import RuleCriteria
    from .rule_criteria_exposure import RuleCriteriaExposure
    from .rule_model import RuleModel
    from .rule_model_data_criteria import RuleModelDataCriteria
    from .rule_model_data_criteria_exposure import RuleModelDataCriteriaExposure
    from .rule_model_type import RuleModelType
    from .score_model import ScoreModel
    from .target_filter_model import TargetFilterModel
    from .target_filter_model_alert_rule_policy_filter import TargetFilterModelAlertRulePolicyFilter
    from .target_filter_model_alert_rule_policy_filter_cloud_type_item import (
        TargetFilterModelAlertRulePolicyFilterCloudTypeItem,
    )
    from .target_filter_model_included_resource_lists import TargetFilterModelIncludedResourceLists
    from .target_tag_model import TargetTagModel
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
    from .week_day import WeekDay
    from .week_day_day import WeekDayDay
_dynamic_imports: typing.Dict[str, str] = {
    "AbsoluteTimeRangeConfigModel": ".absolute_time_range_config_model",
    "AbsoluteTimeRangeConfigModelValue": ".absolute_time_range_config_model_value",
    "AlertAttributionModel": ".alert_attribution_model",
    "AlertFilterSuggestion": ".alert_filter_suggestion",
    "AlertFilterSuggestionAlertId": ".alert_filter_suggestion_alert_id",
    "AlertFilterSuggestionAlertStatus": ".alert_filter_suggestion_alert_status",
    "AlertFilterSuggestionCloudType": ".alert_filter_suggestion_cloud_type",
    "AlertFilterSuggestionPolicyRemediable": ".alert_filter_suggestion_policy_remediable",
    "AlertFilterSuggestionPolicySubtype": ".alert_filter_suggestion_policy_subtype",
    "AlertFilterSuggestionRiskGrade": ".alert_filter_suggestion_risk_grade",
    "AlertModel": ".alert_model",
    "AlertModelInvestigateOptions": ".alert_model_investigate_options",
    "AlertModelRiskDetail": ".alert_model_risk_detail",
    "AlertModelStatus": ".alert_model_status",
    "AlertRuleNotificationConfigModel": ".alert_rule_notification_config_model",
    "AlertRuleNotificationConfigModelFrequency": ".alert_rule_notification_config_model_frequency",
    "AlertRuleNotificationConfigModelType": ".alert_rule_notification_config_model_type",
    "AlertRulePolicyFilter": ".alert_rule_policy_filter",
    "AlertRulePolicyFilterCloudTypeItem": ".alert_rule_policy_filter_cloud_type_item",
    "AlertStatusChangeRequestModel": ".alert_status_change_request_model",
    "AlertStatusChangeRequestModelDismissalTimeRange": ".alert_status_change_request_model_dismissal_time_range",
    "AlertStatusChangeRequestModelDismissalTimeRange_Absolute": ".alert_status_change_request_model_dismissal_time_range",
    "AlertStatusChangeRequestModelDismissalTimeRange_Relative": ".alert_status_change_request_model_dismissal_time_range",
    "AlertStatusChangeRequestModelDismissalTimeRange_ToNow": ".alert_status_change_request_model_dismissal_time_range",
    "AlertStatusChangeRequestModelFilter": ".alert_status_change_request_model_filter",
    "AlertStatusChangeRequestModelFilterTimeRange": ".alert_status_change_request_model_filter_time_range",
    "AlertStatusChangeRequestModelFilterTimeRange_Absolute": ".alert_status_change_request_model_filter_time_range",
    "AlertStatusChangeRequestModelFilterTimeRange_Relative": ".alert_status_change_request_model_filter_time_range",
    "AlertStatusChangeRequestModelFilterTimeRange_ToNow": ".alert_status_change_request_model_filter_time_range",
    "AsyncJob": ".async_job",
    "AsyncJobStatus": ".async_job_status",
    "AttributionEventModel": ".attribution_event_model",
    "BaseFilterModel": ".base_filter_model",
    "CloudResourceModel": ".cloud_resource_model",
    "CloudResourceModelAdditionalInfo": ".cloud_resource_model_additional_info",
    "CloudResourceModelAdditionalInfoNodeType": ".cloud_resource_model_additional_info_node_type",
    "CloudResourceModelCloudType": ".cloud_resource_model_cloud_type",
    "ComplianceMetadataModel": ".compliance_metadata_model",
    "ConnectionDetail": ".connection_detail",
    "CountModel": ".count_model",
    "FilterModel": ".filter_model",
    "FilterModelTimeRange": ".filter_model_time_range",
    "FilterModelTimeRange_Absolute": ".filter_model_time_range",
    "FilterModelTimeRange_Relative": ".filter_model_time_range",
    "FilterModelTimeRange_ToNow": ".filter_model_time_range",
    "FilterSuggestion": ".filter_suggestion",
    "HistoryModel": ".history_model",
    "HistoryModelStatus": ".history_model_status",
    "InvestigateOptions": ".investigate_options",
    "JsonNode": ".json_node",
    "JsonNodeNodeType": ".json_node_node_type",
    "NameValueIntegerString": ".name_value_integer_string",
    "PagedResultsAlertModel": ".paged_results_alert_model",
    "ParsedTableFilter": ".parsed_table_filter",
    "PolicyModel": ".policy_model",
    "PolicyModelCloudType": ".policy_model_cloud_type",
    "PolicyModelPolicySubTypesItem": ".policy_model_policy_sub_types_item",
    "PolicyModelPolicyType": ".policy_model_policy_type",
    "PolicyModelRemediation": ".policy_model_remediation",
    "PolicyModelRule": ".policy_model_rule",
    "PolicyModelRuleDataCriteria": ".policy_model_rule_data_criteria",
    "PolicyModelRuleDataCriteriaExposure": ".policy_model_rule_data_criteria_exposure",
    "PolicyModelRuleType": ".policy_model_rule_type",
    "PolicyModelSeverity": ".policy_model_severity",
    "PolicyRiskScoreModel": ".policy_risk_score_model",
    "PolicyRiskScoreModelCloudType": ".policy_risk_score_model_cloud_type",
    "PolicyRiskScoreModelPolicySubTypesItem": ".policy_risk_score_model_policy_sub_types_item",
    "PolicyRiskScoreModelPolicyType": ".policy_risk_score_model_policy_type",
    "PolicyRiskScoreModelRemediation": ".policy_risk_score_model_remediation",
    "PolicyRiskScoreModelRule": ".policy_risk_score_model_rule",
    "PolicyRiskScoreModelRuleDataCriteria": ".policy_risk_score_model_rule_data_criteria",
    "PolicyRiskScoreModelRuleDataCriteriaExposure": ".policy_risk_score_model_rule_data_criteria_exposure",
    "PolicyRiskScoreModelRuleType": ".policy_risk_score_model_rule_type",
    "PolicyRiskScoreModelSeverity": ".policy_risk_score_model_severity",
    "PolicyScanConfigModel": ".policy_scan_config_model",
    "PolicyScanConfigModelTarget": ".policy_scan_config_model_target",
    "PolicyScanConfigModelTargetAlertRulePolicyFilter": ".policy_scan_config_model_target_alert_rule_policy_filter",
    "PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem": ".policy_scan_config_model_target_alert_rule_policy_filter_cloud_type_item",
    "PolicyScanConfigModelTargetIncludedResourceLists": ".policy_scan_config_model_target_included_resource_lists",
    "RelativeTimeDurationModel": ".relative_time_duration_model",
    "RelativeTimeDurationModelUnit": ".relative_time_duration_model_unit",
    "RelativeTimeRangeConfigModel": ".relative_time_range_config_model",
    "RelativeTimeRangeConfigModelRelativeTimeType": ".relative_time_range_config_model_relative_time_type",
    "RelativeTimeRangeConfigModelValue": ".relative_time_range_config_model_value",
    "RelativeTimeRangeConfigModelValueUnit": ".relative_time_range_config_model_value_unit",
    "RemediationAction": ".remediation_action",
    "RemediationCliModel": ".remediation_cli_model",
    "RemediationModel": ".remediation_model",
    "RequireDismissalNoteConfigModel": ".require_dismissal_note_config_model",
    "ResourceListIdsCollection": ".resource_list_ids_collection",
    "RiskDetailModel": ".risk_detail_model",
    "RuleCriteria": ".rule_criteria",
    "RuleCriteriaExposure": ".rule_criteria_exposure",
    "RuleModel": ".rule_model",
    "RuleModelDataCriteria": ".rule_model_data_criteria",
    "RuleModelDataCriteriaExposure": ".rule_model_data_criteria_exposure",
    "RuleModelType": ".rule_model_type",
    "ScoreModel": ".score_model",
    "TargetFilterModel": ".target_filter_model",
    "TargetFilterModelAlertRulePolicyFilter": ".target_filter_model_alert_rule_policy_filter",
    "TargetFilterModelAlertRulePolicyFilterCloudTypeItem": ".target_filter_model_alert_rule_policy_filter_cloud_type_item",
    "TargetFilterModelIncludedResourceLists": ".target_filter_model_included_resource_lists",
    "TargetTagModel": ".target_tag_model",
    "TimeModel": ".time_model",
    "TimeRangeConfigModel": ".time_range_config_model",
    "TimeRangeConfigModel_Absolute": ".time_range_config_model",
    "TimeRangeConfigModel_Relative": ".time_range_config_model",
    "TimeRangeConfigModel_ToNow": ".time_range_config_model",
    "ToNowTimeRangeConfigModel": ".to_now_time_range_config_model",
    "ToNowTimeRangeConfigModelValue": ".to_now_time_range_config_model_value",
    "UiFilterModel": ".ui_filter_model",
    "UiFilterModelOperator": ".ui_filter_model_operator",
    "WeekDay": ".week_day",
    "WeekDayDay": ".week_day_day",
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
    "AlertAttributionModel",
    "AlertFilterSuggestion",
    "AlertFilterSuggestionAlertId",
    "AlertFilterSuggestionAlertStatus",
    "AlertFilterSuggestionCloudType",
    "AlertFilterSuggestionPolicyRemediable",
    "AlertFilterSuggestionPolicySubtype",
    "AlertFilterSuggestionRiskGrade",
    "AlertModel",
    "AlertModelInvestigateOptions",
    "AlertModelRiskDetail",
    "AlertModelStatus",
    "AlertRuleNotificationConfigModel",
    "AlertRuleNotificationConfigModelFrequency",
    "AlertRuleNotificationConfigModelType",
    "AlertRulePolicyFilter",
    "AlertRulePolicyFilterCloudTypeItem",
    "AlertStatusChangeRequestModel",
    "AlertStatusChangeRequestModelDismissalTimeRange",
    "AlertStatusChangeRequestModelDismissalTimeRange_Absolute",
    "AlertStatusChangeRequestModelDismissalTimeRange_Relative",
    "AlertStatusChangeRequestModelDismissalTimeRange_ToNow",
    "AlertStatusChangeRequestModelFilter",
    "AlertStatusChangeRequestModelFilterTimeRange",
    "AlertStatusChangeRequestModelFilterTimeRange_Absolute",
    "AlertStatusChangeRequestModelFilterTimeRange_Relative",
    "AlertStatusChangeRequestModelFilterTimeRange_ToNow",
    "AsyncJob",
    "AsyncJobStatus",
    "AttributionEventModel",
    "BaseFilterModel",
    "CloudResourceModel",
    "CloudResourceModelAdditionalInfo",
    "CloudResourceModelAdditionalInfoNodeType",
    "CloudResourceModelCloudType",
    "ComplianceMetadataModel",
    "ConnectionDetail",
    "CountModel",
    "FilterModel",
    "FilterModelTimeRange",
    "FilterModelTimeRange_Absolute",
    "FilterModelTimeRange_Relative",
    "FilterModelTimeRange_ToNow",
    "FilterSuggestion",
    "HistoryModel",
    "HistoryModelStatus",
    "InvestigateOptions",
    "JsonNode",
    "JsonNodeNodeType",
    "NameValueIntegerString",
    "PagedResultsAlertModel",
    "ParsedTableFilter",
    "PolicyModel",
    "PolicyModelCloudType",
    "PolicyModelPolicySubTypesItem",
    "PolicyModelPolicyType",
    "PolicyModelRemediation",
    "PolicyModelRule",
    "PolicyModelRuleDataCriteria",
    "PolicyModelRuleDataCriteriaExposure",
    "PolicyModelRuleType",
    "PolicyModelSeverity",
    "PolicyRiskScoreModel",
    "PolicyRiskScoreModelCloudType",
    "PolicyRiskScoreModelPolicySubTypesItem",
    "PolicyRiskScoreModelPolicyType",
    "PolicyRiskScoreModelRemediation",
    "PolicyRiskScoreModelRule",
    "PolicyRiskScoreModelRuleDataCriteria",
    "PolicyRiskScoreModelRuleDataCriteriaExposure",
    "PolicyRiskScoreModelRuleType",
    "PolicyRiskScoreModelSeverity",
    "PolicyScanConfigModel",
    "PolicyScanConfigModelTarget",
    "PolicyScanConfigModelTargetAlertRulePolicyFilter",
    "PolicyScanConfigModelTargetAlertRulePolicyFilterCloudTypeItem",
    "PolicyScanConfigModelTargetIncludedResourceLists",
    "RelativeTimeDurationModel",
    "RelativeTimeDurationModelUnit",
    "RelativeTimeRangeConfigModel",
    "RelativeTimeRangeConfigModelRelativeTimeType",
    "RelativeTimeRangeConfigModelValue",
    "RelativeTimeRangeConfigModelValueUnit",
    "RemediationAction",
    "RemediationCliModel",
    "RemediationModel",
    "RequireDismissalNoteConfigModel",
    "ResourceListIdsCollection",
    "RiskDetailModel",
    "RuleCriteria",
    "RuleCriteriaExposure",
    "RuleModel",
    "RuleModelDataCriteria",
    "RuleModelDataCriteriaExposure",
    "RuleModelType",
    "ScoreModel",
    "TargetFilterModel",
    "TargetFilterModelAlertRulePolicyFilter",
    "TargetFilterModelAlertRulePolicyFilterCloudTypeItem",
    "TargetFilterModelIncludedResourceLists",
    "TargetTagModel",
    "TimeModel",
    "TimeRangeConfigModel",
    "TimeRangeConfigModel_Absolute",
    "TimeRangeConfigModel_Relative",
    "TimeRangeConfigModel_ToNow",
    "ToNowTimeRangeConfigModel",
    "ToNowTimeRangeConfigModelValue",
    "UiFilterModel",
    "UiFilterModelOperator",
    "WeekDay",
    "WeekDayDay",
]

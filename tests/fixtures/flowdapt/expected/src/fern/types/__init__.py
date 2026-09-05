



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_error_model import ApiErrorModel
    from .http_validation_error import HttpValidationError
    from .ping_response import PingResponse
    from .v1alpha1config_resource_create_request import V1Alpha1ConfigResourceCreateRequest
    from .v1alpha1config_resource_create_response import V1Alpha1ConfigResourceCreateResponse
    from .v1alpha1config_resource_read_response import V1Alpha1ConfigResourceReadResponse
    from .v1alpha1config_resource_spec import V1Alpha1ConfigResourceSpec
    from .v1alpha1config_resource_update_response import V1Alpha1ConfigResourceUpdateResponse
    from .v1alpha1config_selector import V1Alpha1ConfigSelector
    from .v1alpha1config_selector_type import V1Alpha1ConfigSelectorType
    from .v1alpha1config_selector_value import V1Alpha1ConfigSelectorValue
    from .v1alpha1metrics import V1Alpha1Metrics
    from .v1alpha1metrics_bucket_value import V1Alpha1MetricsBucketValue
    from .v1alpha1metrics_bucket_value_explicit_bounds_item import V1Alpha1MetricsBucketValueExplicitBoundsItem
    from .v1alpha1metrics_bucket_value_max import V1Alpha1MetricsBucketValueMax
    from .v1alpha1metrics_bucket_value_min import V1Alpha1MetricsBucketValueMin
    from .v1alpha1metrics_bucket_value_sum import V1Alpha1MetricsBucketValueSum
    from .v1alpha1metrics_count_value import V1Alpha1MetricsCountValue
    from .v1alpha1metrics_count_value_value import V1Alpha1MetricsCountValueValue
    from .v1alpha1metrics_value_item import V1Alpha1MetricsValueItem
    from .v1alpha1plugin import V1Alpha1Plugin
    from .v1alpha1plugin_files import V1Alpha1PluginFiles
    from .v1alpha1plugin_metadata import V1Alpha1PluginMetadata
    from .v1alpha1resource_metadata import V1Alpha1ResourceMetadata
    from .v1alpha1system_status import V1Alpha1SystemStatus
    from .v1alpha1system_status_os_info import V1Alpha1SystemStatusOsInfo
    from .v1alpha1system_status_system_info import V1Alpha1SystemStatusSystemInfo
    from .v1alpha1trigger_rule_action import V1Alpha1TriggerRuleAction
    from .v1alpha1trigger_rule_resource_create_response import V1Alpha1TriggerRuleResourceCreateResponse
    from .v1alpha1trigger_rule_resource_read_response import V1Alpha1TriggerRuleResourceReadResponse
    from .v1alpha1trigger_rule_resource_spec import V1Alpha1TriggerRuleResourceSpec
    from .v1alpha1trigger_rule_resource_spec_rule import V1Alpha1TriggerRuleResourceSpecRule
    from .v1alpha1trigger_rule_resource_update_response import V1Alpha1TriggerRuleResourceUpdateResponse
    from .v1alpha1trigger_rule_type import V1Alpha1TriggerRuleType
    from .v1alpha1workflow_resource_create_response import V1Alpha1WorkflowResourceCreateResponse
    from .v1alpha1workflow_resource_read_response import V1Alpha1WorkflowResourceReadResponse
    from .v1alpha1workflow_resource_spec import V1Alpha1WorkflowResourceSpec
    from .v1alpha1workflow_resource_update_response import V1Alpha1WorkflowResourceUpdateResponse
    from .v1alpha1workflow_run_read_response import V1Alpha1WorkflowRunReadResponse
    from .v1alpha1workflow_stage import V1Alpha1WorkflowStage
    from .v1alpha2config_resource_create_request import V1Alpha2ConfigResourceCreateRequest
    from .v1alpha2config_resource_create_response import V1Alpha2ConfigResourceCreateResponse
    from .v1alpha2config_resource_spec import V1Alpha2ConfigResourceSpec
    from .v1alpha2config_selector import V1Alpha2ConfigSelector
    from .v1alpha2config_selector_value import V1Alpha2ConfigSelectorValue
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "ApiErrorModel": ".api_error_model",
    "HttpValidationError": ".http_validation_error",
    "PingResponse": ".ping_response",
    "V1Alpha1ConfigResourceCreateRequest": ".v1alpha1config_resource_create_request",
    "V1Alpha1ConfigResourceCreateResponse": ".v1alpha1config_resource_create_response",
    "V1Alpha1ConfigResourceReadResponse": ".v1alpha1config_resource_read_response",
    "V1Alpha1ConfigResourceSpec": ".v1alpha1config_resource_spec",
    "V1Alpha1ConfigResourceUpdateResponse": ".v1alpha1config_resource_update_response",
    "V1Alpha1ConfigSelector": ".v1alpha1config_selector",
    "V1Alpha1ConfigSelectorType": ".v1alpha1config_selector_type",
    "V1Alpha1ConfigSelectorValue": ".v1alpha1config_selector_value",
    "V1Alpha1Metrics": ".v1alpha1metrics",
    "V1Alpha1MetricsBucketValue": ".v1alpha1metrics_bucket_value",
    "V1Alpha1MetricsBucketValueExplicitBoundsItem": ".v1alpha1metrics_bucket_value_explicit_bounds_item",
    "V1Alpha1MetricsBucketValueMax": ".v1alpha1metrics_bucket_value_max",
    "V1Alpha1MetricsBucketValueMin": ".v1alpha1metrics_bucket_value_min",
    "V1Alpha1MetricsBucketValueSum": ".v1alpha1metrics_bucket_value_sum",
    "V1Alpha1MetricsCountValue": ".v1alpha1metrics_count_value",
    "V1Alpha1MetricsCountValueValue": ".v1alpha1metrics_count_value_value",
    "V1Alpha1MetricsValueItem": ".v1alpha1metrics_value_item",
    "V1Alpha1Plugin": ".v1alpha1plugin",
    "V1Alpha1PluginFiles": ".v1alpha1plugin_files",
    "V1Alpha1PluginMetadata": ".v1alpha1plugin_metadata",
    "V1Alpha1ResourceMetadata": ".v1alpha1resource_metadata",
    "V1Alpha1SystemStatus": ".v1alpha1system_status",
    "V1Alpha1SystemStatusOsInfo": ".v1alpha1system_status_os_info",
    "V1Alpha1SystemStatusSystemInfo": ".v1alpha1system_status_system_info",
    "V1Alpha1TriggerRuleAction": ".v1alpha1trigger_rule_action",
    "V1Alpha1TriggerRuleResourceCreateResponse": ".v1alpha1trigger_rule_resource_create_response",
    "V1Alpha1TriggerRuleResourceReadResponse": ".v1alpha1trigger_rule_resource_read_response",
    "V1Alpha1TriggerRuleResourceSpec": ".v1alpha1trigger_rule_resource_spec",
    "V1Alpha1TriggerRuleResourceSpecRule": ".v1alpha1trigger_rule_resource_spec_rule",
    "V1Alpha1TriggerRuleResourceUpdateResponse": ".v1alpha1trigger_rule_resource_update_response",
    "V1Alpha1TriggerRuleType": ".v1alpha1trigger_rule_type",
    "V1Alpha1WorkflowResourceCreateResponse": ".v1alpha1workflow_resource_create_response",
    "V1Alpha1WorkflowResourceReadResponse": ".v1alpha1workflow_resource_read_response",
    "V1Alpha1WorkflowResourceSpec": ".v1alpha1workflow_resource_spec",
    "V1Alpha1WorkflowResourceUpdateResponse": ".v1alpha1workflow_resource_update_response",
    "V1Alpha1WorkflowRunReadResponse": ".v1alpha1workflow_run_read_response",
    "V1Alpha1WorkflowStage": ".v1alpha1workflow_stage",
    "V1Alpha2ConfigResourceCreateRequest": ".v1alpha2config_resource_create_request",
    "V1Alpha2ConfigResourceCreateResponse": ".v1alpha2config_resource_create_response",
    "V1Alpha2ConfigResourceSpec": ".v1alpha2config_resource_spec",
    "V1Alpha2ConfigSelector": ".v1alpha2config_selector",
    "V1Alpha2ConfigSelectorValue": ".v1alpha2config_selector_value",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "ApiErrorModel",
    "HttpValidationError",
    "PingResponse",
    "V1Alpha1ConfigResourceCreateRequest",
    "V1Alpha1ConfigResourceCreateResponse",
    "V1Alpha1ConfigResourceReadResponse",
    "V1Alpha1ConfigResourceSpec",
    "V1Alpha1ConfigResourceUpdateResponse",
    "V1Alpha1ConfigSelector",
    "V1Alpha1ConfigSelectorType",
    "V1Alpha1ConfigSelectorValue",
    "V1Alpha1Metrics",
    "V1Alpha1MetricsBucketValue",
    "V1Alpha1MetricsBucketValueExplicitBoundsItem",
    "V1Alpha1MetricsBucketValueMax",
    "V1Alpha1MetricsBucketValueMin",
    "V1Alpha1MetricsBucketValueSum",
    "V1Alpha1MetricsCountValue",
    "V1Alpha1MetricsCountValueValue",
    "V1Alpha1MetricsValueItem",
    "V1Alpha1Plugin",
    "V1Alpha1PluginFiles",
    "V1Alpha1PluginMetadata",
    "V1Alpha1ResourceMetadata",
    "V1Alpha1SystemStatus",
    "V1Alpha1SystemStatusOsInfo",
    "V1Alpha1SystemStatusSystemInfo",
    "V1Alpha1TriggerRuleAction",
    "V1Alpha1TriggerRuleResourceCreateResponse",
    "V1Alpha1TriggerRuleResourceReadResponse",
    "V1Alpha1TriggerRuleResourceSpec",
    "V1Alpha1TriggerRuleResourceSpecRule",
    "V1Alpha1TriggerRuleResourceUpdateResponse",
    "V1Alpha1TriggerRuleType",
    "V1Alpha1WorkflowResourceCreateResponse",
    "V1Alpha1WorkflowResourceReadResponse",
    "V1Alpha1WorkflowResourceSpec",
    "V1Alpha1WorkflowResourceUpdateResponse",
    "V1Alpha1WorkflowRunReadResponse",
    "V1Alpha1WorkflowStage",
    "V1Alpha2ConfigResourceCreateRequest",
    "V1Alpha2ConfigResourceCreateResponse",
    "V1Alpha2ConfigResourceSpec",
    "V1Alpha2ConfigSelector",
    "V1Alpha2ConfigSelectorValue",
    "ValidationError",
    "ValidationErrorLocItem",
]

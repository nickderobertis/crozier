



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ApiErrorModel,
        HttpValidationError,
        PingResponse,
        V1Alpha1ConfigResourceCreateRequest,
        V1Alpha1ConfigResourceCreateResponse,
        V1Alpha1ConfigResourceReadResponse,
        V1Alpha1ConfigResourceSpec,
        V1Alpha1ConfigResourceUpdateResponse,
        V1Alpha1ConfigSelector,
        V1Alpha1ConfigSelectorType,
        V1Alpha1ConfigSelectorValue,
        V1Alpha1Metrics,
        V1Alpha1MetricsBucketValue,
        V1Alpha1MetricsBucketValueExplicitBoundsItem,
        V1Alpha1MetricsBucketValueMax,
        V1Alpha1MetricsBucketValueMin,
        V1Alpha1MetricsBucketValueSum,
        V1Alpha1MetricsCountValue,
        V1Alpha1MetricsCountValueValue,
        V1Alpha1MetricsValueItem,
        V1Alpha1Plugin,
        V1Alpha1PluginFiles,
        V1Alpha1PluginMetadata,
        V1Alpha1ResourceMetadata,
        V1Alpha1SystemStatus,
        V1Alpha1SystemStatusOsInfo,
        V1Alpha1SystemStatusSystemInfo,
        V1Alpha1TriggerRuleAction,
        V1Alpha1TriggerRuleResourceCreateResponse,
        V1Alpha1TriggerRuleResourceReadResponse,
        V1Alpha1TriggerRuleResourceSpec,
        V1Alpha1TriggerRuleResourceSpecRule,
        V1Alpha1TriggerRuleResourceUpdateResponse,
        V1Alpha1TriggerRuleType,
        V1Alpha1WorkflowResourceCreateResponse,
        V1Alpha1WorkflowResourceReadResponse,
        V1Alpha1WorkflowResourceSpec,
        V1Alpha1WorkflowResourceUpdateResponse,
        V1Alpha1WorkflowRunReadResponse,
        V1Alpha1WorkflowStage,
        V1Alpha2ConfigResourceCreateRequest,
        V1Alpha2ConfigResourceCreateResponse,
        V1Alpha2ConfigResourceSpec,
        V1Alpha2ConfigSelector,
        V1Alpha2ConfigSelectorValue,
        ValidationError,
        ValidationErrorLocItem,
    )
    from .errors import ForbiddenError, MethodNotAllowedError, NotFoundError, UnprocessableEntityError
    from . import configs, health, plugins, triggers, workflows
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .configs import CreateConfigRequestBody
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ApiErrorModel": ".types",
    "AsyncFernApi": ".client",
    "CreateConfigRequestBody": ".configs",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "ForbiddenError": ".errors",
    "HttpValidationError": ".types",
    "MethodNotAllowedError": ".errors",
    "NotFoundError": ".errors",
    "PingResponse": ".types",
    "UnprocessableEntityError": ".errors",
    "V1Alpha1ConfigResourceCreateRequest": ".types",
    "V1Alpha1ConfigResourceCreateResponse": ".types",
    "V1Alpha1ConfigResourceReadResponse": ".types",
    "V1Alpha1ConfigResourceSpec": ".types",
    "V1Alpha1ConfigResourceUpdateResponse": ".types",
    "V1Alpha1ConfigSelector": ".types",
    "V1Alpha1ConfigSelectorType": ".types",
    "V1Alpha1ConfigSelectorValue": ".types",
    "V1Alpha1Metrics": ".types",
    "V1Alpha1MetricsBucketValue": ".types",
    "V1Alpha1MetricsBucketValueExplicitBoundsItem": ".types",
    "V1Alpha1MetricsBucketValueMax": ".types",
    "V1Alpha1MetricsBucketValueMin": ".types",
    "V1Alpha1MetricsBucketValueSum": ".types",
    "V1Alpha1MetricsCountValue": ".types",
    "V1Alpha1MetricsCountValueValue": ".types",
    "V1Alpha1MetricsValueItem": ".types",
    "V1Alpha1Plugin": ".types",
    "V1Alpha1PluginFiles": ".types",
    "V1Alpha1PluginMetadata": ".types",
    "V1Alpha1ResourceMetadata": ".types",
    "V1Alpha1SystemStatus": ".types",
    "V1Alpha1SystemStatusOsInfo": ".types",
    "V1Alpha1SystemStatusSystemInfo": ".types",
    "V1Alpha1TriggerRuleAction": ".types",
    "V1Alpha1TriggerRuleResourceCreateResponse": ".types",
    "V1Alpha1TriggerRuleResourceReadResponse": ".types",
    "V1Alpha1TriggerRuleResourceSpec": ".types",
    "V1Alpha1TriggerRuleResourceSpecRule": ".types",
    "V1Alpha1TriggerRuleResourceUpdateResponse": ".types",
    "V1Alpha1TriggerRuleType": ".types",
    "V1Alpha1WorkflowResourceCreateResponse": ".types",
    "V1Alpha1WorkflowResourceReadResponse": ".types",
    "V1Alpha1WorkflowResourceSpec": ".types",
    "V1Alpha1WorkflowResourceUpdateResponse": ".types",
    "V1Alpha1WorkflowRunReadResponse": ".types",
    "V1Alpha1WorkflowStage": ".types",
    "V1Alpha2ConfigResourceCreateRequest": ".types",
    "V1Alpha2ConfigResourceCreateResponse": ".types",
    "V1Alpha2ConfigResourceSpec": ".types",
    "V1Alpha2ConfigSelector": ".types",
    "V1Alpha2ConfigSelectorValue": ".types",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "__version__": ".version",
    "configs": ".configs",
    "health": ".health",
    "plugins": ".plugins",
    "triggers": ".triggers",
    "workflows": ".workflows",
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
    "AsyncFernApi",
    "CreateConfigRequestBody",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "ForbiddenError",
    "HttpValidationError",
    "MethodNotAllowedError",
    "NotFoundError",
    "PingResponse",
    "UnprocessableEntityError",
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
    "__version__",
    "configs",
    "health",
    "plugins",
    "triggers",
    "workflows",
]

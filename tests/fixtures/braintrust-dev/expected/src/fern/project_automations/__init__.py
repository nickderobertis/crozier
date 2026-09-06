



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetProjectAutomationResponse,
        PatchProjectAutomationConfig,
        PatchProjectAutomationConfigBatchSize,
        PatchProjectAutomationConfigBatchSizeCredentials,
        PatchProjectAutomationConfigBatchSizeCredentialsType,
        PatchProjectAutomationConfigBatchSizeEventType,
        PatchProjectAutomationConfigBatchSizeExportDefinition,
        PatchProjectAutomationConfigBatchSizeExportDefinitionBtqlQuery,
        PatchProjectAutomationConfigBatchSizeExportDefinitionLogSpans,
        PatchProjectAutomationConfigBatchSizeExportDefinitionLogTraces,
        PatchProjectAutomationConfigBatchSizeExportDefinition_BtqlQuery,
        PatchProjectAutomationConfigBatchSizeExportDefinition_LogSpans,
        PatchProjectAutomationConfigBatchSizeExportDefinition_LogTraces,
        PatchProjectAutomationConfigBatchSizeFormat,
        PatchProjectAutomationConfigBtqlFilter,
        PatchProjectAutomationConfigBtqlFilterAction,
        PatchProjectAutomationConfigBtqlFilterActionSlack,
        PatchProjectAutomationConfigBtqlFilterActionWebhook,
        PatchProjectAutomationConfigBtqlFilterAction_Slack,
        PatchProjectAutomationConfigBtqlFilterAction_Webhook,
        PatchProjectAutomationConfigBtqlFilterEventType,
        PatchProjectAutomationConfigEnvironmentFilter,
        PatchProjectAutomationConfigEnvironmentFilterAction,
        PatchProjectAutomationConfigEnvironmentFilterActionSlack,
        PatchProjectAutomationConfigEnvironmentFilterActionWebhook,
        PatchProjectAutomationConfigEnvironmentFilterAction_Slack,
        PatchProjectAutomationConfigEnvironmentFilterAction_Webhook,
        PatchProjectAutomationConfigEnvironmentFilterEventType,
        PatchProjectAutomationConfigObjectType,
        PatchProjectAutomationConfigObjectTypeEventType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetProjectAutomationResponse": ".types",
    "PatchProjectAutomationConfig": ".types",
    "PatchProjectAutomationConfigBatchSize": ".types",
    "PatchProjectAutomationConfigBatchSizeCredentials": ".types",
    "PatchProjectAutomationConfigBatchSizeCredentialsType": ".types",
    "PatchProjectAutomationConfigBatchSizeEventType": ".types",
    "PatchProjectAutomationConfigBatchSizeExportDefinition": ".types",
    "PatchProjectAutomationConfigBatchSizeExportDefinitionBtqlQuery": ".types",
    "PatchProjectAutomationConfigBatchSizeExportDefinitionLogSpans": ".types",
    "PatchProjectAutomationConfigBatchSizeExportDefinitionLogTraces": ".types",
    "PatchProjectAutomationConfigBatchSizeExportDefinition_BtqlQuery": ".types",
    "PatchProjectAutomationConfigBatchSizeExportDefinition_LogSpans": ".types",
    "PatchProjectAutomationConfigBatchSizeExportDefinition_LogTraces": ".types",
    "PatchProjectAutomationConfigBatchSizeFormat": ".types",
    "PatchProjectAutomationConfigBtqlFilter": ".types",
    "PatchProjectAutomationConfigBtqlFilterAction": ".types",
    "PatchProjectAutomationConfigBtqlFilterActionSlack": ".types",
    "PatchProjectAutomationConfigBtqlFilterActionWebhook": ".types",
    "PatchProjectAutomationConfigBtqlFilterAction_Slack": ".types",
    "PatchProjectAutomationConfigBtqlFilterAction_Webhook": ".types",
    "PatchProjectAutomationConfigBtqlFilterEventType": ".types",
    "PatchProjectAutomationConfigEnvironmentFilter": ".types",
    "PatchProjectAutomationConfigEnvironmentFilterAction": ".types",
    "PatchProjectAutomationConfigEnvironmentFilterActionSlack": ".types",
    "PatchProjectAutomationConfigEnvironmentFilterActionWebhook": ".types",
    "PatchProjectAutomationConfigEnvironmentFilterAction_Slack": ".types",
    "PatchProjectAutomationConfigEnvironmentFilterAction_Webhook": ".types",
    "PatchProjectAutomationConfigEnvironmentFilterEventType": ".types",
    "PatchProjectAutomationConfigObjectType": ".types",
    "PatchProjectAutomationConfigObjectTypeEventType": ".types",
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
    "GetProjectAutomationResponse",
    "PatchProjectAutomationConfig",
    "PatchProjectAutomationConfigBatchSize",
    "PatchProjectAutomationConfigBatchSizeCredentials",
    "PatchProjectAutomationConfigBatchSizeCredentialsType",
    "PatchProjectAutomationConfigBatchSizeEventType",
    "PatchProjectAutomationConfigBatchSizeExportDefinition",
    "PatchProjectAutomationConfigBatchSizeExportDefinitionBtqlQuery",
    "PatchProjectAutomationConfigBatchSizeExportDefinitionLogSpans",
    "PatchProjectAutomationConfigBatchSizeExportDefinitionLogTraces",
    "PatchProjectAutomationConfigBatchSizeExportDefinition_BtqlQuery",
    "PatchProjectAutomationConfigBatchSizeExportDefinition_LogSpans",
    "PatchProjectAutomationConfigBatchSizeExportDefinition_LogTraces",
    "PatchProjectAutomationConfigBatchSizeFormat",
    "PatchProjectAutomationConfigBtqlFilter",
    "PatchProjectAutomationConfigBtqlFilterAction",
    "PatchProjectAutomationConfigBtqlFilterActionSlack",
    "PatchProjectAutomationConfigBtqlFilterActionWebhook",
    "PatchProjectAutomationConfigBtqlFilterAction_Slack",
    "PatchProjectAutomationConfigBtqlFilterAction_Webhook",
    "PatchProjectAutomationConfigBtqlFilterEventType",
    "PatchProjectAutomationConfigEnvironmentFilter",
    "PatchProjectAutomationConfigEnvironmentFilterAction",
    "PatchProjectAutomationConfigEnvironmentFilterActionSlack",
    "PatchProjectAutomationConfigEnvironmentFilterActionWebhook",
    "PatchProjectAutomationConfigEnvironmentFilterAction_Slack",
    "PatchProjectAutomationConfigEnvironmentFilterAction_Webhook",
    "PatchProjectAutomationConfigEnvironmentFilterEventType",
    "PatchProjectAutomationConfigObjectType",
    "PatchProjectAutomationConfigObjectTypeEventType",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_project_automation_response import GetProjectAutomationResponse
    from .patch_project_automation_config import PatchProjectAutomationConfig
    from .patch_project_automation_config_batch_size import PatchProjectAutomationConfigBatchSize
    from .patch_project_automation_config_batch_size_credentials import PatchProjectAutomationConfigBatchSizeCredentials
    from .patch_project_automation_config_batch_size_credentials_type import (
        PatchProjectAutomationConfigBatchSizeCredentialsType,
    )
    from .patch_project_automation_config_batch_size_event_type import PatchProjectAutomationConfigBatchSizeEventType
    from .patch_project_automation_config_batch_size_export_definition import (
        PatchProjectAutomationConfigBatchSizeExportDefinition,
        PatchProjectAutomationConfigBatchSizeExportDefinition_BtqlQuery,
        PatchProjectAutomationConfigBatchSizeExportDefinition_LogSpans,
        PatchProjectAutomationConfigBatchSizeExportDefinition_LogTraces,
    )
    from .patch_project_automation_config_batch_size_export_definition_btql_query import (
        PatchProjectAutomationConfigBatchSizeExportDefinitionBtqlQuery,
    )
    from .patch_project_automation_config_batch_size_export_definition_log_spans import (
        PatchProjectAutomationConfigBatchSizeExportDefinitionLogSpans,
    )
    from .patch_project_automation_config_batch_size_export_definition_log_traces import (
        PatchProjectAutomationConfigBatchSizeExportDefinitionLogTraces,
    )
    from .patch_project_automation_config_batch_size_format import PatchProjectAutomationConfigBatchSizeFormat
    from .patch_project_automation_config_btql_filter import PatchProjectAutomationConfigBtqlFilter
    from .patch_project_automation_config_btql_filter_action import (
        PatchProjectAutomationConfigBtqlFilterAction,
        PatchProjectAutomationConfigBtqlFilterAction_Slack,
        PatchProjectAutomationConfigBtqlFilterAction_Webhook,
    )
    from .patch_project_automation_config_btql_filter_action_slack import (
        PatchProjectAutomationConfigBtqlFilterActionSlack,
    )
    from .patch_project_automation_config_btql_filter_action_webhook import (
        PatchProjectAutomationConfigBtqlFilterActionWebhook,
    )
    from .patch_project_automation_config_btql_filter_event_type import PatchProjectAutomationConfigBtqlFilterEventType
    from .patch_project_automation_config_environment_filter import PatchProjectAutomationConfigEnvironmentFilter
    from .patch_project_automation_config_environment_filter_action import (
        PatchProjectAutomationConfigEnvironmentFilterAction,
        PatchProjectAutomationConfigEnvironmentFilterAction_Slack,
        PatchProjectAutomationConfigEnvironmentFilterAction_Webhook,
    )
    from .patch_project_automation_config_environment_filter_action_slack import (
        PatchProjectAutomationConfigEnvironmentFilterActionSlack,
    )
    from .patch_project_automation_config_environment_filter_action_webhook import (
        PatchProjectAutomationConfigEnvironmentFilterActionWebhook,
    )
    from .patch_project_automation_config_environment_filter_event_type import (
        PatchProjectAutomationConfigEnvironmentFilterEventType,
    )
    from .patch_project_automation_config_object_type import PatchProjectAutomationConfigObjectType
    from .patch_project_automation_config_object_type_event_type import PatchProjectAutomationConfigObjectTypeEventType
_dynamic_imports: typing.Dict[str, str] = {
    "GetProjectAutomationResponse": ".get_project_automation_response",
    "PatchProjectAutomationConfig": ".patch_project_automation_config",
    "PatchProjectAutomationConfigBatchSize": ".patch_project_automation_config_batch_size",
    "PatchProjectAutomationConfigBatchSizeCredentials": ".patch_project_automation_config_batch_size_credentials",
    "PatchProjectAutomationConfigBatchSizeCredentialsType": ".patch_project_automation_config_batch_size_credentials_type",
    "PatchProjectAutomationConfigBatchSizeEventType": ".patch_project_automation_config_batch_size_event_type",
    "PatchProjectAutomationConfigBatchSizeExportDefinition": ".patch_project_automation_config_batch_size_export_definition",
    "PatchProjectAutomationConfigBatchSizeExportDefinitionBtqlQuery": ".patch_project_automation_config_batch_size_export_definition_btql_query",
    "PatchProjectAutomationConfigBatchSizeExportDefinitionLogSpans": ".patch_project_automation_config_batch_size_export_definition_log_spans",
    "PatchProjectAutomationConfigBatchSizeExportDefinitionLogTraces": ".patch_project_automation_config_batch_size_export_definition_log_traces",
    "PatchProjectAutomationConfigBatchSizeExportDefinition_BtqlQuery": ".patch_project_automation_config_batch_size_export_definition",
    "PatchProjectAutomationConfigBatchSizeExportDefinition_LogSpans": ".patch_project_automation_config_batch_size_export_definition",
    "PatchProjectAutomationConfigBatchSizeExportDefinition_LogTraces": ".patch_project_automation_config_batch_size_export_definition",
    "PatchProjectAutomationConfigBatchSizeFormat": ".patch_project_automation_config_batch_size_format",
    "PatchProjectAutomationConfigBtqlFilter": ".patch_project_automation_config_btql_filter",
    "PatchProjectAutomationConfigBtqlFilterAction": ".patch_project_automation_config_btql_filter_action",
    "PatchProjectAutomationConfigBtqlFilterActionSlack": ".patch_project_automation_config_btql_filter_action_slack",
    "PatchProjectAutomationConfigBtqlFilterActionWebhook": ".patch_project_automation_config_btql_filter_action_webhook",
    "PatchProjectAutomationConfigBtqlFilterAction_Slack": ".patch_project_automation_config_btql_filter_action",
    "PatchProjectAutomationConfigBtqlFilterAction_Webhook": ".patch_project_automation_config_btql_filter_action",
    "PatchProjectAutomationConfigBtqlFilterEventType": ".patch_project_automation_config_btql_filter_event_type",
    "PatchProjectAutomationConfigEnvironmentFilter": ".patch_project_automation_config_environment_filter",
    "PatchProjectAutomationConfigEnvironmentFilterAction": ".patch_project_automation_config_environment_filter_action",
    "PatchProjectAutomationConfigEnvironmentFilterActionSlack": ".patch_project_automation_config_environment_filter_action_slack",
    "PatchProjectAutomationConfigEnvironmentFilterActionWebhook": ".patch_project_automation_config_environment_filter_action_webhook",
    "PatchProjectAutomationConfigEnvironmentFilterAction_Slack": ".patch_project_automation_config_environment_filter_action",
    "PatchProjectAutomationConfigEnvironmentFilterAction_Webhook": ".patch_project_automation_config_environment_filter_action",
    "PatchProjectAutomationConfigEnvironmentFilterEventType": ".patch_project_automation_config_environment_filter_event_type",
    "PatchProjectAutomationConfigObjectType": ".patch_project_automation_config_object_type",
    "PatchProjectAutomationConfigObjectTypeEventType": ".patch_project_automation_config_object_type_event_type",
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





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .templates_create_agents_from_template_no_project_request_initial_message_sequence_item import (
        TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItem,
    )
    from .templates_create_agents_from_template_no_project_request_initial_message_sequence_item_role import (
        TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItemRole,
    )
    from .templates_create_agents_from_template_no_project_response import (
        TemplatesCreateAgentsFromTemplateNoProjectResponse,
    )
    from .templates_create_agents_from_template_request_initial_message_sequence_item import (
        TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItem,
    )
    from .templates_create_agents_from_template_request_initial_message_sequence_item_role import (
        TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItemRole,
    )
    from .templates_create_template_no_project_request import (
        TemplatesCreateTemplateNoProjectRequest,
        TemplatesCreateTemplateNoProjectRequest_Agent,
        TemplatesCreateTemplateNoProjectRequest_AgentFile,
    )
    from .templates_create_template_no_project_request_agent import TemplatesCreateTemplateNoProjectRequestAgent
    from .templates_create_template_no_project_request_agent_file import (
        TemplatesCreateTemplateNoProjectRequestAgentFile,
    )
    from .templates_create_template_no_project_response import TemplatesCreateTemplateNoProjectResponse
    from .templates_create_template_request_body import (
        TemplatesCreateTemplateRequestBody,
        TemplatesCreateTemplateRequestBody_Agent,
        TemplatesCreateTemplateRequestBody_AgentFile,
    )
    from .templates_create_template_request_body_agent import TemplatesCreateTemplateRequestBodyAgent
    from .templates_create_template_request_body_agent_file import TemplatesCreateTemplateRequestBodyAgentFile
    from .templates_create_template_response import TemplatesCreateTemplateResponse
    from .templates_delete_template_no_project_response import TemplatesDeleteTemplateNoProjectResponse
    from .templates_delete_template_response import TemplatesDeleteTemplateResponse
    from .templates_fork_template_response import TemplatesForkTemplateResponse
    from .templates_get_template_snapshot_response import TemplatesGetTemplateSnapshotResponse
    from .templates_get_template_snapshot_response_agents_item import TemplatesGetTemplateSnapshotResponseAgentsItem
    from .templates_get_template_snapshot_response_agents_item_agent_type import (
        TemplatesGetTemplateSnapshotResponseAgentsItemAgentType,
    )
    from .templates_get_template_snapshot_response_agents_item_memory_variables import (
        TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariables,
    )
    from .templates_get_template_snapshot_response_agents_item_memory_variables_data_item import (
        TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariablesDataItem,
    )
    from .templates_get_template_snapshot_response_agents_item_properties import (
        TemplatesGetTemplateSnapshotResponseAgentsItemProperties,
    )
    from .templates_get_template_snapshot_response_agents_item_properties_reasoning_effort import (
        TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort,
    )
    from .templates_get_template_snapshot_response_agents_item_properties_verbosity_level import (
        TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesVerbosityLevel,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem,
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_Conditional,
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ConstrainChildTools,
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ContinueLoop,
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ExitLoop,
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_MaxCountPerStep,
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ParentLastTool,
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_RequiredBeforeExit,
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_RequiresApproval,
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_RunFirst,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_conditional import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConditional,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_constrain_child_tools import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConstrainChildTools,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_constrain_child_tools_child_arg_nodes_item import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConstrainChildToolsChildArgNodesItem,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_continue_loop import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemContinueLoop,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_exit_loop import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemExitLoop,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_max_count_per_step import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemMaxCountPerStep,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_parent_last_tool import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemParentLastTool,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_required_before_exit import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemRequiredBeforeExit,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_requires_approval import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemRequiresApproval,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_rules_item_run_first import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemRunFirst,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_variables import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolVariables,
    )
    from .templates_get_template_snapshot_response_agents_item_tool_variables_data_item import (
        TemplatesGetTemplateSnapshotResponseAgentsItemToolVariablesDataItem,
    )
    from .templates_get_template_snapshot_response_blocks_item import TemplatesGetTemplateSnapshotResponseBlocksItem
    from .templates_get_template_snapshot_response_configuration import (
        TemplatesGetTemplateSnapshotResponseConfiguration,
    )
    from .templates_get_template_snapshot_response_relationships_item import (
        TemplatesGetTemplateSnapshotResponseRelationshipsItem,
    )
    from .templates_get_template_snapshot_response_type import TemplatesGetTemplateSnapshotResponseType
    from .templates_legacy_migration_response import TemplatesLegacyMigrationResponse
    from .templates_list_template_versions_response import TemplatesListTemplateVersionsResponse
    from .templates_list_template_versions_response_versions_item import (
        TemplatesListTemplateVersionsResponseVersionsItem,
    )
    from .templates_list_templates_request_sort_by import TemplatesListTemplatesRequestSortBy
    from .templates_list_templates_response import TemplatesListTemplatesResponse
    from .templates_list_templates_response_templates_item import TemplatesListTemplatesResponseTemplatesItem
    from .templates_migrate_deployment_response import TemplatesMigrateDeploymentResponse
    from .templates_rename_template_response import TemplatesRenameTemplateResponse
    from .templates_save_template_version_request_block_reconciliation_strategy import (
        TemplatesSaveTemplateVersionRequestBlockReconciliationStrategy,
    )
    from .templates_save_template_version_response import TemplatesSaveTemplateVersionResponse
    from .templates_set_current_template_from_snapshot_response import TemplatesSetCurrentTemplateFromSnapshotResponse
    from .templates_update_current_template_from_agent_file_no_project_response import (
        TemplatesUpdateCurrentTemplateFromAgentFileNoProjectResponse,
    )
    from .templates_update_current_template_from_agent_file_response import (
        TemplatesUpdateCurrentTemplateFromAgentFileResponse,
    )
    from .templates_update_template_description_response import TemplatesUpdateTemplateDescriptionResponse
_dynamic_imports: typing.Dict[str, str] = {
    "TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItem": ".templates_create_agents_from_template_no_project_request_initial_message_sequence_item",
    "TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItemRole": ".templates_create_agents_from_template_no_project_request_initial_message_sequence_item_role",
    "TemplatesCreateAgentsFromTemplateNoProjectResponse": ".templates_create_agents_from_template_no_project_response",
    "TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItem": ".templates_create_agents_from_template_request_initial_message_sequence_item",
    "TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItemRole": ".templates_create_agents_from_template_request_initial_message_sequence_item_role",
    "TemplatesCreateTemplateNoProjectRequest": ".templates_create_template_no_project_request",
    "TemplatesCreateTemplateNoProjectRequestAgent": ".templates_create_template_no_project_request_agent",
    "TemplatesCreateTemplateNoProjectRequestAgentFile": ".templates_create_template_no_project_request_agent_file",
    "TemplatesCreateTemplateNoProjectRequest_Agent": ".templates_create_template_no_project_request",
    "TemplatesCreateTemplateNoProjectRequest_AgentFile": ".templates_create_template_no_project_request",
    "TemplatesCreateTemplateNoProjectResponse": ".templates_create_template_no_project_response",
    "TemplatesCreateTemplateRequestBody": ".templates_create_template_request_body",
    "TemplatesCreateTemplateRequestBodyAgent": ".templates_create_template_request_body_agent",
    "TemplatesCreateTemplateRequestBodyAgentFile": ".templates_create_template_request_body_agent_file",
    "TemplatesCreateTemplateRequestBody_Agent": ".templates_create_template_request_body",
    "TemplatesCreateTemplateRequestBody_AgentFile": ".templates_create_template_request_body",
    "TemplatesCreateTemplateResponse": ".templates_create_template_response",
    "TemplatesDeleteTemplateNoProjectResponse": ".templates_delete_template_no_project_response",
    "TemplatesDeleteTemplateResponse": ".templates_delete_template_response",
    "TemplatesForkTemplateResponse": ".templates_fork_template_response",
    "TemplatesGetTemplateSnapshotResponse": ".templates_get_template_snapshot_response",
    "TemplatesGetTemplateSnapshotResponseAgentsItem": ".templates_get_template_snapshot_response_agents_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemAgentType": ".templates_get_template_snapshot_response_agents_item_agent_type",
    "TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariables": ".templates_get_template_snapshot_response_agents_item_memory_variables",
    "TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariablesDataItem": ".templates_get_template_snapshot_response_agents_item_memory_variables_data_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemProperties": ".templates_get_template_snapshot_response_agents_item_properties",
    "TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort": ".templates_get_template_snapshot_response_agents_item_properties_reasoning_effort",
    "TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesVerbosityLevel": ".templates_get_template_snapshot_response_agents_item_properties_verbosity_level",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConditional": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_conditional",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConstrainChildTools": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_constrain_child_tools",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConstrainChildToolsChildArgNodesItem": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_constrain_child_tools_child_arg_nodes_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemContinueLoop": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_continue_loop",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemExitLoop": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_exit_loop",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemMaxCountPerStep": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_max_count_per_step",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemParentLastTool": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_parent_last_tool",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemRequiredBeforeExit": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_required_before_exit",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemRequiresApproval": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_requires_approval",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemRunFirst": ".templates_get_template_snapshot_response_agents_item_tool_rules_item_run_first",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_Conditional": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ConstrainChildTools": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ContinueLoop": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ExitLoop": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_MaxCountPerStep": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ParentLastTool": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_RequiredBeforeExit": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_RequiresApproval": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_RunFirst": ".templates_get_template_snapshot_response_agents_item_tool_rules_item",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolVariables": ".templates_get_template_snapshot_response_agents_item_tool_variables",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolVariablesDataItem": ".templates_get_template_snapshot_response_agents_item_tool_variables_data_item",
    "TemplatesGetTemplateSnapshotResponseBlocksItem": ".templates_get_template_snapshot_response_blocks_item",
    "TemplatesGetTemplateSnapshotResponseConfiguration": ".templates_get_template_snapshot_response_configuration",
    "TemplatesGetTemplateSnapshotResponseRelationshipsItem": ".templates_get_template_snapshot_response_relationships_item",
    "TemplatesGetTemplateSnapshotResponseType": ".templates_get_template_snapshot_response_type",
    "TemplatesLegacyMigrationResponse": ".templates_legacy_migration_response",
    "TemplatesListTemplateVersionsResponse": ".templates_list_template_versions_response",
    "TemplatesListTemplateVersionsResponseVersionsItem": ".templates_list_template_versions_response_versions_item",
    "TemplatesListTemplatesRequestSortBy": ".templates_list_templates_request_sort_by",
    "TemplatesListTemplatesResponse": ".templates_list_templates_response",
    "TemplatesListTemplatesResponseTemplatesItem": ".templates_list_templates_response_templates_item",
    "TemplatesMigrateDeploymentResponse": ".templates_migrate_deployment_response",
    "TemplatesRenameTemplateResponse": ".templates_rename_template_response",
    "TemplatesSaveTemplateVersionRequestBlockReconciliationStrategy": ".templates_save_template_version_request_block_reconciliation_strategy",
    "TemplatesSaveTemplateVersionResponse": ".templates_save_template_version_response",
    "TemplatesSetCurrentTemplateFromSnapshotResponse": ".templates_set_current_template_from_snapshot_response",
    "TemplatesUpdateCurrentTemplateFromAgentFileNoProjectResponse": ".templates_update_current_template_from_agent_file_no_project_response",
    "TemplatesUpdateCurrentTemplateFromAgentFileResponse": ".templates_update_current_template_from_agent_file_response",
    "TemplatesUpdateTemplateDescriptionResponse": ".templates_update_template_description_response",
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
    "TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItem",
    "TemplatesCreateAgentsFromTemplateNoProjectRequestInitialMessageSequenceItemRole",
    "TemplatesCreateAgentsFromTemplateNoProjectResponse",
    "TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItem",
    "TemplatesCreateAgentsFromTemplateRequestInitialMessageSequenceItemRole",
    "TemplatesCreateTemplateNoProjectRequest",
    "TemplatesCreateTemplateNoProjectRequestAgent",
    "TemplatesCreateTemplateNoProjectRequestAgentFile",
    "TemplatesCreateTemplateNoProjectRequest_Agent",
    "TemplatesCreateTemplateNoProjectRequest_AgentFile",
    "TemplatesCreateTemplateNoProjectResponse",
    "TemplatesCreateTemplateRequestBody",
    "TemplatesCreateTemplateRequestBodyAgent",
    "TemplatesCreateTemplateRequestBodyAgentFile",
    "TemplatesCreateTemplateRequestBody_Agent",
    "TemplatesCreateTemplateRequestBody_AgentFile",
    "TemplatesCreateTemplateResponse",
    "TemplatesDeleteTemplateNoProjectResponse",
    "TemplatesDeleteTemplateResponse",
    "TemplatesForkTemplateResponse",
    "TemplatesGetTemplateSnapshotResponse",
    "TemplatesGetTemplateSnapshotResponseAgentsItem",
    "TemplatesGetTemplateSnapshotResponseAgentsItemAgentType",
    "TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariables",
    "TemplatesGetTemplateSnapshotResponseAgentsItemMemoryVariablesDataItem",
    "TemplatesGetTemplateSnapshotResponseAgentsItemProperties",
    "TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesReasoningEffort",
    "TemplatesGetTemplateSnapshotResponseAgentsItemPropertiesVerbosityLevel",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConditional",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConstrainChildTools",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemConstrainChildToolsChildArgNodesItem",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemContinueLoop",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemExitLoop",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemMaxCountPerStep",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemParentLastTool",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemRequiredBeforeExit",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemRequiresApproval",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItemRunFirst",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_Conditional",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ConstrainChildTools",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ContinueLoop",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ExitLoop",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_MaxCountPerStep",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_ParentLastTool",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_RequiredBeforeExit",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_RequiresApproval",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolRulesItem_RunFirst",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolVariables",
    "TemplatesGetTemplateSnapshotResponseAgentsItemToolVariablesDataItem",
    "TemplatesGetTemplateSnapshotResponseBlocksItem",
    "TemplatesGetTemplateSnapshotResponseConfiguration",
    "TemplatesGetTemplateSnapshotResponseRelationshipsItem",
    "TemplatesGetTemplateSnapshotResponseType",
    "TemplatesLegacyMigrationResponse",
    "TemplatesListTemplateVersionsResponse",
    "TemplatesListTemplateVersionsResponseVersionsItem",
    "TemplatesListTemplatesRequestSortBy",
    "TemplatesListTemplatesResponse",
    "TemplatesListTemplatesResponseTemplatesItem",
    "TemplatesMigrateDeploymentResponse",
    "TemplatesRenameTemplateResponse",
    "TemplatesSaveTemplateVersionRequestBlockReconciliationStrategy",
    "TemplatesSaveTemplateVersionResponse",
    "TemplatesSetCurrentTemplateFromSnapshotResponse",
    "TemplatesUpdateCurrentTemplateFromAgentFileNoProjectResponse",
    "TemplatesUpdateCurrentTemplateFromAgentFileResponse",
    "TemplatesUpdateTemplateDescriptionResponse",
]

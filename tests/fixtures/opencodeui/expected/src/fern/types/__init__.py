



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .agent import Agent
    from .agent_config import AgentConfig
    from .agent_config_mode import AgentConfigMode
    from .agent_mode import AgentMode
    from .agent_model import AgentModel
    from .agent_part import AgentPart
    from .agent_part_input import AgentPartInput
    from .agent_part_input_source import AgentPartInputSource
    from .agent_part_source import AgentPartSource
    from .api_auth import ApiAuth
    from .api_error import ApiError
    from .api_error_data import ApiErrorData
    from .api_error_name import ApiErrorName
    from .app_log_request_level import AppLogRequestLevel
    from .app_skills_response_item import AppSkillsResponseItem
    from .assistant_message import AssistantMessage
    from .assistant_message_error import (
        AssistantMessageError,
        AssistantMessageError_ApiError,
        AssistantMessageError_MessageAbortedError,
        AssistantMessageError_MessageOutputLengthError,
        AssistantMessageError_ProviderAuthError,
        AssistantMessageError_UnknownError,
    )
    from .assistant_message_path import AssistantMessagePath
    from .assistant_message_role import AssistantMessageRole
    from .assistant_message_time import AssistantMessageTime
    from .assistant_message_tokens import AssistantMessageTokens
    from .assistant_message_tokens_cache import AssistantMessageTokensCache
    from .auth import Auth, Auth_Api, Auth_Oauth, Auth_Wellknown
    from .bad_request_error_body import BadRequestErrorBody
    from .command import Command
    from .command_source import CommandSource
    from .compaction_part import CompactionPart
    from .config import Config
    from .config_agent import ConfigAgent
    from .config_autoupdate import ConfigAutoupdate
    from .config_autoupdate_one import ConfigAutoupdateOne
    from .config_command_value import ConfigCommandValue
    from .config_compaction import ConfigCompaction
    from .config_enterprise import ConfigEnterprise
    from .config_experimental import ConfigExperimental
    from .config_formatter import ConfigFormatter
    from .config_formatter_one_value import ConfigFormatterOneValue
    from .config_lsp import ConfigLsp
    from .config_lsp_one_value import ConfigLspOneValue
    from .config_lsp_one_value_command import ConfigLspOneValueCommand
    from .config_lsp_one_value_zero import ConfigLspOneValueZero
    from .config_mcp_value import ConfigMcpValue
    from .config_mcp_value_enabled import ConfigMcpValueEnabled
    from .config_mcp_value_zero import ConfigMcpValueZero, ConfigMcpValueZero_Local, ConfigMcpValueZero_Remote
    from .config_mode import ConfigMode
    from .config_providers_response import ConfigProvidersResponse
    from .config_share import ConfigShare
    from .config_skills import ConfigSkills
    from .config_tui import ConfigTui
    from .config_tui_diff_style import ConfigTuiDiffStyle
    from .config_tui_scroll_acceleration import ConfigTuiScrollAcceleration
    from .config_watcher import ConfigWatcher
    from .event import (
        Event,
        Event_CommandExecuted,
        Event_FileEdited,
        Event_FileWatcherUpdated,
        Event_GlobalDisposed,
        Event_InstallationUpdateAvailable,
        Event_InstallationUpdated,
        Event_LspClientDiagnostics,
        Event_LspUpdated,
        Event_McpBrowserOpenFailed,
        Event_McpToolsChanged,
        Event_MessagePartRemoved,
        Event_MessagePartUpdated,
        Event_MessageRemoved,
        Event_MessageUpdated,
        Event_PermissionAsked,
        Event_PermissionReplied,
        Event_ProjectUpdated,
        Event_PtyCreated,
        Event_PtyDeleted,
        Event_PtyExited,
        Event_PtyUpdated,
        Event_QuestionAsked,
        Event_QuestionRejected,
        Event_QuestionReplied,
        Event_ServerConnected,
        Event_ServerInstanceDisposed,
        Event_SessionCompacted,
        Event_SessionCreated,
        Event_SessionDeleted,
        Event_SessionDiff,
        Event_SessionError,
        Event_SessionIdle,
        Event_SessionStatus,
        Event_SessionUpdated,
        Event_TodoUpdated,
        Event_TuiCommandExecute,
        Event_TuiPromptAppend,
        Event_TuiSessionSelect,
        Event_TuiToastShow,
        Event_VcsBranchUpdated,
        Event_WorktreeFailed,
        Event_WorktreeReady,
    )
    from .event_command_executed import EventCommandExecuted
    from .event_command_executed_properties import EventCommandExecutedProperties
    from .event_file_edited import EventFileEdited
    from .event_file_edited_properties import EventFileEditedProperties
    from .event_file_watcher_updated import EventFileWatcherUpdated
    from .event_file_watcher_updated_properties import EventFileWatcherUpdatedProperties
    from .event_file_watcher_updated_properties_event import EventFileWatcherUpdatedPropertiesEvent
    from .event_file_watcher_updated_properties_event_one import EventFileWatcherUpdatedPropertiesEventOne
    from .event_file_watcher_updated_properties_event_two import EventFileWatcherUpdatedPropertiesEventTwo
    from .event_file_watcher_updated_properties_event_zero import EventFileWatcherUpdatedPropertiesEventZero
    from .event_global_disposed import EventGlobalDisposed
    from .event_global_disposed_properties import EventGlobalDisposedProperties
    from .event_installation_update_available import EventInstallationUpdateAvailable
    from .event_installation_update_available_properties import EventInstallationUpdateAvailableProperties
    from .event_installation_updated import EventInstallationUpdated
    from .event_installation_updated_properties import EventInstallationUpdatedProperties
    from .event_lsp_client_diagnostics import EventLspClientDiagnostics
    from .event_lsp_client_diagnostics_properties import EventLspClientDiagnosticsProperties
    from .event_lsp_updated import EventLspUpdated
    from .event_lsp_updated_properties import EventLspUpdatedProperties
    from .event_mcp_browser_open_failed import EventMcpBrowserOpenFailed
    from .event_mcp_browser_open_failed_properties import EventMcpBrowserOpenFailedProperties
    from .event_mcp_tools_changed import EventMcpToolsChanged
    from .event_mcp_tools_changed_properties import EventMcpToolsChangedProperties
    from .event_message_part_removed import EventMessagePartRemoved
    from .event_message_part_removed_properties import EventMessagePartRemovedProperties
    from .event_message_part_updated import EventMessagePartUpdated
    from .event_message_part_updated_properties import EventMessagePartUpdatedProperties
    from .event_message_removed import EventMessageRemoved
    from .event_message_removed_properties import EventMessageRemovedProperties
    from .event_message_updated import EventMessageUpdated
    from .event_message_updated_properties import EventMessageUpdatedProperties
    from .event_permission_asked import EventPermissionAsked
    from .event_permission_replied import EventPermissionReplied
    from .event_permission_replied_properties import EventPermissionRepliedProperties
    from .event_permission_replied_properties_reply import EventPermissionRepliedPropertiesReply
    from .event_project_updated import EventProjectUpdated
    from .event_pty_created import EventPtyCreated
    from .event_pty_created_properties import EventPtyCreatedProperties
    from .event_pty_deleted import EventPtyDeleted
    from .event_pty_deleted_properties import EventPtyDeletedProperties
    from .event_pty_exited import EventPtyExited
    from .event_pty_exited_properties import EventPtyExitedProperties
    from .event_pty_updated import EventPtyUpdated
    from .event_pty_updated_properties import EventPtyUpdatedProperties
    from .event_question_asked import EventQuestionAsked
    from .event_question_rejected import EventQuestionRejected
    from .event_question_rejected_properties import EventQuestionRejectedProperties
    from .event_question_replied import EventQuestionReplied
    from .event_question_replied_properties import EventQuestionRepliedProperties
    from .event_server_connected import EventServerConnected
    from .event_server_connected_properties import EventServerConnectedProperties
    from .event_server_instance_disposed import EventServerInstanceDisposed
    from .event_server_instance_disposed_properties import EventServerInstanceDisposedProperties
    from .event_session_compacted import EventSessionCompacted
    from .event_session_compacted_properties import EventSessionCompactedProperties
    from .event_session_created import EventSessionCreated
    from .event_session_created_properties import EventSessionCreatedProperties
    from .event_session_deleted import EventSessionDeleted
    from .event_session_deleted_properties import EventSessionDeletedProperties
    from .event_session_diff import EventSessionDiff
    from .event_session_diff_properties import EventSessionDiffProperties
    from .event_session_error import EventSessionError
    from .event_session_error_properties import EventSessionErrorProperties
    from .event_session_error_properties_error import (
        EventSessionErrorPropertiesError,
        EventSessionErrorPropertiesError_ApiError,
        EventSessionErrorPropertiesError_MessageAbortedError,
        EventSessionErrorPropertiesError_MessageOutputLengthError,
        EventSessionErrorPropertiesError_ProviderAuthError,
        EventSessionErrorPropertiesError_UnknownError,
    )
    from .event_session_idle import EventSessionIdle
    from .event_session_idle_properties import EventSessionIdleProperties
    from .event_session_status import EventSessionStatus
    from .event_session_status_properties import EventSessionStatusProperties
    from .event_session_updated import EventSessionUpdated
    from .event_session_updated_properties import EventSessionUpdatedProperties
    from .event_todo_updated import EventTodoUpdated
    from .event_todo_updated_properties import EventTodoUpdatedProperties
    from .event_tui_command_execute import EventTuiCommandExecute
    from .event_tui_command_execute_properties import EventTuiCommandExecuteProperties
    from .event_tui_command_execute_properties_command import EventTuiCommandExecutePropertiesCommand
    from .event_tui_command_execute_properties_command_zero import EventTuiCommandExecutePropertiesCommandZero
    from .event_tui_prompt_append import EventTuiPromptAppend
    from .event_tui_prompt_append_properties import EventTuiPromptAppendProperties
    from .event_tui_session_select import EventTuiSessionSelect
    from .event_tui_session_select_properties import EventTuiSessionSelectProperties
    from .event_tui_toast_show import EventTuiToastShow
    from .event_tui_toast_show_properties import EventTuiToastShowProperties
    from .event_tui_toast_show_properties_variant import EventTuiToastShowPropertiesVariant
    from .event_vcs_branch_updated import EventVcsBranchUpdated
    from .event_vcs_branch_updated_properties import EventVcsBranchUpdatedProperties
    from .event_worktree_failed import EventWorktreeFailed
    from .event_worktree_failed_properties import EventWorktreeFailedProperties
    from .event_worktree_ready import EventWorktreeReady
    from .event_worktree_ready_properties import EventWorktreeReadyProperties
    from .file import File
    from .file_content import FileContent
    from .file_content_encoding import FileContentEncoding
    from .file_content_patch import FileContentPatch
    from .file_content_patch_hunks_item import FileContentPatchHunksItem
    from .file_content_type import FileContentType
    from .file_diff import FileDiff
    from .file_node import FileNode
    from .file_node_type import FileNodeType
    from .file_part import FilePart
    from .file_part_input import FilePartInput
    from .file_part_source import FilePartSource, FilePartSource_File, FilePartSource_Resource, FilePartSource_Symbol
    from .file_part_source_text import FilePartSourceText
    from .file_part_type import FilePartType
    from .file_source import FileSource
    from .file_status import FileStatus
    from .find_files_request_dirs import FindFilesRequestDirs
    from .find_files_request_type import FindFilesRequestType
    from .find_text_response_item import FindTextResponseItem
    from .find_text_response_item_lines import FindTextResponseItemLines
    from .find_text_response_item_path import FindTextResponseItemPath
    from .find_text_response_item_submatches_item import FindTextResponseItemSubmatchesItem
    from .find_text_response_item_submatches_item_match import FindTextResponseItemSubmatchesItemMatch
    from .formatter_status import FormatterStatus
    from .global_event import GlobalEvent
    from .global_health_response import GlobalHealthResponse
    from .keybinds_config import KeybindsConfig
    from .layout_config import LayoutConfig
    from .log_level import LogLevel
    from .lsp_status import LspStatus
    from .lsp_status_status import LspStatusStatus
    from .lsp_status_status_one import LspStatusStatusOne
    from .lsp_status_status_zero import LspStatusStatusZero
    from .mcp_add_request_config import McpAddRequestConfig, McpAddRequestConfig_Local, McpAddRequestConfig_Remote
    from .mcp_auth_remove_response import McpAuthRemoveResponse
    from .mcp_auth_start_response import McpAuthStartResponse
    from .mcp_local_config import McpLocalConfig
    from .mcp_o_auth_config import McpOAuthConfig
    from .mcp_remote_config import McpRemoteConfig
    from .mcp_remote_config_oauth import McpRemoteConfigOauth
    from .mcp_resource import McpResource
    from .mcp_status import (
        McpStatus,
        McpStatus_Connected,
        McpStatus_Disabled,
        McpStatus_Failed,
        McpStatus_NeedsAuth,
        McpStatus_NeedsClientRegistration,
    )
    from .mcp_status_connected import McpStatusConnected
    from .mcp_status_disabled import McpStatusDisabled
    from .mcp_status_failed import McpStatusFailed
    from .mcp_status_needs_auth import McpStatusNeedsAuth
    from .mcp_status_needs_client_registration import McpStatusNeedsClientRegistration
    from .message import Message, Message_Assistant, Message_User
    from .message_aborted_error import MessageAbortedError
    from .message_aborted_error_data import MessageAbortedErrorData
    from .message_output_length_error import MessageOutputLengthError
    from .message_output_length_error_data import MessageOutputLengthErrorData
    from .model import Model
    from .model_api import ModelApi
    from .model_capabilities import ModelCapabilities
    from .model_capabilities_input import ModelCapabilitiesInput
    from .model_capabilities_interleaved import ModelCapabilitiesInterleaved
    from .model_capabilities_interleaved_field import ModelCapabilitiesInterleavedField
    from .model_capabilities_interleaved_field_field import ModelCapabilitiesInterleavedFieldField
    from .model_capabilities_output import ModelCapabilitiesOutput
    from .model_cost import ModelCost
    from .model_cost_cache import ModelCostCache
    from .model_cost_experimental_over200k import ModelCostExperimentalOver200K
    from .model_cost_experimental_over200k_cache import ModelCostExperimentalOver200KCache
    from .model_limit import ModelLimit
    from .model_status import ModelStatus
    from .not_found_error_body import NotFoundErrorBody
    from .not_found_error_body_data import NotFoundErrorBodyData
    from .not_found_error_body_name import NotFoundErrorBodyName
    from .o_auth import OAuth
    from .part import (
        Part,
        Part_Agent,
        Part_Compaction,
        Part_File,
        Part_Patch,
        Part_Reasoning,
        Part_Retry,
        Part_Snapshot,
        Part_StepFinish,
        Part_StepStart,
        Part_Subtask,
        Part_Text,
        Part_Tool,
    )
    from .patch_part import PatchPart
    from .path import Path
    from .permission_action import PermissionAction
    from .permission_action_config import PermissionActionConfig
    from .permission_config import PermissionConfig
    from .permission_config_original_keys import PermissionConfigOriginalKeys
    from .permission_object_config import PermissionObjectConfig
    from .permission_reply_request_reply import PermissionReplyRequestReply
    from .permission_request import PermissionRequest
    from .permission_request_tool import PermissionRequestTool
    from .permission_respond_request_response import PermissionRespondRequestResponse
    from .permission_rule import PermissionRule
    from .permission_rule_config import PermissionRuleConfig
    from .permission_ruleset import PermissionRuleset
    from .project import Project
    from .project_commands import ProjectCommands
    from .project_icon import ProjectIcon
    from .project_time import ProjectTime
    from .project_update_request_commands import ProjectUpdateRequestCommands
    from .project_update_request_icon import ProjectUpdateRequestIcon
    from .project_vcs import ProjectVcs
    from .provider import Provider
    from .provider_auth_authorization import ProviderAuthAuthorization
    from .provider_auth_authorization_method import ProviderAuthAuthorizationMethod
    from .provider_auth_authorization_method_one import ProviderAuthAuthorizationMethodOne
    from .provider_auth_authorization_method_zero import ProviderAuthAuthorizationMethodZero
    from .provider_auth_error import ProviderAuthError
    from .provider_auth_error_data import ProviderAuthErrorData
    from .provider_auth_method import ProviderAuthMethod
    from .provider_auth_method_type import ProviderAuthMethodType
    from .provider_auth_method_type_one import ProviderAuthMethodTypeOne
    from .provider_auth_method_type_zero import ProviderAuthMethodTypeZero
    from .provider_config import ProviderConfig
    from .provider_config_models_value import ProviderConfigModelsValue
    from .provider_config_models_value_cost import ProviderConfigModelsValueCost
    from .provider_config_models_value_cost_context_over200k import ProviderConfigModelsValueCostContextOver200K
    from .provider_config_models_value_interleaved import ProviderConfigModelsValueInterleaved
    from .provider_config_models_value_interleaved_field import ProviderConfigModelsValueInterleavedField
    from .provider_config_models_value_interleaved_field_field import ProviderConfigModelsValueInterleavedFieldField
    from .provider_config_models_value_limit import ProviderConfigModelsValueLimit
    from .provider_config_models_value_modalities import ProviderConfigModelsValueModalities
    from .provider_config_models_value_modalities_input_item import ProviderConfigModelsValueModalitiesInputItem
    from .provider_config_models_value_modalities_output_item import ProviderConfigModelsValueModalitiesOutputItem
    from .provider_config_models_value_provider import ProviderConfigModelsValueProvider
    from .provider_config_models_value_status import ProviderConfigModelsValueStatus
    from .provider_config_models_value_variants_value import ProviderConfigModelsValueVariantsValue
    from .provider_config_options import ProviderConfigOptions
    from .provider_config_options_timeout import ProviderConfigOptionsTimeout
    from .provider_list_response import ProviderListResponse
    from .provider_list_response_all_item import ProviderListResponseAllItem
    from .provider_list_response_all_item_models_value import ProviderListResponseAllItemModelsValue
    from .provider_list_response_all_item_models_value_cost import ProviderListResponseAllItemModelsValueCost
    from .provider_list_response_all_item_models_value_cost_context_over200k import (
        ProviderListResponseAllItemModelsValueCostContextOver200K,
    )
    from .provider_list_response_all_item_models_value_interleaved import (
        ProviderListResponseAllItemModelsValueInterleaved,
    )
    from .provider_list_response_all_item_models_value_interleaved_field import (
        ProviderListResponseAllItemModelsValueInterleavedField,
    )
    from .provider_list_response_all_item_models_value_interleaved_field_field import (
        ProviderListResponseAllItemModelsValueInterleavedFieldField,
    )
    from .provider_list_response_all_item_models_value_limit import ProviderListResponseAllItemModelsValueLimit
    from .provider_list_response_all_item_models_value_modalities import (
        ProviderListResponseAllItemModelsValueModalities,
    )
    from .provider_list_response_all_item_models_value_modalities_input_item import (
        ProviderListResponseAllItemModelsValueModalitiesInputItem,
    )
    from .provider_list_response_all_item_models_value_modalities_output_item import (
        ProviderListResponseAllItemModelsValueModalitiesOutputItem,
    )
    from .provider_list_response_all_item_models_value_provider import ProviderListResponseAllItemModelsValueProvider
    from .provider_list_response_all_item_models_value_status import ProviderListResponseAllItemModelsValueStatus
    from .provider_source import ProviderSource
    from .pty import Pty
    from .pty_status import PtyStatus
    from .pty_update_request_size import PtyUpdateRequestSize
    from .question_answer import QuestionAnswer
    from .question_info import QuestionInfo
    from .question_option import QuestionOption
    from .question_request import QuestionRequest
    from .question_request_tool import QuestionRequestTool
    from .range import Range
    from .range_end import RangeEnd
    from .range_start import RangeStart
    from .reasoning_part import ReasoningPart
    from .reasoning_part_time import ReasoningPartTime
    from .resource_source import ResourceSource
    from .retry_part import RetryPart
    from .retry_part_time import RetryPartTime
    from .server_config import ServerConfig
    from .session import Session
    from .session_command_request_parts_item import SessionCommandRequestPartsItem
    from .session_command_request_parts_item_type import SessionCommandRequestPartsItemType
    from .session_command_response import SessionCommandResponse
    from .session_message_response import SessionMessageResponse
    from .session_messages_response_item import SessionMessagesResponseItem
    from .session_prompt_async_request_model import SessionPromptAsyncRequestModel
    from .session_prompt_async_request_parts_item import (
        SessionPromptAsyncRequestPartsItem,
        SessionPromptAsyncRequestPartsItem_Agent,
        SessionPromptAsyncRequestPartsItem_File,
        SessionPromptAsyncRequestPartsItem_Subtask,
        SessionPromptAsyncRequestPartsItem_Text,
    )
    from .session_prompt_request_model import SessionPromptRequestModel
    from .session_prompt_request_parts_item import (
        SessionPromptRequestPartsItem,
        SessionPromptRequestPartsItem_Agent,
        SessionPromptRequestPartsItem_File,
        SessionPromptRequestPartsItem_Subtask,
        SessionPromptRequestPartsItem_Text,
    )
    from .session_prompt_response import SessionPromptResponse
    from .session_revert import SessionRevert
    from .session_share import SessionShare
    from .session_shell_request_model import SessionShellRequestModel
    from .session_status import SessionStatus, SessionStatus_Busy, SessionStatus_Idle, SessionStatus_Retry
    from .session_status_busy import SessionStatusBusy
    from .session_status_idle import SessionStatusIdle
    from .session_status_retry import SessionStatusRetry
    from .session_summary import SessionSummary
    from .session_time import SessionTime
    from .session_update_request_time import SessionUpdateRequestTime
    from .snapshot_part import SnapshotPart
    from .step_finish_part import StepFinishPart
    from .step_finish_part_tokens import StepFinishPartTokens
    from .step_finish_part_tokens_cache import StepFinishPartTokensCache
    from .step_start_part import StepStartPart
    from .subtask_part import SubtaskPart
    from .subtask_part_input import SubtaskPartInput
    from .subtask_part_input_model import SubtaskPartInputModel
    from .subtask_part_model import SubtaskPartModel
    from .symbol import Symbol
    from .symbol_location import SymbolLocation
    from .symbol_source import SymbolSource
    from .text_part import TextPart
    from .text_part_input import TextPartInput
    from .text_part_input_time import TextPartInputTime
    from .text_part_time import TextPartTime
    from .todo import Todo
    from .tool_i_ds import ToolIDs
    from .tool_list import ToolList
    from .tool_list_item import ToolListItem
    from .tool_part import ToolPart
    from .tool_state import ToolState, ToolState_Completed, ToolState_Error, ToolState_Pending, ToolState_Running
    from .tool_state_completed import ToolStateCompleted
    from .tool_state_completed_time import ToolStateCompletedTime
    from .tool_state_error import ToolStateError
    from .tool_state_error_time import ToolStateErrorTime
    from .tool_state_pending import ToolStatePending
    from .tool_state_running import ToolStateRunning
    from .tool_state_running_time import ToolStateRunningTime
    from .tui_control_next_response import TuiControlNextResponse
    from .tui_publish_request_body import (
        TuiPublishRequestBody,
        TuiPublishRequestBody_TuiCommandExecute,
        TuiPublishRequestBody_TuiPromptAppend,
        TuiPublishRequestBody_TuiSessionSelect,
        TuiPublishRequestBody_TuiToastShow,
    )
    from .tui_show_toast_request_variant import TuiShowToastRequestVariant
    from .unknown_error import UnknownError
    from .unknown_error_data import UnknownErrorData
    from .user_message import UserMessage
    from .user_message_model import UserMessageModel
    from .user_message_summary import UserMessageSummary
    from .user_message_time import UserMessageTime
    from .vcs_info import VcsInfo
    from .well_known_auth import WellKnownAuth
    from .worktree import Worktree
_dynamic_imports: typing.Dict[str, str] = {
    "Agent": ".agent",
    "AgentConfig": ".agent_config",
    "AgentConfigMode": ".agent_config_mode",
    "AgentMode": ".agent_mode",
    "AgentModel": ".agent_model",
    "AgentPart": ".agent_part",
    "AgentPartInput": ".agent_part_input",
    "AgentPartInputSource": ".agent_part_input_source",
    "AgentPartSource": ".agent_part_source",
    "ApiAuth": ".api_auth",
    "ApiError": ".api_error",
    "ApiErrorData": ".api_error_data",
    "ApiErrorName": ".api_error_name",
    "AppLogRequestLevel": ".app_log_request_level",
    "AppSkillsResponseItem": ".app_skills_response_item",
    "AssistantMessage": ".assistant_message",
    "AssistantMessageError": ".assistant_message_error",
    "AssistantMessageError_ApiError": ".assistant_message_error",
    "AssistantMessageError_MessageAbortedError": ".assistant_message_error",
    "AssistantMessageError_MessageOutputLengthError": ".assistant_message_error",
    "AssistantMessageError_ProviderAuthError": ".assistant_message_error",
    "AssistantMessageError_UnknownError": ".assistant_message_error",
    "AssistantMessagePath": ".assistant_message_path",
    "AssistantMessageRole": ".assistant_message_role",
    "AssistantMessageTime": ".assistant_message_time",
    "AssistantMessageTokens": ".assistant_message_tokens",
    "AssistantMessageTokensCache": ".assistant_message_tokens_cache",
    "Auth": ".auth",
    "Auth_Api": ".auth",
    "Auth_Oauth": ".auth",
    "Auth_Wellknown": ".auth",
    "BadRequestErrorBody": ".bad_request_error_body",
    "Command": ".command",
    "CommandSource": ".command_source",
    "CompactionPart": ".compaction_part",
    "Config": ".config",
    "ConfigAgent": ".config_agent",
    "ConfigAutoupdate": ".config_autoupdate",
    "ConfigAutoupdateOne": ".config_autoupdate_one",
    "ConfigCommandValue": ".config_command_value",
    "ConfigCompaction": ".config_compaction",
    "ConfigEnterprise": ".config_enterprise",
    "ConfigExperimental": ".config_experimental",
    "ConfigFormatter": ".config_formatter",
    "ConfigFormatterOneValue": ".config_formatter_one_value",
    "ConfigLsp": ".config_lsp",
    "ConfigLspOneValue": ".config_lsp_one_value",
    "ConfigLspOneValueCommand": ".config_lsp_one_value_command",
    "ConfigLspOneValueZero": ".config_lsp_one_value_zero",
    "ConfigMcpValue": ".config_mcp_value",
    "ConfigMcpValueEnabled": ".config_mcp_value_enabled",
    "ConfigMcpValueZero": ".config_mcp_value_zero",
    "ConfigMcpValueZero_Local": ".config_mcp_value_zero",
    "ConfigMcpValueZero_Remote": ".config_mcp_value_zero",
    "ConfigMode": ".config_mode",
    "ConfigProvidersResponse": ".config_providers_response",
    "ConfigShare": ".config_share",
    "ConfigSkills": ".config_skills",
    "ConfigTui": ".config_tui",
    "ConfigTuiDiffStyle": ".config_tui_diff_style",
    "ConfigTuiScrollAcceleration": ".config_tui_scroll_acceleration",
    "ConfigWatcher": ".config_watcher",
    "Event": ".event",
    "EventCommandExecuted": ".event_command_executed",
    "EventCommandExecutedProperties": ".event_command_executed_properties",
    "EventFileEdited": ".event_file_edited",
    "EventFileEditedProperties": ".event_file_edited_properties",
    "EventFileWatcherUpdated": ".event_file_watcher_updated",
    "EventFileWatcherUpdatedProperties": ".event_file_watcher_updated_properties",
    "EventFileWatcherUpdatedPropertiesEvent": ".event_file_watcher_updated_properties_event",
    "EventFileWatcherUpdatedPropertiesEventOne": ".event_file_watcher_updated_properties_event_one",
    "EventFileWatcherUpdatedPropertiesEventTwo": ".event_file_watcher_updated_properties_event_two",
    "EventFileWatcherUpdatedPropertiesEventZero": ".event_file_watcher_updated_properties_event_zero",
    "EventGlobalDisposed": ".event_global_disposed",
    "EventGlobalDisposedProperties": ".event_global_disposed_properties",
    "EventInstallationUpdateAvailable": ".event_installation_update_available",
    "EventInstallationUpdateAvailableProperties": ".event_installation_update_available_properties",
    "EventInstallationUpdated": ".event_installation_updated",
    "EventInstallationUpdatedProperties": ".event_installation_updated_properties",
    "EventLspClientDiagnostics": ".event_lsp_client_diagnostics",
    "EventLspClientDiagnosticsProperties": ".event_lsp_client_diagnostics_properties",
    "EventLspUpdated": ".event_lsp_updated",
    "EventLspUpdatedProperties": ".event_lsp_updated_properties",
    "EventMcpBrowserOpenFailed": ".event_mcp_browser_open_failed",
    "EventMcpBrowserOpenFailedProperties": ".event_mcp_browser_open_failed_properties",
    "EventMcpToolsChanged": ".event_mcp_tools_changed",
    "EventMcpToolsChangedProperties": ".event_mcp_tools_changed_properties",
    "EventMessagePartRemoved": ".event_message_part_removed",
    "EventMessagePartRemovedProperties": ".event_message_part_removed_properties",
    "EventMessagePartUpdated": ".event_message_part_updated",
    "EventMessagePartUpdatedProperties": ".event_message_part_updated_properties",
    "EventMessageRemoved": ".event_message_removed",
    "EventMessageRemovedProperties": ".event_message_removed_properties",
    "EventMessageUpdated": ".event_message_updated",
    "EventMessageUpdatedProperties": ".event_message_updated_properties",
    "EventPermissionAsked": ".event_permission_asked",
    "EventPermissionReplied": ".event_permission_replied",
    "EventPermissionRepliedProperties": ".event_permission_replied_properties",
    "EventPermissionRepliedPropertiesReply": ".event_permission_replied_properties_reply",
    "EventProjectUpdated": ".event_project_updated",
    "EventPtyCreated": ".event_pty_created",
    "EventPtyCreatedProperties": ".event_pty_created_properties",
    "EventPtyDeleted": ".event_pty_deleted",
    "EventPtyDeletedProperties": ".event_pty_deleted_properties",
    "EventPtyExited": ".event_pty_exited",
    "EventPtyExitedProperties": ".event_pty_exited_properties",
    "EventPtyUpdated": ".event_pty_updated",
    "EventPtyUpdatedProperties": ".event_pty_updated_properties",
    "EventQuestionAsked": ".event_question_asked",
    "EventQuestionRejected": ".event_question_rejected",
    "EventQuestionRejectedProperties": ".event_question_rejected_properties",
    "EventQuestionReplied": ".event_question_replied",
    "EventQuestionRepliedProperties": ".event_question_replied_properties",
    "EventServerConnected": ".event_server_connected",
    "EventServerConnectedProperties": ".event_server_connected_properties",
    "EventServerInstanceDisposed": ".event_server_instance_disposed",
    "EventServerInstanceDisposedProperties": ".event_server_instance_disposed_properties",
    "EventSessionCompacted": ".event_session_compacted",
    "EventSessionCompactedProperties": ".event_session_compacted_properties",
    "EventSessionCreated": ".event_session_created",
    "EventSessionCreatedProperties": ".event_session_created_properties",
    "EventSessionDeleted": ".event_session_deleted",
    "EventSessionDeletedProperties": ".event_session_deleted_properties",
    "EventSessionDiff": ".event_session_diff",
    "EventSessionDiffProperties": ".event_session_diff_properties",
    "EventSessionError": ".event_session_error",
    "EventSessionErrorProperties": ".event_session_error_properties",
    "EventSessionErrorPropertiesError": ".event_session_error_properties_error",
    "EventSessionErrorPropertiesError_ApiError": ".event_session_error_properties_error",
    "EventSessionErrorPropertiesError_MessageAbortedError": ".event_session_error_properties_error",
    "EventSessionErrorPropertiesError_MessageOutputLengthError": ".event_session_error_properties_error",
    "EventSessionErrorPropertiesError_ProviderAuthError": ".event_session_error_properties_error",
    "EventSessionErrorPropertiesError_UnknownError": ".event_session_error_properties_error",
    "EventSessionIdle": ".event_session_idle",
    "EventSessionIdleProperties": ".event_session_idle_properties",
    "EventSessionStatus": ".event_session_status",
    "EventSessionStatusProperties": ".event_session_status_properties",
    "EventSessionUpdated": ".event_session_updated",
    "EventSessionUpdatedProperties": ".event_session_updated_properties",
    "EventTodoUpdated": ".event_todo_updated",
    "EventTodoUpdatedProperties": ".event_todo_updated_properties",
    "EventTuiCommandExecute": ".event_tui_command_execute",
    "EventTuiCommandExecuteProperties": ".event_tui_command_execute_properties",
    "EventTuiCommandExecutePropertiesCommand": ".event_tui_command_execute_properties_command",
    "EventTuiCommandExecutePropertiesCommandZero": ".event_tui_command_execute_properties_command_zero",
    "EventTuiPromptAppend": ".event_tui_prompt_append",
    "EventTuiPromptAppendProperties": ".event_tui_prompt_append_properties",
    "EventTuiSessionSelect": ".event_tui_session_select",
    "EventTuiSessionSelectProperties": ".event_tui_session_select_properties",
    "EventTuiToastShow": ".event_tui_toast_show",
    "EventTuiToastShowProperties": ".event_tui_toast_show_properties",
    "EventTuiToastShowPropertiesVariant": ".event_tui_toast_show_properties_variant",
    "EventVcsBranchUpdated": ".event_vcs_branch_updated",
    "EventVcsBranchUpdatedProperties": ".event_vcs_branch_updated_properties",
    "EventWorktreeFailed": ".event_worktree_failed",
    "EventWorktreeFailedProperties": ".event_worktree_failed_properties",
    "EventWorktreeReady": ".event_worktree_ready",
    "EventWorktreeReadyProperties": ".event_worktree_ready_properties",
    "Event_CommandExecuted": ".event",
    "Event_FileEdited": ".event",
    "Event_FileWatcherUpdated": ".event",
    "Event_GlobalDisposed": ".event",
    "Event_InstallationUpdateAvailable": ".event",
    "Event_InstallationUpdated": ".event",
    "Event_LspClientDiagnostics": ".event",
    "Event_LspUpdated": ".event",
    "Event_McpBrowserOpenFailed": ".event",
    "Event_McpToolsChanged": ".event",
    "Event_MessagePartRemoved": ".event",
    "Event_MessagePartUpdated": ".event",
    "Event_MessageRemoved": ".event",
    "Event_MessageUpdated": ".event",
    "Event_PermissionAsked": ".event",
    "Event_PermissionReplied": ".event",
    "Event_ProjectUpdated": ".event",
    "Event_PtyCreated": ".event",
    "Event_PtyDeleted": ".event",
    "Event_PtyExited": ".event",
    "Event_PtyUpdated": ".event",
    "Event_QuestionAsked": ".event",
    "Event_QuestionRejected": ".event",
    "Event_QuestionReplied": ".event",
    "Event_ServerConnected": ".event",
    "Event_ServerInstanceDisposed": ".event",
    "Event_SessionCompacted": ".event",
    "Event_SessionCreated": ".event",
    "Event_SessionDeleted": ".event",
    "Event_SessionDiff": ".event",
    "Event_SessionError": ".event",
    "Event_SessionIdle": ".event",
    "Event_SessionStatus": ".event",
    "Event_SessionUpdated": ".event",
    "Event_TodoUpdated": ".event",
    "Event_TuiCommandExecute": ".event",
    "Event_TuiPromptAppend": ".event",
    "Event_TuiSessionSelect": ".event",
    "Event_TuiToastShow": ".event",
    "Event_VcsBranchUpdated": ".event",
    "Event_WorktreeFailed": ".event",
    "Event_WorktreeReady": ".event",
    "File": ".file",
    "FileContent": ".file_content",
    "FileContentEncoding": ".file_content_encoding",
    "FileContentPatch": ".file_content_patch",
    "FileContentPatchHunksItem": ".file_content_patch_hunks_item",
    "FileContentType": ".file_content_type",
    "FileDiff": ".file_diff",
    "FileNode": ".file_node",
    "FileNodeType": ".file_node_type",
    "FilePart": ".file_part",
    "FilePartInput": ".file_part_input",
    "FilePartSource": ".file_part_source",
    "FilePartSourceText": ".file_part_source_text",
    "FilePartSource_File": ".file_part_source",
    "FilePartSource_Resource": ".file_part_source",
    "FilePartSource_Symbol": ".file_part_source",
    "FilePartType": ".file_part_type",
    "FileSource": ".file_source",
    "FileStatus": ".file_status",
    "FindFilesRequestDirs": ".find_files_request_dirs",
    "FindFilesRequestType": ".find_files_request_type",
    "FindTextResponseItem": ".find_text_response_item",
    "FindTextResponseItemLines": ".find_text_response_item_lines",
    "FindTextResponseItemPath": ".find_text_response_item_path",
    "FindTextResponseItemSubmatchesItem": ".find_text_response_item_submatches_item",
    "FindTextResponseItemSubmatchesItemMatch": ".find_text_response_item_submatches_item_match",
    "FormatterStatus": ".formatter_status",
    "GlobalEvent": ".global_event",
    "GlobalHealthResponse": ".global_health_response",
    "KeybindsConfig": ".keybinds_config",
    "LayoutConfig": ".layout_config",
    "LogLevel": ".log_level",
    "LspStatus": ".lsp_status",
    "LspStatusStatus": ".lsp_status_status",
    "LspStatusStatusOne": ".lsp_status_status_one",
    "LspStatusStatusZero": ".lsp_status_status_zero",
    "McpAddRequestConfig": ".mcp_add_request_config",
    "McpAddRequestConfig_Local": ".mcp_add_request_config",
    "McpAddRequestConfig_Remote": ".mcp_add_request_config",
    "McpAuthRemoveResponse": ".mcp_auth_remove_response",
    "McpAuthStartResponse": ".mcp_auth_start_response",
    "McpLocalConfig": ".mcp_local_config",
    "McpOAuthConfig": ".mcp_o_auth_config",
    "McpRemoteConfig": ".mcp_remote_config",
    "McpRemoteConfigOauth": ".mcp_remote_config_oauth",
    "McpResource": ".mcp_resource",
    "McpStatus": ".mcp_status",
    "McpStatusConnected": ".mcp_status_connected",
    "McpStatusDisabled": ".mcp_status_disabled",
    "McpStatusFailed": ".mcp_status_failed",
    "McpStatusNeedsAuth": ".mcp_status_needs_auth",
    "McpStatusNeedsClientRegistration": ".mcp_status_needs_client_registration",
    "McpStatus_Connected": ".mcp_status",
    "McpStatus_Disabled": ".mcp_status",
    "McpStatus_Failed": ".mcp_status",
    "McpStatus_NeedsAuth": ".mcp_status",
    "McpStatus_NeedsClientRegistration": ".mcp_status",
    "Message": ".message",
    "MessageAbortedError": ".message_aborted_error",
    "MessageAbortedErrorData": ".message_aborted_error_data",
    "MessageOutputLengthError": ".message_output_length_error",
    "MessageOutputLengthErrorData": ".message_output_length_error_data",
    "Message_Assistant": ".message",
    "Message_User": ".message",
    "Model": ".model",
    "ModelApi": ".model_api",
    "ModelCapabilities": ".model_capabilities",
    "ModelCapabilitiesInput": ".model_capabilities_input",
    "ModelCapabilitiesInterleaved": ".model_capabilities_interleaved",
    "ModelCapabilitiesInterleavedField": ".model_capabilities_interleaved_field",
    "ModelCapabilitiesInterleavedFieldField": ".model_capabilities_interleaved_field_field",
    "ModelCapabilitiesOutput": ".model_capabilities_output",
    "ModelCost": ".model_cost",
    "ModelCostCache": ".model_cost_cache",
    "ModelCostExperimentalOver200K": ".model_cost_experimental_over200k",
    "ModelCostExperimentalOver200KCache": ".model_cost_experimental_over200k_cache",
    "ModelLimit": ".model_limit",
    "ModelStatus": ".model_status",
    "NotFoundErrorBody": ".not_found_error_body",
    "NotFoundErrorBodyData": ".not_found_error_body_data",
    "NotFoundErrorBodyName": ".not_found_error_body_name",
    "OAuth": ".o_auth",
    "Part": ".part",
    "Part_Agent": ".part",
    "Part_Compaction": ".part",
    "Part_File": ".part",
    "Part_Patch": ".part",
    "Part_Reasoning": ".part",
    "Part_Retry": ".part",
    "Part_Snapshot": ".part",
    "Part_StepFinish": ".part",
    "Part_StepStart": ".part",
    "Part_Subtask": ".part",
    "Part_Text": ".part",
    "Part_Tool": ".part",
    "PatchPart": ".patch_part",
    "Path": ".path",
    "PermissionAction": ".permission_action",
    "PermissionActionConfig": ".permission_action_config",
    "PermissionConfig": ".permission_config",
    "PermissionConfigOriginalKeys": ".permission_config_original_keys",
    "PermissionObjectConfig": ".permission_object_config",
    "PermissionReplyRequestReply": ".permission_reply_request_reply",
    "PermissionRequest": ".permission_request",
    "PermissionRequestTool": ".permission_request_tool",
    "PermissionRespondRequestResponse": ".permission_respond_request_response",
    "PermissionRule": ".permission_rule",
    "PermissionRuleConfig": ".permission_rule_config",
    "PermissionRuleset": ".permission_ruleset",
    "Project": ".project",
    "ProjectCommands": ".project_commands",
    "ProjectIcon": ".project_icon",
    "ProjectTime": ".project_time",
    "ProjectUpdateRequestCommands": ".project_update_request_commands",
    "ProjectUpdateRequestIcon": ".project_update_request_icon",
    "ProjectVcs": ".project_vcs",
    "Provider": ".provider",
    "ProviderAuthAuthorization": ".provider_auth_authorization",
    "ProviderAuthAuthorizationMethod": ".provider_auth_authorization_method",
    "ProviderAuthAuthorizationMethodOne": ".provider_auth_authorization_method_one",
    "ProviderAuthAuthorizationMethodZero": ".provider_auth_authorization_method_zero",
    "ProviderAuthError": ".provider_auth_error",
    "ProviderAuthErrorData": ".provider_auth_error_data",
    "ProviderAuthMethod": ".provider_auth_method",
    "ProviderAuthMethodType": ".provider_auth_method_type",
    "ProviderAuthMethodTypeOne": ".provider_auth_method_type_one",
    "ProviderAuthMethodTypeZero": ".provider_auth_method_type_zero",
    "ProviderConfig": ".provider_config",
    "ProviderConfigModelsValue": ".provider_config_models_value",
    "ProviderConfigModelsValueCost": ".provider_config_models_value_cost",
    "ProviderConfigModelsValueCostContextOver200K": ".provider_config_models_value_cost_context_over200k",
    "ProviderConfigModelsValueInterleaved": ".provider_config_models_value_interleaved",
    "ProviderConfigModelsValueInterleavedField": ".provider_config_models_value_interleaved_field",
    "ProviderConfigModelsValueInterleavedFieldField": ".provider_config_models_value_interleaved_field_field",
    "ProviderConfigModelsValueLimit": ".provider_config_models_value_limit",
    "ProviderConfigModelsValueModalities": ".provider_config_models_value_modalities",
    "ProviderConfigModelsValueModalitiesInputItem": ".provider_config_models_value_modalities_input_item",
    "ProviderConfigModelsValueModalitiesOutputItem": ".provider_config_models_value_modalities_output_item",
    "ProviderConfigModelsValueProvider": ".provider_config_models_value_provider",
    "ProviderConfigModelsValueStatus": ".provider_config_models_value_status",
    "ProviderConfigModelsValueVariantsValue": ".provider_config_models_value_variants_value",
    "ProviderConfigOptions": ".provider_config_options",
    "ProviderConfigOptionsTimeout": ".provider_config_options_timeout",
    "ProviderListResponse": ".provider_list_response",
    "ProviderListResponseAllItem": ".provider_list_response_all_item",
    "ProviderListResponseAllItemModelsValue": ".provider_list_response_all_item_models_value",
    "ProviderListResponseAllItemModelsValueCost": ".provider_list_response_all_item_models_value_cost",
    "ProviderListResponseAllItemModelsValueCostContextOver200K": ".provider_list_response_all_item_models_value_cost_context_over200k",
    "ProviderListResponseAllItemModelsValueInterleaved": ".provider_list_response_all_item_models_value_interleaved",
    "ProviderListResponseAllItemModelsValueInterleavedField": ".provider_list_response_all_item_models_value_interleaved_field",
    "ProviderListResponseAllItemModelsValueInterleavedFieldField": ".provider_list_response_all_item_models_value_interleaved_field_field",
    "ProviderListResponseAllItemModelsValueLimit": ".provider_list_response_all_item_models_value_limit",
    "ProviderListResponseAllItemModelsValueModalities": ".provider_list_response_all_item_models_value_modalities",
    "ProviderListResponseAllItemModelsValueModalitiesInputItem": ".provider_list_response_all_item_models_value_modalities_input_item",
    "ProviderListResponseAllItemModelsValueModalitiesOutputItem": ".provider_list_response_all_item_models_value_modalities_output_item",
    "ProviderListResponseAllItemModelsValueProvider": ".provider_list_response_all_item_models_value_provider",
    "ProviderListResponseAllItemModelsValueStatus": ".provider_list_response_all_item_models_value_status",
    "ProviderSource": ".provider_source",
    "Pty": ".pty",
    "PtyStatus": ".pty_status",
    "PtyUpdateRequestSize": ".pty_update_request_size",
    "QuestionAnswer": ".question_answer",
    "QuestionInfo": ".question_info",
    "QuestionOption": ".question_option",
    "QuestionRequest": ".question_request",
    "QuestionRequestTool": ".question_request_tool",
    "Range": ".range",
    "RangeEnd": ".range_end",
    "RangeStart": ".range_start",
    "ReasoningPart": ".reasoning_part",
    "ReasoningPartTime": ".reasoning_part_time",
    "ResourceSource": ".resource_source",
    "RetryPart": ".retry_part",
    "RetryPartTime": ".retry_part_time",
    "ServerConfig": ".server_config",
    "Session": ".session",
    "SessionCommandRequestPartsItem": ".session_command_request_parts_item",
    "SessionCommandRequestPartsItemType": ".session_command_request_parts_item_type",
    "SessionCommandResponse": ".session_command_response",
    "SessionMessageResponse": ".session_message_response",
    "SessionMessagesResponseItem": ".session_messages_response_item",
    "SessionPromptAsyncRequestModel": ".session_prompt_async_request_model",
    "SessionPromptAsyncRequestPartsItem": ".session_prompt_async_request_parts_item",
    "SessionPromptAsyncRequestPartsItem_Agent": ".session_prompt_async_request_parts_item",
    "SessionPromptAsyncRequestPartsItem_File": ".session_prompt_async_request_parts_item",
    "SessionPromptAsyncRequestPartsItem_Subtask": ".session_prompt_async_request_parts_item",
    "SessionPromptAsyncRequestPartsItem_Text": ".session_prompt_async_request_parts_item",
    "SessionPromptRequestModel": ".session_prompt_request_model",
    "SessionPromptRequestPartsItem": ".session_prompt_request_parts_item",
    "SessionPromptRequestPartsItem_Agent": ".session_prompt_request_parts_item",
    "SessionPromptRequestPartsItem_File": ".session_prompt_request_parts_item",
    "SessionPromptRequestPartsItem_Subtask": ".session_prompt_request_parts_item",
    "SessionPromptRequestPartsItem_Text": ".session_prompt_request_parts_item",
    "SessionPromptResponse": ".session_prompt_response",
    "SessionRevert": ".session_revert",
    "SessionShare": ".session_share",
    "SessionShellRequestModel": ".session_shell_request_model",
    "SessionStatus": ".session_status",
    "SessionStatusBusy": ".session_status_busy",
    "SessionStatusIdle": ".session_status_idle",
    "SessionStatusRetry": ".session_status_retry",
    "SessionStatus_Busy": ".session_status",
    "SessionStatus_Idle": ".session_status",
    "SessionStatus_Retry": ".session_status",
    "SessionSummary": ".session_summary",
    "SessionTime": ".session_time",
    "SessionUpdateRequestTime": ".session_update_request_time",
    "SnapshotPart": ".snapshot_part",
    "StepFinishPart": ".step_finish_part",
    "StepFinishPartTokens": ".step_finish_part_tokens",
    "StepFinishPartTokensCache": ".step_finish_part_tokens_cache",
    "StepStartPart": ".step_start_part",
    "SubtaskPart": ".subtask_part",
    "SubtaskPartInput": ".subtask_part_input",
    "SubtaskPartInputModel": ".subtask_part_input_model",
    "SubtaskPartModel": ".subtask_part_model",
    "Symbol": ".symbol",
    "SymbolLocation": ".symbol_location",
    "SymbolSource": ".symbol_source",
    "TextPart": ".text_part",
    "TextPartInput": ".text_part_input",
    "TextPartInputTime": ".text_part_input_time",
    "TextPartTime": ".text_part_time",
    "Todo": ".todo",
    "ToolIDs": ".tool_i_ds",
    "ToolList": ".tool_list",
    "ToolListItem": ".tool_list_item",
    "ToolPart": ".tool_part",
    "ToolState": ".tool_state",
    "ToolStateCompleted": ".tool_state_completed",
    "ToolStateCompletedTime": ".tool_state_completed_time",
    "ToolStateError": ".tool_state_error",
    "ToolStateErrorTime": ".tool_state_error_time",
    "ToolStatePending": ".tool_state_pending",
    "ToolStateRunning": ".tool_state_running",
    "ToolStateRunningTime": ".tool_state_running_time",
    "ToolState_Completed": ".tool_state",
    "ToolState_Error": ".tool_state",
    "ToolState_Pending": ".tool_state",
    "ToolState_Running": ".tool_state",
    "TuiControlNextResponse": ".tui_control_next_response",
    "TuiPublishRequestBody": ".tui_publish_request_body",
    "TuiPublishRequestBody_TuiCommandExecute": ".tui_publish_request_body",
    "TuiPublishRequestBody_TuiPromptAppend": ".tui_publish_request_body",
    "TuiPublishRequestBody_TuiSessionSelect": ".tui_publish_request_body",
    "TuiPublishRequestBody_TuiToastShow": ".tui_publish_request_body",
    "TuiShowToastRequestVariant": ".tui_show_toast_request_variant",
    "UnknownError": ".unknown_error",
    "UnknownErrorData": ".unknown_error_data",
    "UserMessage": ".user_message",
    "UserMessageModel": ".user_message_model",
    "UserMessageSummary": ".user_message_summary",
    "UserMessageTime": ".user_message_time",
    "VcsInfo": ".vcs_info",
    "WellKnownAuth": ".well_known_auth",
    "Worktree": ".worktree",
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
    "Agent",
    "AgentConfig",
    "AgentConfigMode",
    "AgentMode",
    "AgentModel",
    "AgentPart",
    "AgentPartInput",
    "AgentPartInputSource",
    "AgentPartSource",
    "ApiAuth",
    "ApiError",
    "ApiErrorData",
    "ApiErrorName",
    "AppLogRequestLevel",
    "AppSkillsResponseItem",
    "AssistantMessage",
    "AssistantMessageError",
    "AssistantMessageError_ApiError",
    "AssistantMessageError_MessageAbortedError",
    "AssistantMessageError_MessageOutputLengthError",
    "AssistantMessageError_ProviderAuthError",
    "AssistantMessageError_UnknownError",
    "AssistantMessagePath",
    "AssistantMessageRole",
    "AssistantMessageTime",
    "AssistantMessageTokens",
    "AssistantMessageTokensCache",
    "Auth",
    "Auth_Api",
    "Auth_Oauth",
    "Auth_Wellknown",
    "BadRequestErrorBody",
    "Command",
    "CommandSource",
    "CompactionPart",
    "Config",
    "ConfigAgent",
    "ConfigAutoupdate",
    "ConfigAutoupdateOne",
    "ConfigCommandValue",
    "ConfigCompaction",
    "ConfigEnterprise",
    "ConfigExperimental",
    "ConfigFormatter",
    "ConfigFormatterOneValue",
    "ConfigLsp",
    "ConfigLspOneValue",
    "ConfigLspOneValueCommand",
    "ConfigLspOneValueZero",
    "ConfigMcpValue",
    "ConfigMcpValueEnabled",
    "ConfigMcpValueZero",
    "ConfigMcpValueZero_Local",
    "ConfigMcpValueZero_Remote",
    "ConfigMode",
    "ConfigProvidersResponse",
    "ConfigShare",
    "ConfigSkills",
    "ConfigTui",
    "ConfigTuiDiffStyle",
    "ConfigTuiScrollAcceleration",
    "ConfigWatcher",
    "Event",
    "EventCommandExecuted",
    "EventCommandExecutedProperties",
    "EventFileEdited",
    "EventFileEditedProperties",
    "EventFileWatcherUpdated",
    "EventFileWatcherUpdatedProperties",
    "EventFileWatcherUpdatedPropertiesEvent",
    "EventFileWatcherUpdatedPropertiesEventOne",
    "EventFileWatcherUpdatedPropertiesEventTwo",
    "EventFileWatcherUpdatedPropertiesEventZero",
    "EventGlobalDisposed",
    "EventGlobalDisposedProperties",
    "EventInstallationUpdateAvailable",
    "EventInstallationUpdateAvailableProperties",
    "EventInstallationUpdated",
    "EventInstallationUpdatedProperties",
    "EventLspClientDiagnostics",
    "EventLspClientDiagnosticsProperties",
    "EventLspUpdated",
    "EventLspUpdatedProperties",
    "EventMcpBrowserOpenFailed",
    "EventMcpBrowserOpenFailedProperties",
    "EventMcpToolsChanged",
    "EventMcpToolsChangedProperties",
    "EventMessagePartRemoved",
    "EventMessagePartRemovedProperties",
    "EventMessagePartUpdated",
    "EventMessagePartUpdatedProperties",
    "EventMessageRemoved",
    "EventMessageRemovedProperties",
    "EventMessageUpdated",
    "EventMessageUpdatedProperties",
    "EventPermissionAsked",
    "EventPermissionReplied",
    "EventPermissionRepliedProperties",
    "EventPermissionRepliedPropertiesReply",
    "EventProjectUpdated",
    "EventPtyCreated",
    "EventPtyCreatedProperties",
    "EventPtyDeleted",
    "EventPtyDeletedProperties",
    "EventPtyExited",
    "EventPtyExitedProperties",
    "EventPtyUpdated",
    "EventPtyUpdatedProperties",
    "EventQuestionAsked",
    "EventQuestionRejected",
    "EventQuestionRejectedProperties",
    "EventQuestionReplied",
    "EventQuestionRepliedProperties",
    "EventServerConnected",
    "EventServerConnectedProperties",
    "EventServerInstanceDisposed",
    "EventServerInstanceDisposedProperties",
    "EventSessionCompacted",
    "EventSessionCompactedProperties",
    "EventSessionCreated",
    "EventSessionCreatedProperties",
    "EventSessionDeleted",
    "EventSessionDeletedProperties",
    "EventSessionDiff",
    "EventSessionDiffProperties",
    "EventSessionError",
    "EventSessionErrorProperties",
    "EventSessionErrorPropertiesError",
    "EventSessionErrorPropertiesError_ApiError",
    "EventSessionErrorPropertiesError_MessageAbortedError",
    "EventSessionErrorPropertiesError_MessageOutputLengthError",
    "EventSessionErrorPropertiesError_ProviderAuthError",
    "EventSessionErrorPropertiesError_UnknownError",
    "EventSessionIdle",
    "EventSessionIdleProperties",
    "EventSessionStatus",
    "EventSessionStatusProperties",
    "EventSessionUpdated",
    "EventSessionUpdatedProperties",
    "EventTodoUpdated",
    "EventTodoUpdatedProperties",
    "EventTuiCommandExecute",
    "EventTuiCommandExecuteProperties",
    "EventTuiCommandExecutePropertiesCommand",
    "EventTuiCommandExecutePropertiesCommandZero",
    "EventTuiPromptAppend",
    "EventTuiPromptAppendProperties",
    "EventTuiSessionSelect",
    "EventTuiSessionSelectProperties",
    "EventTuiToastShow",
    "EventTuiToastShowProperties",
    "EventTuiToastShowPropertiesVariant",
    "EventVcsBranchUpdated",
    "EventVcsBranchUpdatedProperties",
    "EventWorktreeFailed",
    "EventWorktreeFailedProperties",
    "EventWorktreeReady",
    "EventWorktreeReadyProperties",
    "Event_CommandExecuted",
    "Event_FileEdited",
    "Event_FileWatcherUpdated",
    "Event_GlobalDisposed",
    "Event_InstallationUpdateAvailable",
    "Event_InstallationUpdated",
    "Event_LspClientDiagnostics",
    "Event_LspUpdated",
    "Event_McpBrowserOpenFailed",
    "Event_McpToolsChanged",
    "Event_MessagePartRemoved",
    "Event_MessagePartUpdated",
    "Event_MessageRemoved",
    "Event_MessageUpdated",
    "Event_PermissionAsked",
    "Event_PermissionReplied",
    "Event_ProjectUpdated",
    "Event_PtyCreated",
    "Event_PtyDeleted",
    "Event_PtyExited",
    "Event_PtyUpdated",
    "Event_QuestionAsked",
    "Event_QuestionRejected",
    "Event_QuestionReplied",
    "Event_ServerConnected",
    "Event_ServerInstanceDisposed",
    "Event_SessionCompacted",
    "Event_SessionCreated",
    "Event_SessionDeleted",
    "Event_SessionDiff",
    "Event_SessionError",
    "Event_SessionIdle",
    "Event_SessionStatus",
    "Event_SessionUpdated",
    "Event_TodoUpdated",
    "Event_TuiCommandExecute",
    "Event_TuiPromptAppend",
    "Event_TuiSessionSelect",
    "Event_TuiToastShow",
    "Event_VcsBranchUpdated",
    "Event_WorktreeFailed",
    "Event_WorktreeReady",
    "File",
    "FileContent",
    "FileContentEncoding",
    "FileContentPatch",
    "FileContentPatchHunksItem",
    "FileContentType",
    "FileDiff",
    "FileNode",
    "FileNodeType",
    "FilePart",
    "FilePartInput",
    "FilePartSource",
    "FilePartSourceText",
    "FilePartSource_File",
    "FilePartSource_Resource",
    "FilePartSource_Symbol",
    "FilePartType",
    "FileSource",
    "FileStatus",
    "FindFilesRequestDirs",
    "FindFilesRequestType",
    "FindTextResponseItem",
    "FindTextResponseItemLines",
    "FindTextResponseItemPath",
    "FindTextResponseItemSubmatchesItem",
    "FindTextResponseItemSubmatchesItemMatch",
    "FormatterStatus",
    "GlobalEvent",
    "GlobalHealthResponse",
    "KeybindsConfig",
    "LayoutConfig",
    "LogLevel",
    "LspStatus",
    "LspStatusStatus",
    "LspStatusStatusOne",
    "LspStatusStatusZero",
    "McpAddRequestConfig",
    "McpAddRequestConfig_Local",
    "McpAddRequestConfig_Remote",
    "McpAuthRemoveResponse",
    "McpAuthStartResponse",
    "McpLocalConfig",
    "McpOAuthConfig",
    "McpRemoteConfig",
    "McpRemoteConfigOauth",
    "McpResource",
    "McpStatus",
    "McpStatusConnected",
    "McpStatusDisabled",
    "McpStatusFailed",
    "McpStatusNeedsAuth",
    "McpStatusNeedsClientRegistration",
    "McpStatus_Connected",
    "McpStatus_Disabled",
    "McpStatus_Failed",
    "McpStatus_NeedsAuth",
    "McpStatus_NeedsClientRegistration",
    "Message",
    "MessageAbortedError",
    "MessageAbortedErrorData",
    "MessageOutputLengthError",
    "MessageOutputLengthErrorData",
    "Message_Assistant",
    "Message_User",
    "Model",
    "ModelApi",
    "ModelCapabilities",
    "ModelCapabilitiesInput",
    "ModelCapabilitiesInterleaved",
    "ModelCapabilitiesInterleavedField",
    "ModelCapabilitiesInterleavedFieldField",
    "ModelCapabilitiesOutput",
    "ModelCost",
    "ModelCostCache",
    "ModelCostExperimentalOver200K",
    "ModelCostExperimentalOver200KCache",
    "ModelLimit",
    "ModelStatus",
    "NotFoundErrorBody",
    "NotFoundErrorBodyData",
    "NotFoundErrorBodyName",
    "OAuth",
    "Part",
    "Part_Agent",
    "Part_Compaction",
    "Part_File",
    "Part_Patch",
    "Part_Reasoning",
    "Part_Retry",
    "Part_Snapshot",
    "Part_StepFinish",
    "Part_StepStart",
    "Part_Subtask",
    "Part_Text",
    "Part_Tool",
    "PatchPart",
    "Path",
    "PermissionAction",
    "PermissionActionConfig",
    "PermissionConfig",
    "PermissionConfigOriginalKeys",
    "PermissionObjectConfig",
    "PermissionReplyRequestReply",
    "PermissionRequest",
    "PermissionRequestTool",
    "PermissionRespondRequestResponse",
    "PermissionRule",
    "PermissionRuleConfig",
    "PermissionRuleset",
    "Project",
    "ProjectCommands",
    "ProjectIcon",
    "ProjectTime",
    "ProjectUpdateRequestCommands",
    "ProjectUpdateRequestIcon",
    "ProjectVcs",
    "Provider",
    "ProviderAuthAuthorization",
    "ProviderAuthAuthorizationMethod",
    "ProviderAuthAuthorizationMethodOne",
    "ProviderAuthAuthorizationMethodZero",
    "ProviderAuthError",
    "ProviderAuthErrorData",
    "ProviderAuthMethod",
    "ProviderAuthMethodType",
    "ProviderAuthMethodTypeOne",
    "ProviderAuthMethodTypeZero",
    "ProviderConfig",
    "ProviderConfigModelsValue",
    "ProviderConfigModelsValueCost",
    "ProviderConfigModelsValueCostContextOver200K",
    "ProviderConfigModelsValueInterleaved",
    "ProviderConfigModelsValueInterleavedField",
    "ProviderConfigModelsValueInterleavedFieldField",
    "ProviderConfigModelsValueLimit",
    "ProviderConfigModelsValueModalities",
    "ProviderConfigModelsValueModalitiesInputItem",
    "ProviderConfigModelsValueModalitiesOutputItem",
    "ProviderConfigModelsValueProvider",
    "ProviderConfigModelsValueStatus",
    "ProviderConfigModelsValueVariantsValue",
    "ProviderConfigOptions",
    "ProviderConfigOptionsTimeout",
    "ProviderListResponse",
    "ProviderListResponseAllItem",
    "ProviderListResponseAllItemModelsValue",
    "ProviderListResponseAllItemModelsValueCost",
    "ProviderListResponseAllItemModelsValueCostContextOver200K",
    "ProviderListResponseAllItemModelsValueInterleaved",
    "ProviderListResponseAllItemModelsValueInterleavedField",
    "ProviderListResponseAllItemModelsValueInterleavedFieldField",
    "ProviderListResponseAllItemModelsValueLimit",
    "ProviderListResponseAllItemModelsValueModalities",
    "ProviderListResponseAllItemModelsValueModalitiesInputItem",
    "ProviderListResponseAllItemModelsValueModalitiesOutputItem",
    "ProviderListResponseAllItemModelsValueProvider",
    "ProviderListResponseAllItemModelsValueStatus",
    "ProviderSource",
    "Pty",
    "PtyStatus",
    "PtyUpdateRequestSize",
    "QuestionAnswer",
    "QuestionInfo",
    "QuestionOption",
    "QuestionRequest",
    "QuestionRequestTool",
    "Range",
    "RangeEnd",
    "RangeStart",
    "ReasoningPart",
    "ReasoningPartTime",
    "ResourceSource",
    "RetryPart",
    "RetryPartTime",
    "ServerConfig",
    "Session",
    "SessionCommandRequestPartsItem",
    "SessionCommandRequestPartsItemType",
    "SessionCommandResponse",
    "SessionMessageResponse",
    "SessionMessagesResponseItem",
    "SessionPromptAsyncRequestModel",
    "SessionPromptAsyncRequestPartsItem",
    "SessionPromptAsyncRequestPartsItem_Agent",
    "SessionPromptAsyncRequestPartsItem_File",
    "SessionPromptAsyncRequestPartsItem_Subtask",
    "SessionPromptAsyncRequestPartsItem_Text",
    "SessionPromptRequestModel",
    "SessionPromptRequestPartsItem",
    "SessionPromptRequestPartsItem_Agent",
    "SessionPromptRequestPartsItem_File",
    "SessionPromptRequestPartsItem_Subtask",
    "SessionPromptRequestPartsItem_Text",
    "SessionPromptResponse",
    "SessionRevert",
    "SessionShare",
    "SessionShellRequestModel",
    "SessionStatus",
    "SessionStatusBusy",
    "SessionStatusIdle",
    "SessionStatusRetry",
    "SessionStatus_Busy",
    "SessionStatus_Idle",
    "SessionStatus_Retry",
    "SessionSummary",
    "SessionTime",
    "SessionUpdateRequestTime",
    "SnapshotPart",
    "StepFinishPart",
    "StepFinishPartTokens",
    "StepFinishPartTokensCache",
    "StepStartPart",
    "SubtaskPart",
    "SubtaskPartInput",
    "SubtaskPartInputModel",
    "SubtaskPartModel",
    "Symbol",
    "SymbolLocation",
    "SymbolSource",
    "TextPart",
    "TextPartInput",
    "TextPartInputTime",
    "TextPartTime",
    "Todo",
    "ToolIDs",
    "ToolList",
    "ToolListItem",
    "ToolPart",
    "ToolState",
    "ToolStateCompleted",
    "ToolStateCompletedTime",
    "ToolStateError",
    "ToolStateErrorTime",
    "ToolStatePending",
    "ToolStateRunning",
    "ToolStateRunningTime",
    "ToolState_Completed",
    "ToolState_Error",
    "ToolState_Pending",
    "ToolState_Running",
    "TuiControlNextResponse",
    "TuiPublishRequestBody",
    "TuiPublishRequestBody_TuiCommandExecute",
    "TuiPublishRequestBody_TuiPromptAppend",
    "TuiPublishRequestBody_TuiSessionSelect",
    "TuiPublishRequestBody_TuiToastShow",
    "TuiShowToastRequestVariant",
    "UnknownError",
    "UnknownErrorData",
    "UserMessage",
    "UserMessageModel",
    "UserMessageSummary",
    "UserMessageTime",
    "VcsInfo",
    "WellKnownAuth",
    "Worktree",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action_required_event import (
        ActionRequiredEvent,
        ActionRequiredEvent_McpAuthRequired,
        ActionRequiredEvent_ToolApprovalRequired,
        ActionRequiredEvent_ToolResponseRequired,
    )
    from .agent import Agent
    from .agent_code_snippet import AgentCodeSnippet
    from .agent_code_snippet_sample_code import AgentCodeSnippetSampleCode
    from .agent_code_snippets import AgentCodeSnippets
    from .agent_info import AgentInfo
    from .agent_info_type import AgentInfoType
    from .agent_parent import AgentParent
    from .agent_spec import AgentSpec
    from .alibaba_model_provider import AlibabaModelProvider
    from .anthropic_model_provider import AnthropicModelProvider
    from .approval_allow import ApprovalAllow
    from .approval_decision import ApprovalDecision, ApprovalDecision_Allow, ApprovalDecision_Deny
    from .approval_deny import ApprovalDeny
    from .ask_user_questions_config import AskUserQuestionsConfig
    from .available_mcp_server import AvailableMcpServer
    from .available_model import AvailableModel
    from .available_model_provider import AvailableModelProvider
    from .available_skill import AvailableSkill
    from .base_mcp_auth_required_event import BaseMcpAuthRequiredEvent
    from .base_thread_done_event import BaseThreadDoneEvent
    from .cancel_session_response import CancelSessionResponse
    from .capabilities_data import CapabilitiesData
    from .catalog_custom_model_provider import CatalogCustomModelProvider
    from .catalog_custom_model_provider_type import CatalogCustomModelProviderType
    from .catalog_mcp_server import CatalogMcpServer
    from .catalog_mcp_server_type import CatalogMcpServerType
    from .catalog_model import CatalogModel
    from .catalog_model_provider import CatalogModelProvider
    from .catalog_sandbox_provider import CatalogSandboxProvider
    from .catalog_sandbox_provider_type import CatalogSandboxProviderType
    from .catalog_skill import CatalogSkill
    from .catalog_well_known_model_provider import CatalogWellKnownModelProvider
    from .catalog_well_known_model_provider_type import CatalogWellKnownModelProviderType
    from .chat_completion_chunk_delta_tool_call import ChatCompletionChunkDeltaToolCall
    from .chat_completion_chunk_delta_tool_call_function import ChatCompletionChunkDeltaToolCallFunction
    from .chat_completion_chunk_delta_tool_call_type import ChatCompletionChunkDeltaToolCallType
    from .chat_completion_content_part_refusal import ChatCompletionContentPartRefusal
    from .chat_completion_content_part_text import ChatCompletionContentPartText
    from .chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from .chat_completion_message_tool_call_function import ChatCompletionMessageToolCallFunction
    from .chat_completion_message_tool_call_type import ChatCompletionMessageToolCallType
    from .compaction_config import CompactionConfig
    from .configured_mcp_server import ConfiguredMcpServer
    from .configured_model import ConfiguredModel
    from .configured_model_provider import ConfiguredModelProvider
    from .configured_sandbox_provider import ConfiguredSandboxProvider
    from .configured_skill import ConfiguredSkill
    from .context_management_config import ContextManagementConfig
    from .create_schedule_run_response import CreateScheduleRunResponse
    from .create_session_agent import CreateSessionAgent
    from .create_turn_request import CreateTurnRequest
    from .created_by_subject import CreatedBySubject
    from .cron_expression import CronExpression
    from .custom_model_provider import CustomModelProvider
    from .daytona_sandbox_provider_auth import DaytonaSandboxProviderAuth
    from .delete_agent_response import DeleteAgentResponse
    from .delete_schedule_response import DeleteScheduleResponse
    from .dynamic_sub_agents_config import DynamicSubAgentsConfig
    from .extended_chunk_delta_tool_call import ExtendedChunkDeltaToolCall
    from .file_content import FileContent
    from .finish_reason import FinishReason
    from .fireworks_model_provider import FireworksModelProvider
    from .generative_ui_config import GenerativeUiConfig
    from .get_agent_code_snippets_response import GetAgentCodeSnippetsResponse
    from .get_agent_response import GetAgentResponse
    from .get_capabilities_response import GetCapabilitiesResponse
    from .get_mcp_server_catalog_response import GetMcpServerCatalogResponse
    from .get_mcp_server_response import GetMcpServerResponse
    from .get_me_response import GetMeResponse
    from .get_me_subject import GetMeSubject
    from .get_model_provider_catalog_response import GetModelProviderCatalogResponse
    from .get_model_provider_response import GetModelProviderResponse
    from .get_sandbox_provider_catalog_response import GetSandboxProviderCatalogResponse
    from .get_sandbox_provider_response import GetSandboxProviderResponse
    from .get_schedule_response import GetScheduleResponse
    from .get_session_metrics_chart_data_response import GetSessionMetricsChartDataResponse
    from .get_session_metrics_chart_response import GetSessionMetricsChartResponse
    from .get_session_metrics_meter_response import GetSessionMetricsMeterResponse
    from .get_session_response import GetSessionResponse
    from .get_skill_catalog_response import GetSkillCatalogResponse
    from .get_skill_response import GetSkillResponse
    from .get_turn_response import GetTurnResponse
    from .google_gemini_model_provider import GoogleGeminiModelProvider
    from .initial_user_message import InitialUserMessage
    from .initial_user_message_type import InitialUserMessageType
    from .input_tokens_compaction_trigger import InputTokensCompactionTrigger
    from .input_tokens_compaction_trigger_type import InputTokensCompactionTriggerType
    from .large_tool_response_config import LargeToolResponseConfig
    from .list_agents_response import ListAgentsResponse
    from .list_available_mcp_servers_response import ListAvailableMcpServersResponse
    from .list_available_models_response import ListAvailableModelsResponse
    from .list_available_skills_response import ListAvailableSkillsResponse
    from .list_mcp_server_tools_response import ListMcpServerToolsResponse
    from .list_mcp_servers_response import ListMcpServersResponse
    from .list_model_providers_response import ListModelProvidersResponse
    from .list_schedule_runs_response import ListScheduleRunsResponse
    from .list_schedules_response import ListSchedulesResponse
    from .list_session_events_response import ListSessionEventsResponse
    from .list_sessions_order import ListSessionsOrder
    from .list_sessions_response import ListSessionsResponse
    from .list_skills_response import ListSkillsResponse
    from .list_turn_events_order import ListTurnEventsOrder
    from .list_turn_events_response import ListTurnEventsResponse
    from .list_turns_response import ListTurnsResponse
    from .mcp_auth_required_event import McpAuthRequiredEvent
    from .mcp_auth_status import McpAuthStatus
    from .mcp_auth_status_status import McpAuthStatusStatus
    from .mcp_initialize_event import McpInitializeEvent
    from .mcp_server import McpServer
    from .mcp_server_approval_tool_selector import McpServerApprovalToolSelector
    from .mcp_server_approval_tool_selector_zero import McpServerApprovalToolSelectorZero
    from .mcp_server_auth_info import McpServerAuthInfo
    from .mcp_server_auth_public import McpServerAuthPublic, McpServerAuthPublic_Dcr, McpServerAuthPublic_Header
    from .mcp_server_auth_public_dcr import McpServerAuthPublicDcr
    from .mcp_server_auth_public_header import McpServerAuthPublicHeader
    from .mcp_server_dcr_auth import McpServerDcrAuth
    from .mcp_server_header_auth import McpServerHeaderAuth
    from .mcp_server_init_info import McpServerInitInfo
    from .mcp_server_init_info_transport_type import McpServerInitInfoTransportType
    from .mcp_server_manifest import McpServerManifest
    from .mcp_server_manifest_auth import McpServerManifestAuth, McpServerManifestAuth_Dcr, McpServerManifestAuth_Header
    from .mcp_server_tool_selector import McpServerToolSelector
    from .mcp_server_tool_selector_zero import McpServerToolSelectorZero
    from .mcp_server_type import McpServerType
    from .mcp_tool_info import McpToolInfo
    from .me import Me
    from .me_session_type import MeSessionType
    from .metrics_unit import MetricsUnit
    from .model import Model
    from .model_message_delta_event import ModelMessageDeltaEvent
    from .model_message_event import ModelMessageEvent
    from .model_message_event_content import ModelMessageEventContent
    from .model_message_event_content_one_item import (
        ModelMessageEventContentOneItem,
        ModelMessageEventContentOneItem_Refusal,
        ModelMessageEventContentOneItem_Text,
    )
    from .model_message_event_type import ModelMessageEventType
    from .model_message_usage import ModelMessageUsage
    from .model_message_usage_input_tokens_breakdown import ModelMessageUsageInputTokensBreakdown
    from .model_params import ModelParams
    from .model_properties import ModelProperties
    from .model_provider_auth import ModelProviderAuth
    from .model_provider_manifest import (
        ModelProviderManifest,
        ModelProviderManifest_Alibaba,
        ModelProviderManifest_Anthropic,
        ModelProviderManifest_Custom,
        ModelProviderManifest_Fireworks,
        ModelProviderManifest_GoogleGemini,
        ModelProviderManifest_Moonshot,
        ModelProviderManifest_Openai,
        ModelProviderManifest_Together,
        ModelProviderManifest_Truefoundry,
        ModelProviderManifest_Zai,
    )
    from .moonshot_model_provider import MoonshotModelProvider
    from .open_ai_model_provider import OpenAiModelProvider
    from .previous_turn_id_input import PreviousTurnIdInput
    from .previous_turn_id_input_one import PreviousTurnIdInputOne
    from .previous_turn_id_input_zero import PreviousTurnIdInputZero
    from .raw_tool_call import RawToolCall
    from .reasoning_effort import ReasoningEffort
    from .request_error_response import RequestErrorResponse
    from .request_error_response_error import RequestErrorResponseError
    from .resource_name import ResourceName
    from .response_format import (
        ResponseFormat,
        ResponseFormat_JsonObject,
        ResponseFormat_JsonSchema,
        ResponseFormat_Text,
    )
    from .response_format_json_object import ResponseFormatJsonObject
    from .response_format_json_schema import ResponseFormatJsonSchema
    from .response_format_json_schema_json_schema import ResponseFormatJsonSchemaJsonSchema
    from .response_format_text import ResponseFormatText
    from .runtime_config import RuntimeConfig
    from .sandbox_build_status import SandboxBuildStatus
    from .sandbox_capability import SandboxCapability
    from .sandbox_config import SandboxConfig
    from .sandbox_created_event import SandboxCreatedEvent
    from .sandbox_provider_manifest import SandboxProviderManifest
    from .sandbox_provider_manifest_type import SandboxProviderManifestType
    from .schedule import Schedule
    from .schedule_manifest import ScheduleManifest
    from .schedule_run import ScheduleRun
    from .schedule_run_status import ScheduleRunStatus
    from .schedule_status import ScheduleStatus
    from .session import Session
    from .session_agent import SessionAgent, SessionAgent_Inline, SessionAgent_Reference
    from .session_agent_inline import SessionAgentInline
    from .session_agent_name_ref import SessionAgentNameRef
    from .session_agent_reference import SessionAgentReference
    from .session_agent_spec_body import SessionAgentSpecBody
    from .session_event import (
        SessionEvent,
        SessionEvent_McpAuthRequired,
        SessionEvent_McpInitialize,
        SessionEvent_ModelMessage,
        SessionEvent_SandboxCreated,
        SessionEvent_ThreadCreated,
        SessionEvent_ThreadDone,
        SessionEvent_ToolApprovalRequired,
        SessionEvent_ToolResponse,
        SessionEvent_ToolResponseRequired,
        SessionEvent_TurnCreated,
        SessionEvent_TurnDone,
    )
    from .session_event_item import SessionEventItem
    from .session_metadata import SessionMetadata
    from .session_metrics import SessionMetrics
    from .session_metrics_chart import SessionMetricsChart
    from .session_metrics_chart_chart_type import SessionMetricsChartChartType
    from .session_metrics_chart_data_response import SessionMetricsChartDataResponse
    from .session_metrics_chart_name import SessionMetricsChartName
    from .session_metrics_chart_response import SessionMetricsChartResponse
    from .session_metrics_graph import SessionMetricsGraph
    from .session_metrics_graph_chart_type import SessionMetricsGraphChartType
    from .session_metrics_graph_line import SessionMetricsGraphLine
    from .session_metrics_meter import SessionMetricsMeter
    from .session_metrics_meter_name import SessionMetricsMeterName
    from .session_metrics_meter_response import SessionMetricsMeterResponse
    from .session_metrics_point import SessionMetricsPoint
    from .settings_capability import SettingsCapability
    from .skill import Skill
    from .skill_capability import SkillCapability
    from .skill_manifest import SkillManifest
    from .skill_type import SkillType
    from .text_content import TextContent
    from .thread_created_event import ThreadCreatedEvent
    from .thread_done_event import ThreadDoneEvent
    from .thread_state import ThreadState, ThreadState_Done, ThreadState_Error
    from .thread_state_done import ThreadStateDone
    from .thread_state_error import ThreadStateError
    from .timezone import Timezone
    from .together_ai_model_provider import TogetherAiModelProvider
    from .token_pagination import TokenPagination
    from .tool_approval_required_event import ToolApprovalRequiredEvent
    from .tool_call import ToolCall
    from .tool_call_ref import ToolCallRef
    from .tool_info import ToolInfo, ToolInfo_Mcp, ToolInfo_TruefoundrySystem
    from .tool_response_event import ToolResponseEvent
    from .tool_response_required_event import ToolResponseRequiredEvent
    from .true_foundry_model_provider import TrueFoundryModelProvider
    from .true_foundry_system_tool_info import TrueFoundrySystemToolInfo
    from .turn import Turn
    from .turn_created_event import TurnCreatedEvent
    from .turn_done_event import TurnDoneEvent
    from .turn_done_event_state import (
        TurnDoneEventState,
        TurnDoneEventState_Cancelled,
        TurnDoneEventState_Done,
        TurnDoneEventState_Error,
    )
    from .turn_input_item import (
        TurnInputItem,
        TurnInputItem_UserMessage,
        TurnInputItem_UserToolApproval,
        TurnInputItem_UserToolResponse,
    )
    from .turn_metrics import TurnMetrics
    from .turn_state import TurnState, TurnState_Cancelled, TurnState_Done, TurnState_Error, TurnState_Running
    from .turn_state_cancelled import TurnStateCancelled
    from .turn_state_cancelled_metrics import TurnStateCancelledMetrics
    from .turn_state_cancelled_reason import TurnStateCancelledReason
    from .turn_state_done import TurnStateDone
    from .turn_state_error import TurnStateError
    from .turn_state_error_metrics import TurnStateErrorMetrics
    from .turn_state_running import TurnStateRunning
    from .turn_state_running_status import TurnStateRunningStatus
    from .turn_streaming_event import (
        TurnStreamingEvent,
        TurnStreamingEvent_McpAuthRequired,
        TurnStreamingEvent_McpInitialize,
        TurnStreamingEvent_ModelMessage,
        TurnStreamingEvent_ModelMessageDelta,
        TurnStreamingEvent_SandboxCreated,
        TurnStreamingEvent_ThreadCreated,
        TurnStreamingEvent_ThreadDone,
        TurnStreamingEvent_ToolApprovalRequired,
        TurnStreamingEvent_ToolResponse,
        TurnStreamingEvent_ToolResponseRequired,
        TurnStreamingEvent_TurnCreated,
        TurnStreamingEvent_TurnDone,
    )
    from .user_message import UserMessage
    from .user_message_content import UserMessageContent
    from .user_message_content_item import (
        UserMessageContentItem,
        UserMessageContentItem_File,
        UserMessageContentItem_Text,
    )
    from .user_tool_approval_event import UserToolApprovalEvent
    from .user_tool_response_event import UserToolResponseEvent
    from .zai_model_provider import ZaiModelProvider
_dynamic_imports: typing.Dict[str, str] = {
    "ActionRequiredEvent": ".action_required_event",
    "ActionRequiredEvent_McpAuthRequired": ".action_required_event",
    "ActionRequiredEvent_ToolApprovalRequired": ".action_required_event",
    "ActionRequiredEvent_ToolResponseRequired": ".action_required_event",
    "Agent": ".agent",
    "AgentCodeSnippet": ".agent_code_snippet",
    "AgentCodeSnippetSampleCode": ".agent_code_snippet_sample_code",
    "AgentCodeSnippets": ".agent_code_snippets",
    "AgentInfo": ".agent_info",
    "AgentInfoType": ".agent_info_type",
    "AgentParent": ".agent_parent",
    "AgentSpec": ".agent_spec",
    "AlibabaModelProvider": ".alibaba_model_provider",
    "AnthropicModelProvider": ".anthropic_model_provider",
    "ApprovalAllow": ".approval_allow",
    "ApprovalDecision": ".approval_decision",
    "ApprovalDecision_Allow": ".approval_decision",
    "ApprovalDecision_Deny": ".approval_decision",
    "ApprovalDeny": ".approval_deny",
    "AskUserQuestionsConfig": ".ask_user_questions_config",
    "AvailableMcpServer": ".available_mcp_server",
    "AvailableModel": ".available_model",
    "AvailableModelProvider": ".available_model_provider",
    "AvailableSkill": ".available_skill",
    "BaseMcpAuthRequiredEvent": ".base_mcp_auth_required_event",
    "BaseThreadDoneEvent": ".base_thread_done_event",
    "CancelSessionResponse": ".cancel_session_response",
    "CapabilitiesData": ".capabilities_data",
    "CatalogCustomModelProvider": ".catalog_custom_model_provider",
    "CatalogCustomModelProviderType": ".catalog_custom_model_provider_type",
    "CatalogMcpServer": ".catalog_mcp_server",
    "CatalogMcpServerType": ".catalog_mcp_server_type",
    "CatalogModel": ".catalog_model",
    "CatalogModelProvider": ".catalog_model_provider",
    "CatalogSandboxProvider": ".catalog_sandbox_provider",
    "CatalogSandboxProviderType": ".catalog_sandbox_provider_type",
    "CatalogSkill": ".catalog_skill",
    "CatalogWellKnownModelProvider": ".catalog_well_known_model_provider",
    "CatalogWellKnownModelProviderType": ".catalog_well_known_model_provider_type",
    "ChatCompletionChunkDeltaToolCall": ".chat_completion_chunk_delta_tool_call",
    "ChatCompletionChunkDeltaToolCallFunction": ".chat_completion_chunk_delta_tool_call_function",
    "ChatCompletionChunkDeltaToolCallType": ".chat_completion_chunk_delta_tool_call_type",
    "ChatCompletionContentPartRefusal": ".chat_completion_content_part_refusal",
    "ChatCompletionContentPartText": ".chat_completion_content_part_text",
    "ChatCompletionMessageToolCall": ".chat_completion_message_tool_call",
    "ChatCompletionMessageToolCallFunction": ".chat_completion_message_tool_call_function",
    "ChatCompletionMessageToolCallType": ".chat_completion_message_tool_call_type",
    "CompactionConfig": ".compaction_config",
    "ConfiguredMcpServer": ".configured_mcp_server",
    "ConfiguredModel": ".configured_model",
    "ConfiguredModelProvider": ".configured_model_provider",
    "ConfiguredSandboxProvider": ".configured_sandbox_provider",
    "ConfiguredSkill": ".configured_skill",
    "ContextManagementConfig": ".context_management_config",
    "CreateScheduleRunResponse": ".create_schedule_run_response",
    "CreateSessionAgent": ".create_session_agent",
    "CreateTurnRequest": ".create_turn_request",
    "CreatedBySubject": ".created_by_subject",
    "CronExpression": ".cron_expression",
    "CustomModelProvider": ".custom_model_provider",
    "DaytonaSandboxProviderAuth": ".daytona_sandbox_provider_auth",
    "DeleteAgentResponse": ".delete_agent_response",
    "DeleteScheduleResponse": ".delete_schedule_response",
    "DynamicSubAgentsConfig": ".dynamic_sub_agents_config",
    "ExtendedChunkDeltaToolCall": ".extended_chunk_delta_tool_call",
    "FileContent": ".file_content",
    "FinishReason": ".finish_reason",
    "FireworksModelProvider": ".fireworks_model_provider",
    "GenerativeUiConfig": ".generative_ui_config",
    "GetAgentCodeSnippetsResponse": ".get_agent_code_snippets_response",
    "GetAgentResponse": ".get_agent_response",
    "GetCapabilitiesResponse": ".get_capabilities_response",
    "GetMcpServerCatalogResponse": ".get_mcp_server_catalog_response",
    "GetMcpServerResponse": ".get_mcp_server_response",
    "GetMeResponse": ".get_me_response",
    "GetMeSubject": ".get_me_subject",
    "GetModelProviderCatalogResponse": ".get_model_provider_catalog_response",
    "GetModelProviderResponse": ".get_model_provider_response",
    "GetSandboxProviderCatalogResponse": ".get_sandbox_provider_catalog_response",
    "GetSandboxProviderResponse": ".get_sandbox_provider_response",
    "GetScheduleResponse": ".get_schedule_response",
    "GetSessionMetricsChartDataResponse": ".get_session_metrics_chart_data_response",
    "GetSessionMetricsChartResponse": ".get_session_metrics_chart_response",
    "GetSessionMetricsMeterResponse": ".get_session_metrics_meter_response",
    "GetSessionResponse": ".get_session_response",
    "GetSkillCatalogResponse": ".get_skill_catalog_response",
    "GetSkillResponse": ".get_skill_response",
    "GetTurnResponse": ".get_turn_response",
    "GoogleGeminiModelProvider": ".google_gemini_model_provider",
    "InitialUserMessage": ".initial_user_message",
    "InitialUserMessageType": ".initial_user_message_type",
    "InputTokensCompactionTrigger": ".input_tokens_compaction_trigger",
    "InputTokensCompactionTriggerType": ".input_tokens_compaction_trigger_type",
    "LargeToolResponseConfig": ".large_tool_response_config",
    "ListAgentsResponse": ".list_agents_response",
    "ListAvailableMcpServersResponse": ".list_available_mcp_servers_response",
    "ListAvailableModelsResponse": ".list_available_models_response",
    "ListAvailableSkillsResponse": ".list_available_skills_response",
    "ListMcpServerToolsResponse": ".list_mcp_server_tools_response",
    "ListMcpServersResponse": ".list_mcp_servers_response",
    "ListModelProvidersResponse": ".list_model_providers_response",
    "ListScheduleRunsResponse": ".list_schedule_runs_response",
    "ListSchedulesResponse": ".list_schedules_response",
    "ListSessionEventsResponse": ".list_session_events_response",
    "ListSessionsOrder": ".list_sessions_order",
    "ListSessionsResponse": ".list_sessions_response",
    "ListSkillsResponse": ".list_skills_response",
    "ListTurnEventsOrder": ".list_turn_events_order",
    "ListTurnEventsResponse": ".list_turn_events_response",
    "ListTurnsResponse": ".list_turns_response",
    "McpAuthRequiredEvent": ".mcp_auth_required_event",
    "McpAuthStatus": ".mcp_auth_status",
    "McpAuthStatusStatus": ".mcp_auth_status_status",
    "McpInitializeEvent": ".mcp_initialize_event",
    "McpServer": ".mcp_server",
    "McpServerApprovalToolSelector": ".mcp_server_approval_tool_selector",
    "McpServerApprovalToolSelectorZero": ".mcp_server_approval_tool_selector_zero",
    "McpServerAuthInfo": ".mcp_server_auth_info",
    "McpServerAuthPublic": ".mcp_server_auth_public",
    "McpServerAuthPublicDcr": ".mcp_server_auth_public_dcr",
    "McpServerAuthPublicHeader": ".mcp_server_auth_public_header",
    "McpServerAuthPublic_Dcr": ".mcp_server_auth_public",
    "McpServerAuthPublic_Header": ".mcp_server_auth_public",
    "McpServerDcrAuth": ".mcp_server_dcr_auth",
    "McpServerHeaderAuth": ".mcp_server_header_auth",
    "McpServerInitInfo": ".mcp_server_init_info",
    "McpServerInitInfoTransportType": ".mcp_server_init_info_transport_type",
    "McpServerManifest": ".mcp_server_manifest",
    "McpServerManifestAuth": ".mcp_server_manifest_auth",
    "McpServerManifestAuth_Dcr": ".mcp_server_manifest_auth",
    "McpServerManifestAuth_Header": ".mcp_server_manifest_auth",
    "McpServerToolSelector": ".mcp_server_tool_selector",
    "McpServerToolSelectorZero": ".mcp_server_tool_selector_zero",
    "McpServerType": ".mcp_server_type",
    "McpToolInfo": ".mcp_tool_info",
    "Me": ".me",
    "MeSessionType": ".me_session_type",
    "MetricsUnit": ".metrics_unit",
    "Model": ".model",
    "ModelMessageDeltaEvent": ".model_message_delta_event",
    "ModelMessageEvent": ".model_message_event",
    "ModelMessageEventContent": ".model_message_event_content",
    "ModelMessageEventContentOneItem": ".model_message_event_content_one_item",
    "ModelMessageEventContentOneItem_Refusal": ".model_message_event_content_one_item",
    "ModelMessageEventContentOneItem_Text": ".model_message_event_content_one_item",
    "ModelMessageEventType": ".model_message_event_type",
    "ModelMessageUsage": ".model_message_usage",
    "ModelMessageUsageInputTokensBreakdown": ".model_message_usage_input_tokens_breakdown",
    "ModelParams": ".model_params",
    "ModelProperties": ".model_properties",
    "ModelProviderAuth": ".model_provider_auth",
    "ModelProviderManifest": ".model_provider_manifest",
    "ModelProviderManifest_Alibaba": ".model_provider_manifest",
    "ModelProviderManifest_Anthropic": ".model_provider_manifest",
    "ModelProviderManifest_Custom": ".model_provider_manifest",
    "ModelProviderManifest_Fireworks": ".model_provider_manifest",
    "ModelProviderManifest_GoogleGemini": ".model_provider_manifest",
    "ModelProviderManifest_Moonshot": ".model_provider_manifest",
    "ModelProviderManifest_Openai": ".model_provider_manifest",
    "ModelProviderManifest_Together": ".model_provider_manifest",
    "ModelProviderManifest_Truefoundry": ".model_provider_manifest",
    "ModelProviderManifest_Zai": ".model_provider_manifest",
    "MoonshotModelProvider": ".moonshot_model_provider",
    "OpenAiModelProvider": ".open_ai_model_provider",
    "PreviousTurnIdInput": ".previous_turn_id_input",
    "PreviousTurnIdInputOne": ".previous_turn_id_input_one",
    "PreviousTurnIdInputZero": ".previous_turn_id_input_zero",
    "RawToolCall": ".raw_tool_call",
    "ReasoningEffort": ".reasoning_effort",
    "RequestErrorResponse": ".request_error_response",
    "RequestErrorResponseError": ".request_error_response_error",
    "ResourceName": ".resource_name",
    "ResponseFormat": ".response_format",
    "ResponseFormatJsonObject": ".response_format_json_object",
    "ResponseFormatJsonSchema": ".response_format_json_schema",
    "ResponseFormatJsonSchemaJsonSchema": ".response_format_json_schema_json_schema",
    "ResponseFormatText": ".response_format_text",
    "ResponseFormat_JsonObject": ".response_format",
    "ResponseFormat_JsonSchema": ".response_format",
    "ResponseFormat_Text": ".response_format",
    "RuntimeConfig": ".runtime_config",
    "SandboxBuildStatus": ".sandbox_build_status",
    "SandboxCapability": ".sandbox_capability",
    "SandboxConfig": ".sandbox_config",
    "SandboxCreatedEvent": ".sandbox_created_event",
    "SandboxProviderManifest": ".sandbox_provider_manifest",
    "SandboxProviderManifestType": ".sandbox_provider_manifest_type",
    "Schedule": ".schedule",
    "ScheduleManifest": ".schedule_manifest",
    "ScheduleRun": ".schedule_run",
    "ScheduleRunStatus": ".schedule_run_status",
    "ScheduleStatus": ".schedule_status",
    "Session": ".session",
    "SessionAgent": ".session_agent",
    "SessionAgentInline": ".session_agent_inline",
    "SessionAgentNameRef": ".session_agent_name_ref",
    "SessionAgentReference": ".session_agent_reference",
    "SessionAgentSpecBody": ".session_agent_spec_body",
    "SessionAgent_Inline": ".session_agent",
    "SessionAgent_Reference": ".session_agent",
    "SessionEvent": ".session_event",
    "SessionEventItem": ".session_event_item",
    "SessionEvent_McpAuthRequired": ".session_event",
    "SessionEvent_McpInitialize": ".session_event",
    "SessionEvent_ModelMessage": ".session_event",
    "SessionEvent_SandboxCreated": ".session_event",
    "SessionEvent_ThreadCreated": ".session_event",
    "SessionEvent_ThreadDone": ".session_event",
    "SessionEvent_ToolApprovalRequired": ".session_event",
    "SessionEvent_ToolResponse": ".session_event",
    "SessionEvent_ToolResponseRequired": ".session_event",
    "SessionEvent_TurnCreated": ".session_event",
    "SessionEvent_TurnDone": ".session_event",
    "SessionMetadata": ".session_metadata",
    "SessionMetrics": ".session_metrics",
    "SessionMetricsChart": ".session_metrics_chart",
    "SessionMetricsChartChartType": ".session_metrics_chart_chart_type",
    "SessionMetricsChartDataResponse": ".session_metrics_chart_data_response",
    "SessionMetricsChartName": ".session_metrics_chart_name",
    "SessionMetricsChartResponse": ".session_metrics_chart_response",
    "SessionMetricsGraph": ".session_metrics_graph",
    "SessionMetricsGraphChartType": ".session_metrics_graph_chart_type",
    "SessionMetricsGraphLine": ".session_metrics_graph_line",
    "SessionMetricsMeter": ".session_metrics_meter",
    "SessionMetricsMeterName": ".session_metrics_meter_name",
    "SessionMetricsMeterResponse": ".session_metrics_meter_response",
    "SessionMetricsPoint": ".session_metrics_point",
    "SettingsCapability": ".settings_capability",
    "Skill": ".skill",
    "SkillCapability": ".skill_capability",
    "SkillManifest": ".skill_manifest",
    "SkillType": ".skill_type",
    "TextContent": ".text_content",
    "ThreadCreatedEvent": ".thread_created_event",
    "ThreadDoneEvent": ".thread_done_event",
    "ThreadState": ".thread_state",
    "ThreadStateDone": ".thread_state_done",
    "ThreadStateError": ".thread_state_error",
    "ThreadState_Done": ".thread_state",
    "ThreadState_Error": ".thread_state",
    "Timezone": ".timezone",
    "TogetherAiModelProvider": ".together_ai_model_provider",
    "TokenPagination": ".token_pagination",
    "ToolApprovalRequiredEvent": ".tool_approval_required_event",
    "ToolCall": ".tool_call",
    "ToolCallRef": ".tool_call_ref",
    "ToolInfo": ".tool_info",
    "ToolInfo_Mcp": ".tool_info",
    "ToolInfo_TruefoundrySystem": ".tool_info",
    "ToolResponseEvent": ".tool_response_event",
    "ToolResponseRequiredEvent": ".tool_response_required_event",
    "TrueFoundryModelProvider": ".true_foundry_model_provider",
    "TrueFoundrySystemToolInfo": ".true_foundry_system_tool_info",
    "Turn": ".turn",
    "TurnCreatedEvent": ".turn_created_event",
    "TurnDoneEvent": ".turn_done_event",
    "TurnDoneEventState": ".turn_done_event_state",
    "TurnDoneEventState_Cancelled": ".turn_done_event_state",
    "TurnDoneEventState_Done": ".turn_done_event_state",
    "TurnDoneEventState_Error": ".turn_done_event_state",
    "TurnInputItem": ".turn_input_item",
    "TurnInputItem_UserMessage": ".turn_input_item",
    "TurnInputItem_UserToolApproval": ".turn_input_item",
    "TurnInputItem_UserToolResponse": ".turn_input_item",
    "TurnMetrics": ".turn_metrics",
    "TurnState": ".turn_state",
    "TurnStateCancelled": ".turn_state_cancelled",
    "TurnStateCancelledMetrics": ".turn_state_cancelled_metrics",
    "TurnStateCancelledReason": ".turn_state_cancelled_reason",
    "TurnStateDone": ".turn_state_done",
    "TurnStateError": ".turn_state_error",
    "TurnStateErrorMetrics": ".turn_state_error_metrics",
    "TurnStateRunning": ".turn_state_running",
    "TurnStateRunningStatus": ".turn_state_running_status",
    "TurnState_Cancelled": ".turn_state",
    "TurnState_Done": ".turn_state",
    "TurnState_Error": ".turn_state",
    "TurnState_Running": ".turn_state",
    "TurnStreamingEvent": ".turn_streaming_event",
    "TurnStreamingEvent_McpAuthRequired": ".turn_streaming_event",
    "TurnStreamingEvent_McpInitialize": ".turn_streaming_event",
    "TurnStreamingEvent_ModelMessage": ".turn_streaming_event",
    "TurnStreamingEvent_ModelMessageDelta": ".turn_streaming_event",
    "TurnStreamingEvent_SandboxCreated": ".turn_streaming_event",
    "TurnStreamingEvent_ThreadCreated": ".turn_streaming_event",
    "TurnStreamingEvent_ThreadDone": ".turn_streaming_event",
    "TurnStreamingEvent_ToolApprovalRequired": ".turn_streaming_event",
    "TurnStreamingEvent_ToolResponse": ".turn_streaming_event",
    "TurnStreamingEvent_ToolResponseRequired": ".turn_streaming_event",
    "TurnStreamingEvent_TurnCreated": ".turn_streaming_event",
    "TurnStreamingEvent_TurnDone": ".turn_streaming_event",
    "UserMessage": ".user_message",
    "UserMessageContent": ".user_message_content",
    "UserMessageContentItem": ".user_message_content_item",
    "UserMessageContentItem_File": ".user_message_content_item",
    "UserMessageContentItem_Text": ".user_message_content_item",
    "UserToolApprovalEvent": ".user_tool_approval_event",
    "UserToolResponseEvent": ".user_tool_response_event",
    "ZaiModelProvider": ".zai_model_provider",
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
    "ActionRequiredEvent",
    "ActionRequiredEvent_McpAuthRequired",
    "ActionRequiredEvent_ToolApprovalRequired",
    "ActionRequiredEvent_ToolResponseRequired",
    "Agent",
    "AgentCodeSnippet",
    "AgentCodeSnippetSampleCode",
    "AgentCodeSnippets",
    "AgentInfo",
    "AgentInfoType",
    "AgentParent",
    "AgentSpec",
    "AlibabaModelProvider",
    "AnthropicModelProvider",
    "ApprovalAllow",
    "ApprovalDecision",
    "ApprovalDecision_Allow",
    "ApprovalDecision_Deny",
    "ApprovalDeny",
    "AskUserQuestionsConfig",
    "AvailableMcpServer",
    "AvailableModel",
    "AvailableModelProvider",
    "AvailableSkill",
    "BaseMcpAuthRequiredEvent",
    "BaseThreadDoneEvent",
    "CancelSessionResponse",
    "CapabilitiesData",
    "CatalogCustomModelProvider",
    "CatalogCustomModelProviderType",
    "CatalogMcpServer",
    "CatalogMcpServerType",
    "CatalogModel",
    "CatalogModelProvider",
    "CatalogSandboxProvider",
    "CatalogSandboxProviderType",
    "CatalogSkill",
    "CatalogWellKnownModelProvider",
    "CatalogWellKnownModelProviderType",
    "ChatCompletionChunkDeltaToolCall",
    "ChatCompletionChunkDeltaToolCallFunction",
    "ChatCompletionChunkDeltaToolCallType",
    "ChatCompletionContentPartRefusal",
    "ChatCompletionContentPartText",
    "ChatCompletionMessageToolCall",
    "ChatCompletionMessageToolCallFunction",
    "ChatCompletionMessageToolCallType",
    "CompactionConfig",
    "ConfiguredMcpServer",
    "ConfiguredModel",
    "ConfiguredModelProvider",
    "ConfiguredSandboxProvider",
    "ConfiguredSkill",
    "ContextManagementConfig",
    "CreateScheduleRunResponse",
    "CreateSessionAgent",
    "CreateTurnRequest",
    "CreatedBySubject",
    "CronExpression",
    "CustomModelProvider",
    "DaytonaSandboxProviderAuth",
    "DeleteAgentResponse",
    "DeleteScheduleResponse",
    "DynamicSubAgentsConfig",
    "ExtendedChunkDeltaToolCall",
    "FileContent",
    "FinishReason",
    "FireworksModelProvider",
    "GenerativeUiConfig",
    "GetAgentCodeSnippetsResponse",
    "GetAgentResponse",
    "GetCapabilitiesResponse",
    "GetMcpServerCatalogResponse",
    "GetMcpServerResponse",
    "GetMeResponse",
    "GetMeSubject",
    "GetModelProviderCatalogResponse",
    "GetModelProviderResponse",
    "GetSandboxProviderCatalogResponse",
    "GetSandboxProviderResponse",
    "GetScheduleResponse",
    "GetSessionMetricsChartDataResponse",
    "GetSessionMetricsChartResponse",
    "GetSessionMetricsMeterResponse",
    "GetSessionResponse",
    "GetSkillCatalogResponse",
    "GetSkillResponse",
    "GetTurnResponse",
    "GoogleGeminiModelProvider",
    "InitialUserMessage",
    "InitialUserMessageType",
    "InputTokensCompactionTrigger",
    "InputTokensCompactionTriggerType",
    "LargeToolResponseConfig",
    "ListAgentsResponse",
    "ListAvailableMcpServersResponse",
    "ListAvailableModelsResponse",
    "ListAvailableSkillsResponse",
    "ListMcpServerToolsResponse",
    "ListMcpServersResponse",
    "ListModelProvidersResponse",
    "ListScheduleRunsResponse",
    "ListSchedulesResponse",
    "ListSessionEventsResponse",
    "ListSessionsOrder",
    "ListSessionsResponse",
    "ListSkillsResponse",
    "ListTurnEventsOrder",
    "ListTurnEventsResponse",
    "ListTurnsResponse",
    "McpAuthRequiredEvent",
    "McpAuthStatus",
    "McpAuthStatusStatus",
    "McpInitializeEvent",
    "McpServer",
    "McpServerApprovalToolSelector",
    "McpServerApprovalToolSelectorZero",
    "McpServerAuthInfo",
    "McpServerAuthPublic",
    "McpServerAuthPublicDcr",
    "McpServerAuthPublicHeader",
    "McpServerAuthPublic_Dcr",
    "McpServerAuthPublic_Header",
    "McpServerDcrAuth",
    "McpServerHeaderAuth",
    "McpServerInitInfo",
    "McpServerInitInfoTransportType",
    "McpServerManifest",
    "McpServerManifestAuth",
    "McpServerManifestAuth_Dcr",
    "McpServerManifestAuth_Header",
    "McpServerToolSelector",
    "McpServerToolSelectorZero",
    "McpServerType",
    "McpToolInfo",
    "Me",
    "MeSessionType",
    "MetricsUnit",
    "Model",
    "ModelMessageDeltaEvent",
    "ModelMessageEvent",
    "ModelMessageEventContent",
    "ModelMessageEventContentOneItem",
    "ModelMessageEventContentOneItem_Refusal",
    "ModelMessageEventContentOneItem_Text",
    "ModelMessageEventType",
    "ModelMessageUsage",
    "ModelMessageUsageInputTokensBreakdown",
    "ModelParams",
    "ModelProperties",
    "ModelProviderAuth",
    "ModelProviderManifest",
    "ModelProviderManifest_Alibaba",
    "ModelProviderManifest_Anthropic",
    "ModelProviderManifest_Custom",
    "ModelProviderManifest_Fireworks",
    "ModelProviderManifest_GoogleGemini",
    "ModelProviderManifest_Moonshot",
    "ModelProviderManifest_Openai",
    "ModelProviderManifest_Together",
    "ModelProviderManifest_Truefoundry",
    "ModelProviderManifest_Zai",
    "MoonshotModelProvider",
    "OpenAiModelProvider",
    "PreviousTurnIdInput",
    "PreviousTurnIdInputOne",
    "PreviousTurnIdInputZero",
    "RawToolCall",
    "ReasoningEffort",
    "RequestErrorResponse",
    "RequestErrorResponseError",
    "ResourceName",
    "ResponseFormat",
    "ResponseFormatJsonObject",
    "ResponseFormatJsonSchema",
    "ResponseFormatJsonSchemaJsonSchema",
    "ResponseFormatText",
    "ResponseFormat_JsonObject",
    "ResponseFormat_JsonSchema",
    "ResponseFormat_Text",
    "RuntimeConfig",
    "SandboxBuildStatus",
    "SandboxCapability",
    "SandboxConfig",
    "SandboxCreatedEvent",
    "SandboxProviderManifest",
    "SandboxProviderManifestType",
    "Schedule",
    "ScheduleManifest",
    "ScheduleRun",
    "ScheduleRunStatus",
    "ScheduleStatus",
    "Session",
    "SessionAgent",
    "SessionAgentInline",
    "SessionAgentNameRef",
    "SessionAgentReference",
    "SessionAgentSpecBody",
    "SessionAgent_Inline",
    "SessionAgent_Reference",
    "SessionEvent",
    "SessionEventItem",
    "SessionEvent_McpAuthRequired",
    "SessionEvent_McpInitialize",
    "SessionEvent_ModelMessage",
    "SessionEvent_SandboxCreated",
    "SessionEvent_ThreadCreated",
    "SessionEvent_ThreadDone",
    "SessionEvent_ToolApprovalRequired",
    "SessionEvent_ToolResponse",
    "SessionEvent_ToolResponseRequired",
    "SessionEvent_TurnCreated",
    "SessionEvent_TurnDone",
    "SessionMetadata",
    "SessionMetrics",
    "SessionMetricsChart",
    "SessionMetricsChartChartType",
    "SessionMetricsChartDataResponse",
    "SessionMetricsChartName",
    "SessionMetricsChartResponse",
    "SessionMetricsGraph",
    "SessionMetricsGraphChartType",
    "SessionMetricsGraphLine",
    "SessionMetricsMeter",
    "SessionMetricsMeterName",
    "SessionMetricsMeterResponse",
    "SessionMetricsPoint",
    "SettingsCapability",
    "Skill",
    "SkillCapability",
    "SkillManifest",
    "SkillType",
    "TextContent",
    "ThreadCreatedEvent",
    "ThreadDoneEvent",
    "ThreadState",
    "ThreadStateDone",
    "ThreadStateError",
    "ThreadState_Done",
    "ThreadState_Error",
    "Timezone",
    "TogetherAiModelProvider",
    "TokenPagination",
    "ToolApprovalRequiredEvent",
    "ToolCall",
    "ToolCallRef",
    "ToolInfo",
    "ToolInfo_Mcp",
    "ToolInfo_TruefoundrySystem",
    "ToolResponseEvent",
    "ToolResponseRequiredEvent",
    "TrueFoundryModelProvider",
    "TrueFoundrySystemToolInfo",
    "Turn",
    "TurnCreatedEvent",
    "TurnDoneEvent",
    "TurnDoneEventState",
    "TurnDoneEventState_Cancelled",
    "TurnDoneEventState_Done",
    "TurnDoneEventState_Error",
    "TurnInputItem",
    "TurnInputItem_UserMessage",
    "TurnInputItem_UserToolApproval",
    "TurnInputItem_UserToolResponse",
    "TurnMetrics",
    "TurnState",
    "TurnStateCancelled",
    "TurnStateCancelledMetrics",
    "TurnStateCancelledReason",
    "TurnStateDone",
    "TurnStateError",
    "TurnStateErrorMetrics",
    "TurnStateRunning",
    "TurnStateRunningStatus",
    "TurnState_Cancelled",
    "TurnState_Done",
    "TurnState_Error",
    "TurnState_Running",
    "TurnStreamingEvent",
    "TurnStreamingEvent_McpAuthRequired",
    "TurnStreamingEvent_McpInitialize",
    "TurnStreamingEvent_ModelMessage",
    "TurnStreamingEvent_ModelMessageDelta",
    "TurnStreamingEvent_SandboxCreated",
    "TurnStreamingEvent_ThreadCreated",
    "TurnStreamingEvent_ThreadDone",
    "TurnStreamingEvent_ToolApprovalRequired",
    "TurnStreamingEvent_ToolResponse",
    "TurnStreamingEvent_ToolResponseRequired",
    "TurnStreamingEvent_TurnCreated",
    "TurnStreamingEvent_TurnDone",
    "UserMessage",
    "UserMessageContent",
    "UserMessageContentItem",
    "UserMessageContentItem_File",
    "UserMessageContentItem_Text",
    "UserToolApprovalEvent",
    "UserToolResponseEvent",
    "ZaiModelProvider",
]

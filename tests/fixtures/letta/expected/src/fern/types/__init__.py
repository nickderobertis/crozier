



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .agent_environment_variable import AgentEnvironmentVariable
    from .agent_file_attachment import AgentFileAttachment
    from .agent_file_schema import AgentFileSchema
    from .agent_state import AgentState
    from .agent_state_model_settings import (
        AgentStateModelSettings,
        AgentStateModelSettings_Anthropic,
        AgentStateModelSettings_Azure,
        AgentStateModelSettings_Bedrock,
        AgentStateModelSettings_ChatgptOauth,
        AgentStateModelSettings_Deepseek,
        AgentStateModelSettings_GoogleAi,
        AgentStateModelSettings_GoogleVertex,
        AgentStateModelSettings_Groq,
        AgentStateModelSettings_Openai,
        AgentStateModelSettings_Together,
        AgentStateModelSettings_Xai,
        AgentStateModelSettings_Zai,
    )
    from .agent_state_response_format import (
        AgentStateResponseFormat,
        AgentStateResponseFormat_JsonObject,
        AgentStateResponseFormat_JsonSchema,
        AgentStateResponseFormat_Text,
    )
    from .agent_state_tool_rules_item import (
        AgentStateToolRulesItem,
        AgentStateToolRulesItem_Conditional,
        AgentStateToolRulesItem_ConstrainChildTools,
        AgentStateToolRulesItem_ContinueLoop,
        AgentStateToolRulesItem_ExitLoop,
        AgentStateToolRulesItem_MaxCountPerStep,
        AgentStateToolRulesItem_ParentLastTool,
        AgentStateToolRulesItem_RequiredBeforeExit,
        AgentStateToolRulesItem_RequiresApproval,
        AgentStateToolRulesItem_RunFirst,
    )
    from .agent_type import AgentType
    from .annotation import Annotation
    from .annotation_type import AnnotationType
    from .annotation_url_citation import AnnotationUrlCitation
    from .anthropic_model_settings import AnthropicModelSettings
    from .anthropic_model_settings_effort import AnthropicModelSettingsEffort
    from .anthropic_model_settings_response_format import (
        AnthropicModelSettingsResponseFormat,
        AnthropicModelSettingsResponseFormat_JsonObject,
        AnthropicModelSettingsResponseFormat_JsonSchema,
        AnthropicModelSettingsResponseFormat_Text,
    )
    from .anthropic_model_settings_verbosity import AnthropicModelSettingsVerbosity
    from .anthropic_thinking import AnthropicThinking
    from .anthropic_thinking_type import AnthropicThinkingType
    from .approval_create import ApprovalCreate
    from .approval_create_approvals_item import (
        ApprovalCreateApprovalsItem,
        ApprovalCreateApprovalsItem_Approval,
        ApprovalCreateApprovalsItem_Tool,
    )
    from .approval_create_type import ApprovalCreateType
    from .approval_request_message import ApprovalRequestMessage
    from .approval_request_message_message_type import ApprovalRequestMessageMessageType
    from .approval_request_message_tool_call import ApprovalRequestMessageToolCall
    from .approval_request_message_tool_calls import ApprovalRequestMessageToolCalls
    from .approval_response_message import ApprovalResponseMessage
    from .approval_response_message_approvals_item import (
        ApprovalResponseMessageApprovalsItem,
        ApprovalResponseMessageApprovalsItem_Approval,
        ApprovalResponseMessageApprovalsItem_Tool,
    )
    from .approval_return import ApprovalReturn
    from .approval_return_type import ApprovalReturnType
    from .archival_memory_search_response import ArchivalMemorySearchResponse
    from .archival_memory_search_result import ArchivalMemorySearchResult
    from .archive import Archive
    from .assistant_message import AssistantMessage
    from .assistant_message_content import AssistantMessageContent
    from .assistant_message_list_result import AssistantMessageListResult
    from .assistant_message_list_result_content import AssistantMessageListResultContent
    from .audio import Audio
    from .auth_request import AuthRequest
    from .auth_response import AuthResponse
    from .azure_model_settings import AzureModelSettings
    from .azure_model_settings_response_format import (
        AzureModelSettingsResponseFormat,
        AzureModelSettingsResponseFormat_JsonObject,
        AzureModelSettingsResponseFormat_JsonSchema,
        AzureModelSettingsResponseFormat_Text,
    )
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_error_code import BadRequestErrorBodyErrorCode
    from .base64image import Base64Image
    from .base_tool_rule_schema import BaseToolRuleSchema
    from .batch_job import BatchJob
    from .bedrock_model_settings import BedrockModelSettings
    from .bedrock_model_settings_response_format import (
        BedrockModelSettingsResponseFormat,
        BedrockModelSettingsResponseFormat_JsonObject,
        BedrockModelSettingsResponseFormat_JsonSchema,
        BedrockModelSettingsResponseFormat_Text,
    )
    from .block import Block
    from .block_response import BlockResponse
    from .block_schema import BlockSchema
    from .block_update import BlockUpdate
    from .body_export_agent import BodyExportAgent
    from .chat_completion import ChatCompletion
    from .chat_completion_assistant_message_param import ChatCompletionAssistantMessageParam
    from .chat_completion_assistant_message_param_content import ChatCompletionAssistantMessageParamContent
    from .chat_completion_assistant_message_param_content_one_item import (
        ChatCompletionAssistantMessageParamContentOneItem,
        ChatCompletionAssistantMessageParamContentOneItem_Refusal,
        ChatCompletionAssistantMessageParamContentOneItem_Text,
    )
    from .chat_completion_assistant_message_param_tool_calls_item import (
        ChatCompletionAssistantMessageParamToolCallsItem,
        ChatCompletionAssistantMessageParamToolCallsItem_Custom,
        ChatCompletionAssistantMessageParamToolCallsItem_Function,
    )
    from .chat_completion_audio import ChatCompletionAudio
    from .chat_completion_content_part_image_param import ChatCompletionContentPartImageParam
    from .chat_completion_content_part_input_audio_param import ChatCompletionContentPartInputAudioParam
    from .chat_completion_content_part_refusal_param import ChatCompletionContentPartRefusalParam
    from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
    from .chat_completion_content_part_text_param_type import ChatCompletionContentPartTextParamType
    from .chat_completion_developer_message_param import ChatCompletionDeveloperMessageParam
    from .chat_completion_developer_message_param_content import ChatCompletionDeveloperMessageParamContent
    from .chat_completion_function_message_param import ChatCompletionFunctionMessageParam
    from .chat_completion_message import ChatCompletionMessage
    from .chat_completion_message_custom_tool_call import ChatCompletionMessageCustomToolCall
    from .chat_completion_message_custom_tool_call_param import ChatCompletionMessageCustomToolCallParam
    from .chat_completion_message_function_tool_call_input import ChatCompletionMessageFunctionToolCallInput
    from .chat_completion_message_function_tool_call_input_type import ChatCompletionMessageFunctionToolCallInputType
    from .chat_completion_message_function_tool_call_output import ChatCompletionMessageFunctionToolCallOutput
    from .chat_completion_message_function_tool_call_output_type import ChatCompletionMessageFunctionToolCallOutputType
    from .chat_completion_message_function_tool_call_param import ChatCompletionMessageFunctionToolCallParam
    from .chat_completion_message_role import ChatCompletionMessageRole
    from .chat_completion_message_tool_calls_item import (
        ChatCompletionMessageToolCallsItem,
        ChatCompletionMessageToolCallsItem_Custom,
        ChatCompletionMessageToolCallsItem_Function,
    )
    from .chat_completion_object import ChatCompletionObject
    from .chat_completion_service_tier import ChatCompletionServiceTier
    from .chat_completion_system_message_param import ChatCompletionSystemMessageParam
    from .chat_completion_system_message_param_content import ChatCompletionSystemMessageParamContent
    from .chat_completion_token_logprob import ChatCompletionTokenLogprob
    from .chat_completion_tool_message_param import ChatCompletionToolMessageParam
    from .chat_completion_tool_message_param_content import ChatCompletionToolMessageParamContent
    from .chat_completion_user_message_param import ChatCompletionUserMessageParam
    from .chat_completion_user_message_param_content import ChatCompletionUserMessageParamContent
    from .chat_completion_user_message_param_content_one_item import (
        ChatCompletionUserMessageParamContentOneItem,
        ChatCompletionUserMessageParamContentOneItem_File,
        ChatCompletionUserMessageParamContentOneItem_ImageUrl,
        ChatCompletionUserMessageParamContentOneItem_InputAudio,
        ChatCompletionUserMessageParamContentOneItem_Text,
    )
    from .chat_gpto_auth_model_settings import ChatGptoAuthModelSettings
    from .chat_gpto_auth_reasoning import ChatGptoAuthReasoning
    from .chat_gpto_auth_reasoning_reasoning_effort import ChatGptoAuthReasoningReasoningEffort
    from .child_tool_rule import ChildToolRule
    from .child_tool_rule_schema import ChildToolRuleSchema
    from .choice import Choice
    from .choice_finish_reason import ChoiceFinishReason
    from .choice_logprobs import ChoiceLogprobs
    from .client_tool_schema import ClientToolSchema
    from .code_input import CodeInput
    from .compaction_request import CompactionRequest
    from .compaction_response import CompactionResponse
    from .compaction_settings_input import CompactionSettingsInput
    from .compaction_settings_input_mode import CompactionSettingsInputMode
    from .compaction_settings_input_model_settings import (
        CompactionSettingsInputModelSettings,
        CompactionSettingsInputModelSettings_Anthropic,
        CompactionSettingsInputModelSettings_Azure,
        CompactionSettingsInputModelSettings_Bedrock,
        CompactionSettingsInputModelSettings_ChatgptOauth,
        CompactionSettingsInputModelSettings_Deepseek,
        CompactionSettingsInputModelSettings_GoogleAi,
        CompactionSettingsInputModelSettings_GoogleVertex,
        CompactionSettingsInputModelSettings_Groq,
        CompactionSettingsInputModelSettings_Openai,
        CompactionSettingsInputModelSettings_Together,
        CompactionSettingsInputModelSettings_Xai,
        CompactionSettingsInputModelSettings_Zai,
    )
    from .compaction_settings_output import CompactionSettingsOutput
    from .compaction_settings_output_mode import CompactionSettingsOutputMode
    from .compaction_settings_output_model_settings import (
        CompactionSettingsOutputModelSettings,
        CompactionSettingsOutputModelSettings_Anthropic,
        CompactionSettingsOutputModelSettings_Azure,
        CompactionSettingsOutputModelSettings_Bedrock,
        CompactionSettingsOutputModelSettings_ChatgptOauth,
        CompactionSettingsOutputModelSettings_Deepseek,
        CompactionSettingsOutputModelSettings_GoogleAi,
        CompactionSettingsOutputModelSettings_GoogleVertex,
        CompactionSettingsOutputModelSettings_Groq,
        CompactionSettingsOutputModelSettings_Openai,
        CompactionSettingsOutputModelSettings_Together,
        CompactionSettingsOutputModelSettings_Xai,
        CompactionSettingsOutputModelSettings_Zai,
    )
    from .comparison_operator import ComparisonOperator
    from .completion_tokens_details import CompletionTokensDetails
    from .completion_usage import CompletionUsage
    from .conditional_tool_rule import ConditionalToolRule
    from .conditional_tool_rule_schema import ConditionalToolRuleSchema
    from .conflict_error_body import ConflictErrorBody
    from .context_window_overview import ContextWindowOverview
    from .continue_tool_rule import ContinueToolRule
    from .conversation import Conversation
    from .core_memory_block_schema import CoreMemoryBlockSchema
    from .create_block import CreateBlock
    from .create_ssemcp_server import CreateSsemcpServer
    from .create_stdio_mcp_server import CreateStdioMcpServer
    from .create_streamable_httpmcp_server import CreateStreamableHttpmcpServer
    from .custom_input import CustomInput
    from .custom_output import CustomOutput
    from .deepseek_model_settings import DeepseekModelSettings
    from .deepseek_model_settings_response_format import (
        DeepseekModelSettingsResponseFormat,
        DeepseekModelSettingsResponseFormat_JsonObject,
        DeepseekModelSettingsResponseFormat_JsonSchema,
        DeepseekModelSettingsResponseFormat_Text,
    )
    from .delete_deployment_response import DeleteDeploymentResponse
    from .deployment_entity import DeploymentEntity
    from .duplicate_file_handling import DuplicateFileHandling
    from .dynamic_manager import DynamicManager
    from .dynamic_manager_update import DynamicManagerUpdate
    from .e2b_sandbox_config import E2BSandboxConfig
    from .embedding_config import EmbeddingConfig
    from .embedding_config_embedding_endpoint_type import EmbeddingConfigEmbeddingEndpointType
    from .embedding_model import EmbeddingModel
    from .embedding_model_embedding_endpoint_type import EmbeddingModelEmbeddingEndpointType
    from .embedding_model_model_type import EmbeddingModelModelType
    from .event_message import EventMessage
    from .event_message_event_type import EventMessageEventType
    from .feedback_type import FeedbackType
    from .feeds_list_feeds_request_offset import FeedsListFeedsRequestOffset
    from .feeds_list_subscriptions_request_offset import FeedsListSubscriptionsRequestOffset
    from .file import File
    from .file_agent_schema import FileAgentSchema
    from .file_block import FileBlock
    from .file_file import FileFile
    from .file_metadata import FileMetadata
    from .file_processing_status import FileProcessingStatus
    from .file_schema import FileSchema
    from .file_stats import FileStats
    from .folder import Folder
    from .function_call_input import FunctionCallInput
    from .function_call_output import FunctionCallOutput
    from .function_definition import FunctionDefinition
    from .function_output import FunctionOutput
    from .function_tool import FunctionTool
    from .function_tool_type import FunctionToolType
    from .gemini_thinking_config import GeminiThinkingConfig
    from .generate_tool_input import GenerateToolInput
    from .generate_tool_output import GenerateToolOutput
    from .google_ai_model_settings import GoogleAiModelSettings
    from .google_ai_model_settings_response_schema import (
        GoogleAiModelSettingsResponseSchema,
        GoogleAiModelSettingsResponseSchema_JsonObject,
        GoogleAiModelSettingsResponseSchema_JsonSchema,
        GoogleAiModelSettingsResponseSchema_Text,
    )
    from .google_vertex_model_settings import GoogleVertexModelSettings
    from .google_vertex_model_settings_response_schema import (
        GoogleVertexModelSettingsResponseSchema,
        GoogleVertexModelSettingsResponseSchema_JsonObject,
        GoogleVertexModelSettingsResponseSchema_JsonSchema,
        GoogleVertexModelSettingsResponseSchema_Text,
    )
    from .groq_model_settings import GroqModelSettings
    from .groq_model_settings_response_format import (
        GroqModelSettingsResponseFormat,
        GroqModelSettingsResponseFormat_JsonObject,
        GroqModelSettingsResponseFormat_JsonSchema,
        GroqModelSettingsResponseFormat_Text,
    )
    from .group import Group
    from .group_schema import GroupSchema
    from .group_schema_manager_config import (
        GroupSchemaManagerConfig,
        GroupSchemaManagerConfig_Dynamic,
        GroupSchemaManagerConfig_RoundRobin,
        GroupSchemaManagerConfig_Sleeptime,
        GroupSchemaManagerConfig_Supervisor,
        GroupSchemaManagerConfig_VoiceSleeptime,
    )
    from .health import Health
    from .hidden_reasoning_message import HiddenReasoningMessage
    from .hidden_reasoning_message_state import HiddenReasoningMessageState
    from .http_validation_error import HttpValidationError
    from .identity import Identity
    from .identity_property import IdentityProperty
    from .identity_property_type import IdentityPropertyType
    from .identity_property_value import IdentityPropertyValue
    from .identity_type import IdentityType
    from .image_content import ImageContent
    from .image_content_source import (
        ImageContentSource,
        ImageContentSource_Base64,
        ImageContentSource_Letta,
        ImageContentSource_Url,
    )
    from .image_url import ImageUrl
    from .image_url_detail import ImageUrlDetail
    from .imported_agents_response import ImportedAgentsResponse
    from .init_tool_rule import InitToolRule
    from .input_audio import InputAudio
    from .input_audio_format import InputAudioFormat
    from .internal_server_error_body import InternalServerErrorBody
    from .internal_template_block_create import InternalTemplateBlockCreate
    from .job import Job
    from .job_status import JobStatus
    from .job_type import JobType
    from .json_object_response_format import JsonObjectResponseFormat
    from .json_schema_response_format import JsonSchemaResponseFormat
    from .letta_assistant_message_content_union import (
        LettaAssistantMessageContentUnion,
        LettaAssistantMessageContentUnion_Text,
    )
    from .letta_batch_messages import LettaBatchMessages
    from .letta_batch_request import LettaBatchRequest
    from .letta_batch_request_input import LettaBatchRequestInput
    from .letta_batch_request_input_one_item import (
        LettaBatchRequestInputOneItem,
        LettaBatchRequestInputOneItem_Image,
        LettaBatchRequestInputOneItem_OmittedReasoning,
        LettaBatchRequestInputOneItem_Reasoning,
        LettaBatchRequestInputOneItem_RedactedReasoning,
        LettaBatchRequestInputOneItem_SummarizedReasoning,
        LettaBatchRequestInputOneItem_Text,
        LettaBatchRequestInputOneItem_ToolCall,
        LettaBatchRequestInputOneItem_ToolReturn,
    )
    from .letta_batch_request_messages_item import LettaBatchRequestMessagesItem
    from .letta_error_message import LettaErrorMessage
    from .letta_image import LettaImage
    from .letta_message_content_union import (
        LettaMessageContentUnion,
        LettaMessageContentUnion_Image,
        LettaMessageContentUnion_OmittedReasoning,
        LettaMessageContentUnion_Reasoning,
        LettaMessageContentUnion_RedactedReasoning,
        LettaMessageContentUnion_Text,
        LettaMessageContentUnion_ToolCall,
        LettaMessageContentUnion_ToolReturn,
    )
    from .letta_message_union import (
        LettaMessageUnion,
        LettaMessageUnion_ApprovalRequestMessage,
        LettaMessageUnion_ApprovalResponseMessage,
        LettaMessageUnion_AssistantMessage,
        LettaMessageUnion_Event,
        LettaMessageUnion_HiddenReasoningMessage,
        LettaMessageUnion_ReasoningMessage,
        LettaMessageUnion_Summary,
        LettaMessageUnion_SystemMessage,
        LettaMessageUnion_ToolCallMessage,
        LettaMessageUnion_ToolReturnMessage,
        LettaMessageUnion_UserMessage,
    )
    from .letta_ping import LettaPing
    from .letta_request import LettaRequest
    from .letta_request_config import LettaRequestConfig
    from .letta_request_input import LettaRequestInput
    from .letta_request_input_one_item import (
        LettaRequestInputOneItem,
        LettaRequestInputOneItem_Image,
        LettaRequestInputOneItem_OmittedReasoning,
        LettaRequestInputOneItem_Reasoning,
        LettaRequestInputOneItem_RedactedReasoning,
        LettaRequestInputOneItem_SummarizedReasoning,
        LettaRequestInputOneItem_Text,
        LettaRequestInputOneItem_ToolCall,
        LettaRequestInputOneItem_ToolReturn,
    )
    from .letta_request_messages_item import LettaRequestMessagesItem
    from .letta_response import LettaResponse
    from .letta_schemas_agent_file_agent_schema import LettaSchemasAgentFileAgentSchema
    from .letta_schemas_agent_file_agent_schema_model_settings import (
        LettaSchemasAgentFileAgentSchemaModelSettings,
        LettaSchemasAgentFileAgentSchemaModelSettings_Anthropic,
        LettaSchemasAgentFileAgentSchemaModelSettings_Azure,
        LettaSchemasAgentFileAgentSchemaModelSettings_Bedrock,
        LettaSchemasAgentFileAgentSchemaModelSettings_ChatgptOauth,
        LettaSchemasAgentFileAgentSchemaModelSettings_Deepseek,
        LettaSchemasAgentFileAgentSchemaModelSettings_GoogleAi,
        LettaSchemasAgentFileAgentSchemaModelSettings_GoogleVertex,
        LettaSchemasAgentFileAgentSchemaModelSettings_Groq,
        LettaSchemasAgentFileAgentSchemaModelSettings_Openai,
        LettaSchemasAgentFileAgentSchemaModelSettings_Together,
        LettaSchemasAgentFileAgentSchemaModelSettings_Xai,
        LettaSchemasAgentFileAgentSchemaModelSettings_Zai,
    )
    from .letta_schemas_agent_file_agent_schema_response_format import (
        LettaSchemasAgentFileAgentSchemaResponseFormat,
        LettaSchemasAgentFileAgentSchemaResponseFormat_JsonObject,
        LettaSchemasAgentFileAgentSchemaResponseFormat_JsonSchema,
        LettaSchemasAgentFileAgentSchemaResponseFormat_Text,
    )
    from .letta_schemas_agent_file_agent_schema_tool_rules_item import (
        LettaSchemasAgentFileAgentSchemaToolRulesItem,
        LettaSchemasAgentFileAgentSchemaToolRulesItem_Conditional,
        LettaSchemasAgentFileAgentSchemaToolRulesItem_ConstrainChildTools,
        LettaSchemasAgentFileAgentSchemaToolRulesItem_ContinueLoop,
        LettaSchemasAgentFileAgentSchemaToolRulesItem_ExitLoop,
        LettaSchemasAgentFileAgentSchemaToolRulesItem_MaxCountPerStep,
        LettaSchemasAgentFileAgentSchemaToolRulesItem_ParentLastTool,
        LettaSchemasAgentFileAgentSchemaToolRulesItem_RequiredBeforeExit,
        LettaSchemasAgentFileAgentSchemaToolRulesItem_RequiresApproval,
        LettaSchemasAgentFileAgentSchemaToolRulesItem_RunFirst,
    )
    from .letta_schemas_agent_file_message_schema import LettaSchemasAgentFileMessageSchema
    from .letta_schemas_agent_file_message_schema_approvals_item import LettaSchemasAgentFileMessageSchemaApprovalsItem
    from .letta_schemas_agent_file_message_schema_content import LettaSchemasAgentFileMessageSchemaContent
    from .letta_schemas_agent_file_message_schema_type import LettaSchemasAgentFileMessageSchemaType
    from .letta_schemas_agent_file_tool_schema import LettaSchemasAgentFileToolSchema
    from .letta_schemas_letta_message_tool_return import LettaSchemasLettaMessageToolReturn
    from .letta_schemas_letta_message_tool_return_status import LettaSchemasLettaMessageToolReturnStatus
    from .letta_schemas_letta_message_tool_return_tool_return import LettaSchemasLettaMessageToolReturnToolReturn
    from .letta_schemas_letta_message_tool_return_type import LettaSchemasLettaMessageToolReturnType
    from .letta_schemas_mcp_server_tool_execute_request import LettaSchemasMcpServerToolExecuteRequest
    from .letta_schemas_mcp_server_update_ssemcp_server import LettaSchemasMcpServerUpdateSsemcpServer
    from .letta_schemas_mcp_server_update_stdio_mcp_server import LettaSchemasMcpServerUpdateStdioMcpServer
    from .letta_schemas_mcp_server_update_streamable_httpmcp_server import (
        LettaSchemasMcpServerUpdateStreamableHttpmcpServer,
    )
    from .letta_schemas_mcp_update_ssemcp_server import LettaSchemasMcpUpdateSsemcpServer
    from .letta_schemas_mcp_update_stdio_mcp_server import LettaSchemasMcpUpdateStdioMcpServer
    from .letta_schemas_mcp_update_streamable_httpmcp_server import LettaSchemasMcpUpdateStreamableHttpmcpServer
    from .letta_schemas_message_tool_return_input import LettaSchemasMessageToolReturnInput
    from .letta_schemas_message_tool_return_input_func_response import LettaSchemasMessageToolReturnInputFuncResponse
    from .letta_schemas_message_tool_return_input_func_response_one_item import (
        LettaSchemasMessageToolReturnInputFuncResponseOneItem,
        LettaSchemasMessageToolReturnInputFuncResponseOneItem_Image,
        LettaSchemasMessageToolReturnInputFuncResponseOneItem_Text,
    )
    from .letta_schemas_message_tool_return_input_status import LettaSchemasMessageToolReturnInputStatus
    from .letta_schemas_message_tool_return_output import LettaSchemasMessageToolReturnOutput
    from .letta_schemas_message_tool_return_output_func_response import LettaSchemasMessageToolReturnOutputFuncResponse
    from .letta_schemas_message_tool_return_output_func_response_one_item import (
        LettaSchemasMessageToolReturnOutputFuncResponseOneItem,
        LettaSchemasMessageToolReturnOutputFuncResponseOneItem_Image,
        LettaSchemasMessageToolReturnOutputFuncResponseOneItem_Text,
    )
    from .letta_schemas_message_tool_return_output_status import LettaSchemasMessageToolReturnOutputStatus
    from .letta_serialize_schemas_pydantic_agent_schema_agent_schema import (
        LettaSerializeSchemasPydanticAgentSchemaAgentSchema,
    )
    from .letta_serialize_schemas_pydantic_agent_schema_agent_schema_tool_rules_item import (
        LettaSerializeSchemasPydanticAgentSchemaAgentSchemaToolRulesItem,
    )
    from .letta_serialize_schemas_pydantic_agent_schema_message_schema import (
        LettaSerializeSchemasPydanticAgentSchemaMessageSchema,
    )
    from .letta_serialize_schemas_pydantic_agent_schema_tool_schema import (
        LettaSerializeSchemasPydanticAgentSchemaToolSchema,
    )
    from .letta_stop_reason import LettaStopReason
    from .letta_stop_reason_message_type import LettaStopReasonMessageType
    from .letta_streaming_request import LettaStreamingRequest
    from .letta_streaming_request_input import LettaStreamingRequestInput
    from .letta_streaming_request_input_one_item import (
        LettaStreamingRequestInputOneItem,
        LettaStreamingRequestInputOneItem_Image,
        LettaStreamingRequestInputOneItem_OmittedReasoning,
        LettaStreamingRequestInputOneItem_Reasoning,
        LettaStreamingRequestInputOneItem_RedactedReasoning,
        LettaStreamingRequestInputOneItem_SummarizedReasoning,
        LettaStreamingRequestInputOneItem_Text,
        LettaStreamingRequestInputOneItem_ToolCall,
        LettaStreamingRequestInputOneItem_ToolReturn,
    )
    from .letta_streaming_request_messages_item import LettaStreamingRequestMessagesItem
    from .letta_streaming_response import (
        LettaStreamingResponse,
        LettaStreamingResponse_ApprovalRequestMessage,
        LettaStreamingResponse_ApprovalResponseMessage,
        LettaStreamingResponse_AssistantMessage,
        LettaStreamingResponse_ErrorMessage,
        LettaStreamingResponse_HiddenReasoningMessage,
        LettaStreamingResponse_Ping,
        LettaStreamingResponse_ReasoningMessage,
        LettaStreamingResponse_StopReason,
        LettaStreamingResponse_SystemMessage,
        LettaStreamingResponse_ToolCallMessage,
        LettaStreamingResponse_ToolReturnMessage,
        LettaStreamingResponse_UsageStatistics,
        LettaStreamingResponse_UserMessage,
    )
    from .letta_tool_return_content_union import (
        LettaToolReturnContentUnion,
        LettaToolReturnContentUnion_Image,
        LettaToolReturnContentUnion_Text,
    )
    from .letta_usage_statistics import LettaUsageStatistics
    from .letta_usage_statistics_message_type import LettaUsageStatisticsMessageType
    from .letta_user_message_content_union import (
        LettaUserMessageContentUnion,
        LettaUserMessageContentUnion_Image,
        LettaUserMessageContentUnion_Text,
    )
    from .list_deployment_entities_response import ListDeploymentEntitiesResponse
    from .llm_config import LlmConfig
    from .llm_config_compatibility_type import LlmConfigCompatibilityType
    from .llm_config_effort import LlmConfigEffort
    from .llm_config_model_endpoint_type import LlmConfigModelEndpointType
    from .llm_config_reasoning_effort import LlmConfigReasoningEffort
    from .llm_config_response_format import (
        LlmConfigResponseFormat,
        LlmConfigResponseFormat_JsonObject,
        LlmConfigResponseFormat_JsonSchema,
        LlmConfigResponseFormat_Text,
    )
    from .llm_config_verbosity import LlmConfigVerbosity
    from .local_sandbox_config import LocalSandboxConfig
    from .manager_type import ManagerType
    from .max_count_per_step_tool_rule import MaxCountPerStepToolRule
    from .max_count_per_step_tool_rule_schema import MaxCountPerStepToolRuleSchema
    from .mcp_server_schema import McpServerSchema
    from .mcp_server_type import McpServerType
    from .mcp_tool import McpTool
    from .mcp_tool_health import McpToolHealth
    from .memory import Memory
    from .memory_agent_type import MemoryAgentType
    from .message import Message
    from .message_approvals_item import MessageApprovalsItem
    from .message_content_item import (
        MessageContentItem,
        MessageContentItem_Image,
        MessageContentItem_OmittedReasoning,
        MessageContentItem_Reasoning,
        MessageContentItem_RedactedReasoning,
        MessageContentItem_SummarizedReasoning,
        MessageContentItem_Text,
        MessageContentItem_ToolCall,
        MessageContentItem_ToolReturn,
    )
    from .message_create import MessageCreate
    from .message_create_content import MessageCreateContent
    from .message_create_role import MessageCreateRole
    from .message_create_type import MessageCreateType
    from .message_role import MessageRole
    from .message_search_result import MessageSearchResult
    from .message_type import MessageType
    from .modal_sandbox_config import ModalSandboxConfig
    from .modal_sandbox_config_language import ModalSandboxConfigLanguage
    from .model import Model
    from .model_compatibility_type import ModelCompatibilityType
    from .model_effort import ModelEffort
    from .model_model_endpoint_type import ModelModelEndpointType
    from .model_model_type import ModelModelType
    from .model_reasoning_effort import ModelReasoningEffort
    from .model_response_format import (
        ModelResponseFormat,
        ModelResponseFormat_JsonObject,
        ModelResponseFormat_JsonSchema,
        ModelResponseFormat_Text,
    )
    from .model_verbosity import ModelVerbosity
    from .modify_approval_request import ModifyApprovalRequest
    from .not_found_error_body import NotFoundErrorBody
    from .not_found_error_body_error_code import NotFoundErrorBodyErrorCode
    from .not_found_error_body_message import NotFoundErrorBodyMessage
    from .npm_requirement import NpmRequirement
    from .omitted_reasoning_content import OmittedReasoningContent
    from .open_ai_model_settings import OpenAiModelSettings
    from .open_ai_model_settings_response_format import (
        OpenAiModelSettingsResponseFormat,
        OpenAiModelSettingsResponseFormat_JsonObject,
        OpenAiModelSettingsResponseFormat_JsonSchema,
        OpenAiModelSettingsResponseFormat_Text,
    )
    from .open_ai_reasoning import OpenAiReasoning
    from .open_ai_reasoning_reasoning_effort import OpenAiReasoningReasoningEffort
    from .openai_types_chat_chat_completion_message_function_tool_call_function import (
        OpenaiTypesChatChatCompletionMessageFunctionToolCallFunction,
    )
    from .openai_types_chat_chat_completion_message_function_tool_call_param_function import (
        OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction,
    )
    from .organization import Organization
    from .organization_create import OrganizationCreate
    from .organization_sources_stats import OrganizationSourcesStats
    from .organization_update import OrganizationUpdate
    from .paginated_agent_files import PaginatedAgentFiles
    from .parameter_properties import ParameterProperties
    from .parameters_schema import ParametersSchema
    from .parent_tool_rule import ParentToolRule
    from .passage import Passage
    from .passage_search_result import PassageSearchResult
    from .payment_required_error_body import PaymentRequiredErrorBody
    from .pip_requirement import PipRequirement
    from .pipelines_list_pipelines_request_offset import PipelinesListPipelinesRequestOffset
    from .projects_list_projects_request_offset import ProjectsListProjectsRequestOffset
    from .prompt_tokens_details import PromptTokensDetails
    from .provider import Provider
    from .provider_category import ProviderCategory
    from .provider_trace import ProviderTrace
    from .provider_type import ProviderType
    from .reasoning_content import ReasoningContent
    from .reasoning_message import ReasoningMessage
    from .reasoning_message_list_result import ReasoningMessageListResult
    from .reasoning_message_source import ReasoningMessageSource
    from .redacted_reasoning_content import RedactedReasoningContent
    from .required_before_exit_tool_rule import RequiredBeforeExitToolRule
    from .requires_approval_tool_rule import RequiresApprovalToolRule
    from .retrieve_stream_request import RetrieveStreamRequest
    from .round_robin_manager import RoundRobinManager
    from .round_robin_manager_update import RoundRobinManagerUpdate
    from .run import Run
    from .run_metrics import RunMetrics
    from .run_status import RunStatus
    from .sandbox_config import SandboxConfig
    from .sandbox_config_create import SandboxConfigCreate
    from .sandbox_config_create_config import SandboxConfigCreateConfig
    from .sandbox_config_update import SandboxConfigUpdate
    from .sandbox_config_update_config import SandboxConfigUpdateConfig
    from .sandbox_environment_variable import SandboxEnvironmentVariable
    from .sandbox_environment_variable_create import SandboxEnvironmentVariableCreate
    from .sandbox_environment_variable_update import SandboxEnvironmentVariableUpdate
    from .sandbox_type import SandboxType
    from .sleeptime_manager import SleeptimeManager
    from .sleeptime_manager_update import SleeptimeManagerUpdate
    from .source import Source
    from .source_create import SourceCreate
    from .source_schema import SourceSchema
    from .source_stats import SourceStats
    from .source_update import SourceUpdate
    from .sse_server_config import SseServerConfig
    from .ssemcp_server import SsemcpServer
    from .stdio_mcp_server import StdioMcpServer
    from .stdio_server_config import StdioServerConfig
    from .step import Step
    from .step_feedback import StepFeedback
    from .step_metrics import StepMetrics
    from .step_status import StepStatus
    from .stop_reason_type import StopReasonType
    from .streamable_http_server_config import StreamableHttpServerConfig
    from .streamable_httpmcp_server import StreamableHttpmcpServer
    from .summarized_reasoning_content import SummarizedReasoningContent
    from .summarized_reasoning_content_part import SummarizedReasoningContentPart
    from .summary_message import SummaryMessage
    from .supervisor_manager import SupervisorManager
    from .supervisor_manager_update import SupervisorManagerUpdate
    from .system_message import SystemMessage
    from .system_message_list_result import SystemMessageListResult
    from .tag_schema import TagSchema
    from .templates_list_template_versions_request_offset import TemplatesListTemplateVersionsRequestOffset
    from .templates_list_templates_request_offset import TemplatesListTemplatesRequestOffset
    from .terminal_tool_rule import TerminalToolRule
    from .text_content import TextContent
    from .text_response_format import TextResponseFormat
    from .together_model_settings import TogetherModelSettings
    from .together_model_settings_response_format import (
        TogetherModelSettingsResponseFormat,
        TogetherModelSettingsResponseFormat_JsonObject,
        TogetherModelSettingsResponseFormat_JsonSchema,
        TogetherModelSettingsResponseFormat_Text,
    )
    from .tool import Tool
    from .tool_annotations import ToolAnnotations
    from .tool_call import ToolCall
    from .tool_call_content import ToolCallContent
    from .tool_call_delta import ToolCallDelta
    from .tool_call_message import ToolCallMessage
    from .tool_call_message_tool_call import ToolCallMessageToolCall
    from .tool_call_message_tool_calls import ToolCallMessageToolCalls
    from .tool_call_node import ToolCallNode
    from .tool_create import ToolCreate
    from .tool_env_var_schema import ToolEnvVarSchema
    from .tool_execution_result import ToolExecutionResult
    from .tool_execution_result_status import ToolExecutionResultStatus
    from .tool_json_schema import ToolJsonSchema
    from .tool_return_content import ToolReturnContent
    from .tool_return_message import ToolReturnMessage
    from .tool_return_message_message_type import ToolReturnMessageMessageType
    from .tool_return_message_status import ToolReturnMessageStatus
    from .tool_search_result import ToolSearchResult
    from .tool_type import ToolType
    from .top_logprob import TopLogprob
    from .update_assistant_message import UpdateAssistantMessage
    from .update_assistant_message_content import UpdateAssistantMessageContent
    from .update_reasoning_message import UpdateReasoningMessage
    from .update_system_message import UpdateSystemMessage
    from .update_user_message import UpdateUserMessage
    from .update_user_message_content import UpdateUserMessageContent
    from .url_image import UrlImage
    from .usage_statistics import UsageStatistics
    from .usage_statistics_completion_token_details import UsageStatisticsCompletionTokenDetails
    from .usage_statistics_prompt_token_details import UsageStatisticsPromptTokenDetails
    from .user import User
    from .user_create import UserCreate
    from .user_message import UserMessage
    from .user_message_content import UserMessageContent
    from .user_message_list_result import UserMessageListResult
    from .user_message_list_result_content import UserMessageListResultContent
    from .user_update import UserUpdate
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .vector_db_provider import VectorDbProvider
    from .voice_sleeptime_manager import VoiceSleeptimeManager
    from .voice_sleeptime_manager_update import VoiceSleeptimeManagerUpdate
    from .xai_model_settings import XaiModelSettings
    from .xai_model_settings_response_format import (
        XaiModelSettingsResponseFormat,
        XaiModelSettingsResponseFormat_JsonObject,
        XaiModelSettingsResponseFormat_JsonSchema,
        XaiModelSettingsResponseFormat_Text,
    )
    from .zai_model_settings import ZaiModelSettings
    from .zai_model_settings_response_format import (
        ZaiModelSettingsResponseFormat,
        ZaiModelSettingsResponseFormat_JsonObject,
        ZaiModelSettingsResponseFormat_JsonSchema,
        ZaiModelSettingsResponseFormat_Text,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AgentEnvironmentVariable": ".agent_environment_variable",
    "AgentFileAttachment": ".agent_file_attachment",
    "AgentFileSchema": ".agent_file_schema",
    "AgentState": ".agent_state",
    "AgentStateModelSettings": ".agent_state_model_settings",
    "AgentStateModelSettings_Anthropic": ".agent_state_model_settings",
    "AgentStateModelSettings_Azure": ".agent_state_model_settings",
    "AgentStateModelSettings_Bedrock": ".agent_state_model_settings",
    "AgentStateModelSettings_ChatgptOauth": ".agent_state_model_settings",
    "AgentStateModelSettings_Deepseek": ".agent_state_model_settings",
    "AgentStateModelSettings_GoogleAi": ".agent_state_model_settings",
    "AgentStateModelSettings_GoogleVertex": ".agent_state_model_settings",
    "AgentStateModelSettings_Groq": ".agent_state_model_settings",
    "AgentStateModelSettings_Openai": ".agent_state_model_settings",
    "AgentStateModelSettings_Together": ".agent_state_model_settings",
    "AgentStateModelSettings_Xai": ".agent_state_model_settings",
    "AgentStateModelSettings_Zai": ".agent_state_model_settings",
    "AgentStateResponseFormat": ".agent_state_response_format",
    "AgentStateResponseFormat_JsonObject": ".agent_state_response_format",
    "AgentStateResponseFormat_JsonSchema": ".agent_state_response_format",
    "AgentStateResponseFormat_Text": ".agent_state_response_format",
    "AgentStateToolRulesItem": ".agent_state_tool_rules_item",
    "AgentStateToolRulesItem_Conditional": ".agent_state_tool_rules_item",
    "AgentStateToolRulesItem_ConstrainChildTools": ".agent_state_tool_rules_item",
    "AgentStateToolRulesItem_ContinueLoop": ".agent_state_tool_rules_item",
    "AgentStateToolRulesItem_ExitLoop": ".agent_state_tool_rules_item",
    "AgentStateToolRulesItem_MaxCountPerStep": ".agent_state_tool_rules_item",
    "AgentStateToolRulesItem_ParentLastTool": ".agent_state_tool_rules_item",
    "AgentStateToolRulesItem_RequiredBeforeExit": ".agent_state_tool_rules_item",
    "AgentStateToolRulesItem_RequiresApproval": ".agent_state_tool_rules_item",
    "AgentStateToolRulesItem_RunFirst": ".agent_state_tool_rules_item",
    "AgentType": ".agent_type",
    "Annotation": ".annotation",
    "AnnotationType": ".annotation_type",
    "AnnotationUrlCitation": ".annotation_url_citation",
    "AnthropicModelSettings": ".anthropic_model_settings",
    "AnthropicModelSettingsEffort": ".anthropic_model_settings_effort",
    "AnthropicModelSettingsResponseFormat": ".anthropic_model_settings_response_format",
    "AnthropicModelSettingsResponseFormat_JsonObject": ".anthropic_model_settings_response_format",
    "AnthropicModelSettingsResponseFormat_JsonSchema": ".anthropic_model_settings_response_format",
    "AnthropicModelSettingsResponseFormat_Text": ".anthropic_model_settings_response_format",
    "AnthropicModelSettingsVerbosity": ".anthropic_model_settings_verbosity",
    "AnthropicThinking": ".anthropic_thinking",
    "AnthropicThinkingType": ".anthropic_thinking_type",
    "ApprovalCreate": ".approval_create",
    "ApprovalCreateApprovalsItem": ".approval_create_approvals_item",
    "ApprovalCreateApprovalsItem_Approval": ".approval_create_approvals_item",
    "ApprovalCreateApprovalsItem_Tool": ".approval_create_approvals_item",
    "ApprovalCreateType": ".approval_create_type",
    "ApprovalRequestMessage": ".approval_request_message",
    "ApprovalRequestMessageMessageType": ".approval_request_message_message_type",
    "ApprovalRequestMessageToolCall": ".approval_request_message_tool_call",
    "ApprovalRequestMessageToolCalls": ".approval_request_message_tool_calls",
    "ApprovalResponseMessage": ".approval_response_message",
    "ApprovalResponseMessageApprovalsItem": ".approval_response_message_approvals_item",
    "ApprovalResponseMessageApprovalsItem_Approval": ".approval_response_message_approvals_item",
    "ApprovalResponseMessageApprovalsItem_Tool": ".approval_response_message_approvals_item",
    "ApprovalReturn": ".approval_return",
    "ApprovalReturnType": ".approval_return_type",
    "ArchivalMemorySearchResponse": ".archival_memory_search_response",
    "ArchivalMemorySearchResult": ".archival_memory_search_result",
    "Archive": ".archive",
    "AssistantMessage": ".assistant_message",
    "AssistantMessageContent": ".assistant_message_content",
    "AssistantMessageListResult": ".assistant_message_list_result",
    "AssistantMessageListResultContent": ".assistant_message_list_result_content",
    "Audio": ".audio",
    "AuthRequest": ".auth_request",
    "AuthResponse": ".auth_response",
    "AzureModelSettings": ".azure_model_settings",
    "AzureModelSettingsResponseFormat": ".azure_model_settings_response_format",
    "AzureModelSettingsResponseFormat_JsonObject": ".azure_model_settings_response_format",
    "AzureModelSettingsResponseFormat_JsonSchema": ".azure_model_settings_response_format",
    "AzureModelSettingsResponseFormat_Text": ".azure_model_settings_response_format",
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyErrorCode": ".bad_request_error_body_error_code",
    "Base64Image": ".base64image",
    "BaseToolRuleSchema": ".base_tool_rule_schema",
    "BatchJob": ".batch_job",
    "BedrockModelSettings": ".bedrock_model_settings",
    "BedrockModelSettingsResponseFormat": ".bedrock_model_settings_response_format",
    "BedrockModelSettingsResponseFormat_JsonObject": ".bedrock_model_settings_response_format",
    "BedrockModelSettingsResponseFormat_JsonSchema": ".bedrock_model_settings_response_format",
    "BedrockModelSettingsResponseFormat_Text": ".bedrock_model_settings_response_format",
    "Block": ".block",
    "BlockResponse": ".block_response",
    "BlockSchema": ".block_schema",
    "BlockUpdate": ".block_update",
    "BodyExportAgent": ".body_export_agent",
    "ChatCompletion": ".chat_completion",
    "ChatCompletionAssistantMessageParam": ".chat_completion_assistant_message_param",
    "ChatCompletionAssistantMessageParamContent": ".chat_completion_assistant_message_param_content",
    "ChatCompletionAssistantMessageParamContentOneItem": ".chat_completion_assistant_message_param_content_one_item",
    "ChatCompletionAssistantMessageParamContentOneItem_Refusal": ".chat_completion_assistant_message_param_content_one_item",
    "ChatCompletionAssistantMessageParamContentOneItem_Text": ".chat_completion_assistant_message_param_content_one_item",
    "ChatCompletionAssistantMessageParamToolCallsItem": ".chat_completion_assistant_message_param_tool_calls_item",
    "ChatCompletionAssistantMessageParamToolCallsItem_Custom": ".chat_completion_assistant_message_param_tool_calls_item",
    "ChatCompletionAssistantMessageParamToolCallsItem_Function": ".chat_completion_assistant_message_param_tool_calls_item",
    "ChatCompletionAudio": ".chat_completion_audio",
    "ChatCompletionContentPartImageParam": ".chat_completion_content_part_image_param",
    "ChatCompletionContentPartInputAudioParam": ".chat_completion_content_part_input_audio_param",
    "ChatCompletionContentPartRefusalParam": ".chat_completion_content_part_refusal_param",
    "ChatCompletionContentPartTextParam": ".chat_completion_content_part_text_param",
    "ChatCompletionContentPartTextParamType": ".chat_completion_content_part_text_param_type",
    "ChatCompletionDeveloperMessageParam": ".chat_completion_developer_message_param",
    "ChatCompletionDeveloperMessageParamContent": ".chat_completion_developer_message_param_content",
    "ChatCompletionFunctionMessageParam": ".chat_completion_function_message_param",
    "ChatCompletionMessage": ".chat_completion_message",
    "ChatCompletionMessageCustomToolCall": ".chat_completion_message_custom_tool_call",
    "ChatCompletionMessageCustomToolCallParam": ".chat_completion_message_custom_tool_call_param",
    "ChatCompletionMessageFunctionToolCallInput": ".chat_completion_message_function_tool_call_input",
    "ChatCompletionMessageFunctionToolCallInputType": ".chat_completion_message_function_tool_call_input_type",
    "ChatCompletionMessageFunctionToolCallOutput": ".chat_completion_message_function_tool_call_output",
    "ChatCompletionMessageFunctionToolCallOutputType": ".chat_completion_message_function_tool_call_output_type",
    "ChatCompletionMessageFunctionToolCallParam": ".chat_completion_message_function_tool_call_param",
    "ChatCompletionMessageRole": ".chat_completion_message_role",
    "ChatCompletionMessageToolCallsItem": ".chat_completion_message_tool_calls_item",
    "ChatCompletionMessageToolCallsItem_Custom": ".chat_completion_message_tool_calls_item",
    "ChatCompletionMessageToolCallsItem_Function": ".chat_completion_message_tool_calls_item",
    "ChatCompletionObject": ".chat_completion_object",
    "ChatCompletionServiceTier": ".chat_completion_service_tier",
    "ChatCompletionSystemMessageParam": ".chat_completion_system_message_param",
    "ChatCompletionSystemMessageParamContent": ".chat_completion_system_message_param_content",
    "ChatCompletionTokenLogprob": ".chat_completion_token_logprob",
    "ChatCompletionToolMessageParam": ".chat_completion_tool_message_param",
    "ChatCompletionToolMessageParamContent": ".chat_completion_tool_message_param_content",
    "ChatCompletionUserMessageParam": ".chat_completion_user_message_param",
    "ChatCompletionUserMessageParamContent": ".chat_completion_user_message_param_content",
    "ChatCompletionUserMessageParamContentOneItem": ".chat_completion_user_message_param_content_one_item",
    "ChatCompletionUserMessageParamContentOneItem_File": ".chat_completion_user_message_param_content_one_item",
    "ChatCompletionUserMessageParamContentOneItem_ImageUrl": ".chat_completion_user_message_param_content_one_item",
    "ChatCompletionUserMessageParamContentOneItem_InputAudio": ".chat_completion_user_message_param_content_one_item",
    "ChatCompletionUserMessageParamContentOneItem_Text": ".chat_completion_user_message_param_content_one_item",
    "ChatGptoAuthModelSettings": ".chat_gpto_auth_model_settings",
    "ChatGptoAuthReasoning": ".chat_gpto_auth_reasoning",
    "ChatGptoAuthReasoningReasoningEffort": ".chat_gpto_auth_reasoning_reasoning_effort",
    "ChildToolRule": ".child_tool_rule",
    "ChildToolRuleSchema": ".child_tool_rule_schema",
    "Choice": ".choice",
    "ChoiceFinishReason": ".choice_finish_reason",
    "ChoiceLogprobs": ".choice_logprobs",
    "ClientToolSchema": ".client_tool_schema",
    "CodeInput": ".code_input",
    "CompactionRequest": ".compaction_request",
    "CompactionResponse": ".compaction_response",
    "CompactionSettingsInput": ".compaction_settings_input",
    "CompactionSettingsInputMode": ".compaction_settings_input_mode",
    "CompactionSettingsInputModelSettings": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_Anthropic": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_Azure": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_Bedrock": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_ChatgptOauth": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_Deepseek": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_GoogleAi": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_GoogleVertex": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_Groq": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_Openai": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_Together": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_Xai": ".compaction_settings_input_model_settings",
    "CompactionSettingsInputModelSettings_Zai": ".compaction_settings_input_model_settings",
    "CompactionSettingsOutput": ".compaction_settings_output",
    "CompactionSettingsOutputMode": ".compaction_settings_output_mode",
    "CompactionSettingsOutputModelSettings": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_Anthropic": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_Azure": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_Bedrock": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_ChatgptOauth": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_Deepseek": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_GoogleAi": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_GoogleVertex": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_Groq": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_Openai": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_Together": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_Xai": ".compaction_settings_output_model_settings",
    "CompactionSettingsOutputModelSettings_Zai": ".compaction_settings_output_model_settings",
    "ComparisonOperator": ".comparison_operator",
    "CompletionTokensDetails": ".completion_tokens_details",
    "CompletionUsage": ".completion_usage",
    "ConditionalToolRule": ".conditional_tool_rule",
    "ConditionalToolRuleSchema": ".conditional_tool_rule_schema",
    "ConflictErrorBody": ".conflict_error_body",
    "ContextWindowOverview": ".context_window_overview",
    "ContinueToolRule": ".continue_tool_rule",
    "Conversation": ".conversation",
    "CoreMemoryBlockSchema": ".core_memory_block_schema",
    "CreateBlock": ".create_block",
    "CreateSsemcpServer": ".create_ssemcp_server",
    "CreateStdioMcpServer": ".create_stdio_mcp_server",
    "CreateStreamableHttpmcpServer": ".create_streamable_httpmcp_server",
    "CustomInput": ".custom_input",
    "CustomOutput": ".custom_output",
    "DeepseekModelSettings": ".deepseek_model_settings",
    "DeepseekModelSettingsResponseFormat": ".deepseek_model_settings_response_format",
    "DeepseekModelSettingsResponseFormat_JsonObject": ".deepseek_model_settings_response_format",
    "DeepseekModelSettingsResponseFormat_JsonSchema": ".deepseek_model_settings_response_format",
    "DeepseekModelSettingsResponseFormat_Text": ".deepseek_model_settings_response_format",
    "DeleteDeploymentResponse": ".delete_deployment_response",
    "DeploymentEntity": ".deployment_entity",
    "DuplicateFileHandling": ".duplicate_file_handling",
    "DynamicManager": ".dynamic_manager",
    "DynamicManagerUpdate": ".dynamic_manager_update",
    "E2BSandboxConfig": ".e2b_sandbox_config",
    "EmbeddingConfig": ".embedding_config",
    "EmbeddingConfigEmbeddingEndpointType": ".embedding_config_embedding_endpoint_type",
    "EmbeddingModel": ".embedding_model",
    "EmbeddingModelEmbeddingEndpointType": ".embedding_model_embedding_endpoint_type",
    "EmbeddingModelModelType": ".embedding_model_model_type",
    "EventMessage": ".event_message",
    "EventMessageEventType": ".event_message_event_type",
    "FeedbackType": ".feedback_type",
    "FeedsListFeedsRequestOffset": ".feeds_list_feeds_request_offset",
    "FeedsListSubscriptionsRequestOffset": ".feeds_list_subscriptions_request_offset",
    "File": ".file",
    "FileAgentSchema": ".file_agent_schema",
    "FileBlock": ".file_block",
    "FileFile": ".file_file",
    "FileMetadata": ".file_metadata",
    "FileProcessingStatus": ".file_processing_status",
    "FileSchema": ".file_schema",
    "FileStats": ".file_stats",
    "Folder": ".folder",
    "FunctionCallInput": ".function_call_input",
    "FunctionCallOutput": ".function_call_output",
    "FunctionDefinition": ".function_definition",
    "FunctionOutput": ".function_output",
    "FunctionTool": ".function_tool",
    "FunctionToolType": ".function_tool_type",
    "GeminiThinkingConfig": ".gemini_thinking_config",
    "GenerateToolInput": ".generate_tool_input",
    "GenerateToolOutput": ".generate_tool_output",
    "GoogleAiModelSettings": ".google_ai_model_settings",
    "GoogleAiModelSettingsResponseSchema": ".google_ai_model_settings_response_schema",
    "GoogleAiModelSettingsResponseSchema_JsonObject": ".google_ai_model_settings_response_schema",
    "GoogleAiModelSettingsResponseSchema_JsonSchema": ".google_ai_model_settings_response_schema",
    "GoogleAiModelSettingsResponseSchema_Text": ".google_ai_model_settings_response_schema",
    "GoogleVertexModelSettings": ".google_vertex_model_settings",
    "GoogleVertexModelSettingsResponseSchema": ".google_vertex_model_settings_response_schema",
    "GoogleVertexModelSettingsResponseSchema_JsonObject": ".google_vertex_model_settings_response_schema",
    "GoogleVertexModelSettingsResponseSchema_JsonSchema": ".google_vertex_model_settings_response_schema",
    "GoogleVertexModelSettingsResponseSchema_Text": ".google_vertex_model_settings_response_schema",
    "GroqModelSettings": ".groq_model_settings",
    "GroqModelSettingsResponseFormat": ".groq_model_settings_response_format",
    "GroqModelSettingsResponseFormat_JsonObject": ".groq_model_settings_response_format",
    "GroqModelSettingsResponseFormat_JsonSchema": ".groq_model_settings_response_format",
    "GroqModelSettingsResponseFormat_Text": ".groq_model_settings_response_format",
    "Group": ".group",
    "GroupSchema": ".group_schema",
    "GroupSchemaManagerConfig": ".group_schema_manager_config",
    "GroupSchemaManagerConfig_Dynamic": ".group_schema_manager_config",
    "GroupSchemaManagerConfig_RoundRobin": ".group_schema_manager_config",
    "GroupSchemaManagerConfig_Sleeptime": ".group_schema_manager_config",
    "GroupSchemaManagerConfig_Supervisor": ".group_schema_manager_config",
    "GroupSchemaManagerConfig_VoiceSleeptime": ".group_schema_manager_config",
    "Health": ".health",
    "HiddenReasoningMessage": ".hidden_reasoning_message",
    "HiddenReasoningMessageState": ".hidden_reasoning_message_state",
    "HttpValidationError": ".http_validation_error",
    "Identity": ".identity",
    "IdentityProperty": ".identity_property",
    "IdentityPropertyType": ".identity_property_type",
    "IdentityPropertyValue": ".identity_property_value",
    "IdentityType": ".identity_type",
    "ImageContent": ".image_content",
    "ImageContentSource": ".image_content_source",
    "ImageContentSource_Base64": ".image_content_source",
    "ImageContentSource_Letta": ".image_content_source",
    "ImageContentSource_Url": ".image_content_source",
    "ImageUrl": ".image_url",
    "ImageUrlDetail": ".image_url_detail",
    "ImportedAgentsResponse": ".imported_agents_response",
    "InitToolRule": ".init_tool_rule",
    "InputAudio": ".input_audio",
    "InputAudioFormat": ".input_audio_format",
    "InternalServerErrorBody": ".internal_server_error_body",
    "InternalTemplateBlockCreate": ".internal_template_block_create",
    "Job": ".job",
    "JobStatus": ".job_status",
    "JobType": ".job_type",
    "JsonObjectResponseFormat": ".json_object_response_format",
    "JsonSchemaResponseFormat": ".json_schema_response_format",
    "LettaAssistantMessageContentUnion": ".letta_assistant_message_content_union",
    "LettaAssistantMessageContentUnion_Text": ".letta_assistant_message_content_union",
    "LettaBatchMessages": ".letta_batch_messages",
    "LettaBatchRequest": ".letta_batch_request",
    "LettaBatchRequestInput": ".letta_batch_request_input",
    "LettaBatchRequestInputOneItem": ".letta_batch_request_input_one_item",
    "LettaBatchRequestInputOneItem_Image": ".letta_batch_request_input_one_item",
    "LettaBatchRequestInputOneItem_OmittedReasoning": ".letta_batch_request_input_one_item",
    "LettaBatchRequestInputOneItem_Reasoning": ".letta_batch_request_input_one_item",
    "LettaBatchRequestInputOneItem_RedactedReasoning": ".letta_batch_request_input_one_item",
    "LettaBatchRequestInputOneItem_SummarizedReasoning": ".letta_batch_request_input_one_item",
    "LettaBatchRequestInputOneItem_Text": ".letta_batch_request_input_one_item",
    "LettaBatchRequestInputOneItem_ToolCall": ".letta_batch_request_input_one_item",
    "LettaBatchRequestInputOneItem_ToolReturn": ".letta_batch_request_input_one_item",
    "LettaBatchRequestMessagesItem": ".letta_batch_request_messages_item",
    "LettaErrorMessage": ".letta_error_message",
    "LettaImage": ".letta_image",
    "LettaMessageContentUnion": ".letta_message_content_union",
    "LettaMessageContentUnion_Image": ".letta_message_content_union",
    "LettaMessageContentUnion_OmittedReasoning": ".letta_message_content_union",
    "LettaMessageContentUnion_Reasoning": ".letta_message_content_union",
    "LettaMessageContentUnion_RedactedReasoning": ".letta_message_content_union",
    "LettaMessageContentUnion_Text": ".letta_message_content_union",
    "LettaMessageContentUnion_ToolCall": ".letta_message_content_union",
    "LettaMessageContentUnion_ToolReturn": ".letta_message_content_union",
    "LettaMessageUnion": ".letta_message_union",
    "LettaMessageUnion_ApprovalRequestMessage": ".letta_message_union",
    "LettaMessageUnion_ApprovalResponseMessage": ".letta_message_union",
    "LettaMessageUnion_AssistantMessage": ".letta_message_union",
    "LettaMessageUnion_Event": ".letta_message_union",
    "LettaMessageUnion_HiddenReasoningMessage": ".letta_message_union",
    "LettaMessageUnion_ReasoningMessage": ".letta_message_union",
    "LettaMessageUnion_Summary": ".letta_message_union",
    "LettaMessageUnion_SystemMessage": ".letta_message_union",
    "LettaMessageUnion_ToolCallMessage": ".letta_message_union",
    "LettaMessageUnion_ToolReturnMessage": ".letta_message_union",
    "LettaMessageUnion_UserMessage": ".letta_message_union",
    "LettaPing": ".letta_ping",
    "LettaRequest": ".letta_request",
    "LettaRequestConfig": ".letta_request_config",
    "LettaRequestInput": ".letta_request_input",
    "LettaRequestInputOneItem": ".letta_request_input_one_item",
    "LettaRequestInputOneItem_Image": ".letta_request_input_one_item",
    "LettaRequestInputOneItem_OmittedReasoning": ".letta_request_input_one_item",
    "LettaRequestInputOneItem_Reasoning": ".letta_request_input_one_item",
    "LettaRequestInputOneItem_RedactedReasoning": ".letta_request_input_one_item",
    "LettaRequestInputOneItem_SummarizedReasoning": ".letta_request_input_one_item",
    "LettaRequestInputOneItem_Text": ".letta_request_input_one_item",
    "LettaRequestInputOneItem_ToolCall": ".letta_request_input_one_item",
    "LettaRequestInputOneItem_ToolReturn": ".letta_request_input_one_item",
    "LettaRequestMessagesItem": ".letta_request_messages_item",
    "LettaResponse": ".letta_response",
    "LettaSchemasAgentFileAgentSchema": ".letta_schemas_agent_file_agent_schema",
    "LettaSchemasAgentFileAgentSchemaModelSettings": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Anthropic": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Azure": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Bedrock": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_ChatgptOauth": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Deepseek": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_GoogleAi": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_GoogleVertex": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Groq": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Openai": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Together": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Xai": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Zai": ".letta_schemas_agent_file_agent_schema_model_settings",
    "LettaSchemasAgentFileAgentSchemaResponseFormat": ".letta_schemas_agent_file_agent_schema_response_format",
    "LettaSchemasAgentFileAgentSchemaResponseFormat_JsonObject": ".letta_schemas_agent_file_agent_schema_response_format",
    "LettaSchemasAgentFileAgentSchemaResponseFormat_JsonSchema": ".letta_schemas_agent_file_agent_schema_response_format",
    "LettaSchemasAgentFileAgentSchemaResponseFormat_Text": ".letta_schemas_agent_file_agent_schema_response_format",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_Conditional": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_ConstrainChildTools": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_ContinueLoop": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_ExitLoop": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_MaxCountPerStep": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_ParentLastTool": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_RequiredBeforeExit": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_RequiresApproval": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_RunFirst": ".letta_schemas_agent_file_agent_schema_tool_rules_item",
    "LettaSchemasAgentFileMessageSchema": ".letta_schemas_agent_file_message_schema",
    "LettaSchemasAgentFileMessageSchemaApprovalsItem": ".letta_schemas_agent_file_message_schema_approvals_item",
    "LettaSchemasAgentFileMessageSchemaContent": ".letta_schemas_agent_file_message_schema_content",
    "LettaSchemasAgentFileMessageSchemaType": ".letta_schemas_agent_file_message_schema_type",
    "LettaSchemasAgentFileToolSchema": ".letta_schemas_agent_file_tool_schema",
    "LettaSchemasLettaMessageToolReturn": ".letta_schemas_letta_message_tool_return",
    "LettaSchemasLettaMessageToolReturnStatus": ".letta_schemas_letta_message_tool_return_status",
    "LettaSchemasLettaMessageToolReturnToolReturn": ".letta_schemas_letta_message_tool_return_tool_return",
    "LettaSchemasLettaMessageToolReturnType": ".letta_schemas_letta_message_tool_return_type",
    "LettaSchemasMcpServerToolExecuteRequest": ".letta_schemas_mcp_server_tool_execute_request",
    "LettaSchemasMcpServerUpdateSsemcpServer": ".letta_schemas_mcp_server_update_ssemcp_server",
    "LettaSchemasMcpServerUpdateStdioMcpServer": ".letta_schemas_mcp_server_update_stdio_mcp_server",
    "LettaSchemasMcpServerUpdateStreamableHttpmcpServer": ".letta_schemas_mcp_server_update_streamable_httpmcp_server",
    "LettaSchemasMcpUpdateSsemcpServer": ".letta_schemas_mcp_update_ssemcp_server",
    "LettaSchemasMcpUpdateStdioMcpServer": ".letta_schemas_mcp_update_stdio_mcp_server",
    "LettaSchemasMcpUpdateStreamableHttpmcpServer": ".letta_schemas_mcp_update_streamable_httpmcp_server",
    "LettaSchemasMessageToolReturnInput": ".letta_schemas_message_tool_return_input",
    "LettaSchemasMessageToolReturnInputFuncResponse": ".letta_schemas_message_tool_return_input_func_response",
    "LettaSchemasMessageToolReturnInputFuncResponseOneItem": ".letta_schemas_message_tool_return_input_func_response_one_item",
    "LettaSchemasMessageToolReturnInputFuncResponseOneItem_Image": ".letta_schemas_message_tool_return_input_func_response_one_item",
    "LettaSchemasMessageToolReturnInputFuncResponseOneItem_Text": ".letta_schemas_message_tool_return_input_func_response_one_item",
    "LettaSchemasMessageToolReturnInputStatus": ".letta_schemas_message_tool_return_input_status",
    "LettaSchemasMessageToolReturnOutput": ".letta_schemas_message_tool_return_output",
    "LettaSchemasMessageToolReturnOutputFuncResponse": ".letta_schemas_message_tool_return_output_func_response",
    "LettaSchemasMessageToolReturnOutputFuncResponseOneItem": ".letta_schemas_message_tool_return_output_func_response_one_item",
    "LettaSchemasMessageToolReturnOutputFuncResponseOneItem_Image": ".letta_schemas_message_tool_return_output_func_response_one_item",
    "LettaSchemasMessageToolReturnOutputFuncResponseOneItem_Text": ".letta_schemas_message_tool_return_output_func_response_one_item",
    "LettaSchemasMessageToolReturnOutputStatus": ".letta_schemas_message_tool_return_output_status",
    "LettaSerializeSchemasPydanticAgentSchemaAgentSchema": ".letta_serialize_schemas_pydantic_agent_schema_agent_schema",
    "LettaSerializeSchemasPydanticAgentSchemaAgentSchemaToolRulesItem": ".letta_serialize_schemas_pydantic_agent_schema_agent_schema_tool_rules_item",
    "LettaSerializeSchemasPydanticAgentSchemaMessageSchema": ".letta_serialize_schemas_pydantic_agent_schema_message_schema",
    "LettaSerializeSchemasPydanticAgentSchemaToolSchema": ".letta_serialize_schemas_pydantic_agent_schema_tool_schema",
    "LettaStopReason": ".letta_stop_reason",
    "LettaStopReasonMessageType": ".letta_stop_reason_message_type",
    "LettaStreamingRequest": ".letta_streaming_request",
    "LettaStreamingRequestInput": ".letta_streaming_request_input",
    "LettaStreamingRequestInputOneItem": ".letta_streaming_request_input_one_item",
    "LettaStreamingRequestInputOneItem_Image": ".letta_streaming_request_input_one_item",
    "LettaStreamingRequestInputOneItem_OmittedReasoning": ".letta_streaming_request_input_one_item",
    "LettaStreamingRequestInputOneItem_Reasoning": ".letta_streaming_request_input_one_item",
    "LettaStreamingRequestInputOneItem_RedactedReasoning": ".letta_streaming_request_input_one_item",
    "LettaStreamingRequestInputOneItem_SummarizedReasoning": ".letta_streaming_request_input_one_item",
    "LettaStreamingRequestInputOneItem_Text": ".letta_streaming_request_input_one_item",
    "LettaStreamingRequestInputOneItem_ToolCall": ".letta_streaming_request_input_one_item",
    "LettaStreamingRequestInputOneItem_ToolReturn": ".letta_streaming_request_input_one_item",
    "LettaStreamingRequestMessagesItem": ".letta_streaming_request_messages_item",
    "LettaStreamingResponse": ".letta_streaming_response",
    "LettaStreamingResponse_ApprovalRequestMessage": ".letta_streaming_response",
    "LettaStreamingResponse_ApprovalResponseMessage": ".letta_streaming_response",
    "LettaStreamingResponse_AssistantMessage": ".letta_streaming_response",
    "LettaStreamingResponse_ErrorMessage": ".letta_streaming_response",
    "LettaStreamingResponse_HiddenReasoningMessage": ".letta_streaming_response",
    "LettaStreamingResponse_Ping": ".letta_streaming_response",
    "LettaStreamingResponse_ReasoningMessage": ".letta_streaming_response",
    "LettaStreamingResponse_StopReason": ".letta_streaming_response",
    "LettaStreamingResponse_SystemMessage": ".letta_streaming_response",
    "LettaStreamingResponse_ToolCallMessage": ".letta_streaming_response",
    "LettaStreamingResponse_ToolReturnMessage": ".letta_streaming_response",
    "LettaStreamingResponse_UsageStatistics": ".letta_streaming_response",
    "LettaStreamingResponse_UserMessage": ".letta_streaming_response",
    "LettaToolReturnContentUnion": ".letta_tool_return_content_union",
    "LettaToolReturnContentUnion_Image": ".letta_tool_return_content_union",
    "LettaToolReturnContentUnion_Text": ".letta_tool_return_content_union",
    "LettaUsageStatistics": ".letta_usage_statistics",
    "LettaUsageStatisticsMessageType": ".letta_usage_statistics_message_type",
    "LettaUserMessageContentUnion": ".letta_user_message_content_union",
    "LettaUserMessageContentUnion_Image": ".letta_user_message_content_union",
    "LettaUserMessageContentUnion_Text": ".letta_user_message_content_union",
    "ListDeploymentEntitiesResponse": ".list_deployment_entities_response",
    "LlmConfig": ".llm_config",
    "LlmConfigCompatibilityType": ".llm_config_compatibility_type",
    "LlmConfigEffort": ".llm_config_effort",
    "LlmConfigModelEndpointType": ".llm_config_model_endpoint_type",
    "LlmConfigReasoningEffort": ".llm_config_reasoning_effort",
    "LlmConfigResponseFormat": ".llm_config_response_format",
    "LlmConfigResponseFormat_JsonObject": ".llm_config_response_format",
    "LlmConfigResponseFormat_JsonSchema": ".llm_config_response_format",
    "LlmConfigResponseFormat_Text": ".llm_config_response_format",
    "LlmConfigVerbosity": ".llm_config_verbosity",
    "LocalSandboxConfig": ".local_sandbox_config",
    "ManagerType": ".manager_type",
    "MaxCountPerStepToolRule": ".max_count_per_step_tool_rule",
    "MaxCountPerStepToolRuleSchema": ".max_count_per_step_tool_rule_schema",
    "McpServerSchema": ".mcp_server_schema",
    "McpServerType": ".mcp_server_type",
    "McpTool": ".mcp_tool",
    "McpToolHealth": ".mcp_tool_health",
    "Memory": ".memory",
    "MemoryAgentType": ".memory_agent_type",
    "Message": ".message",
    "MessageApprovalsItem": ".message_approvals_item",
    "MessageContentItem": ".message_content_item",
    "MessageContentItem_Image": ".message_content_item",
    "MessageContentItem_OmittedReasoning": ".message_content_item",
    "MessageContentItem_Reasoning": ".message_content_item",
    "MessageContentItem_RedactedReasoning": ".message_content_item",
    "MessageContentItem_SummarizedReasoning": ".message_content_item",
    "MessageContentItem_Text": ".message_content_item",
    "MessageContentItem_ToolCall": ".message_content_item",
    "MessageContentItem_ToolReturn": ".message_content_item",
    "MessageCreate": ".message_create",
    "MessageCreateContent": ".message_create_content",
    "MessageCreateRole": ".message_create_role",
    "MessageCreateType": ".message_create_type",
    "MessageRole": ".message_role",
    "MessageSearchResult": ".message_search_result",
    "MessageType": ".message_type",
    "ModalSandboxConfig": ".modal_sandbox_config",
    "ModalSandboxConfigLanguage": ".modal_sandbox_config_language",
    "Model": ".model",
    "ModelCompatibilityType": ".model_compatibility_type",
    "ModelEffort": ".model_effort",
    "ModelModelEndpointType": ".model_model_endpoint_type",
    "ModelModelType": ".model_model_type",
    "ModelReasoningEffort": ".model_reasoning_effort",
    "ModelResponseFormat": ".model_response_format",
    "ModelResponseFormat_JsonObject": ".model_response_format",
    "ModelResponseFormat_JsonSchema": ".model_response_format",
    "ModelResponseFormat_Text": ".model_response_format",
    "ModelVerbosity": ".model_verbosity",
    "ModifyApprovalRequest": ".modify_approval_request",
    "NotFoundErrorBody": ".not_found_error_body",
    "NotFoundErrorBodyErrorCode": ".not_found_error_body_error_code",
    "NotFoundErrorBodyMessage": ".not_found_error_body_message",
    "NpmRequirement": ".npm_requirement",
    "OmittedReasoningContent": ".omitted_reasoning_content",
    "OpenAiModelSettings": ".open_ai_model_settings",
    "OpenAiModelSettingsResponseFormat": ".open_ai_model_settings_response_format",
    "OpenAiModelSettingsResponseFormat_JsonObject": ".open_ai_model_settings_response_format",
    "OpenAiModelSettingsResponseFormat_JsonSchema": ".open_ai_model_settings_response_format",
    "OpenAiModelSettingsResponseFormat_Text": ".open_ai_model_settings_response_format",
    "OpenAiReasoning": ".open_ai_reasoning",
    "OpenAiReasoningReasoningEffort": ".open_ai_reasoning_reasoning_effort",
    "OpenaiTypesChatChatCompletionMessageFunctionToolCallFunction": ".openai_types_chat_chat_completion_message_function_tool_call_function",
    "OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction": ".openai_types_chat_chat_completion_message_function_tool_call_param_function",
    "Organization": ".organization",
    "OrganizationCreate": ".organization_create",
    "OrganizationSourcesStats": ".organization_sources_stats",
    "OrganizationUpdate": ".organization_update",
    "PaginatedAgentFiles": ".paginated_agent_files",
    "ParameterProperties": ".parameter_properties",
    "ParametersSchema": ".parameters_schema",
    "ParentToolRule": ".parent_tool_rule",
    "Passage": ".passage",
    "PassageSearchResult": ".passage_search_result",
    "PaymentRequiredErrorBody": ".payment_required_error_body",
    "PipRequirement": ".pip_requirement",
    "PipelinesListPipelinesRequestOffset": ".pipelines_list_pipelines_request_offset",
    "ProjectsListProjectsRequestOffset": ".projects_list_projects_request_offset",
    "PromptTokensDetails": ".prompt_tokens_details",
    "Provider": ".provider",
    "ProviderCategory": ".provider_category",
    "ProviderTrace": ".provider_trace",
    "ProviderType": ".provider_type",
    "ReasoningContent": ".reasoning_content",
    "ReasoningMessage": ".reasoning_message",
    "ReasoningMessageListResult": ".reasoning_message_list_result",
    "ReasoningMessageSource": ".reasoning_message_source",
    "RedactedReasoningContent": ".redacted_reasoning_content",
    "RequiredBeforeExitToolRule": ".required_before_exit_tool_rule",
    "RequiresApprovalToolRule": ".requires_approval_tool_rule",
    "RetrieveStreamRequest": ".retrieve_stream_request",
    "RoundRobinManager": ".round_robin_manager",
    "RoundRobinManagerUpdate": ".round_robin_manager_update",
    "Run": ".run",
    "RunMetrics": ".run_metrics",
    "RunStatus": ".run_status",
    "SandboxConfig": ".sandbox_config",
    "SandboxConfigCreate": ".sandbox_config_create",
    "SandboxConfigCreateConfig": ".sandbox_config_create_config",
    "SandboxConfigUpdate": ".sandbox_config_update",
    "SandboxConfigUpdateConfig": ".sandbox_config_update_config",
    "SandboxEnvironmentVariable": ".sandbox_environment_variable",
    "SandboxEnvironmentVariableCreate": ".sandbox_environment_variable_create",
    "SandboxEnvironmentVariableUpdate": ".sandbox_environment_variable_update",
    "SandboxType": ".sandbox_type",
    "SleeptimeManager": ".sleeptime_manager",
    "SleeptimeManagerUpdate": ".sleeptime_manager_update",
    "Source": ".source",
    "SourceCreate": ".source_create",
    "SourceSchema": ".source_schema",
    "SourceStats": ".source_stats",
    "SourceUpdate": ".source_update",
    "SseServerConfig": ".sse_server_config",
    "SsemcpServer": ".ssemcp_server",
    "StdioMcpServer": ".stdio_mcp_server",
    "StdioServerConfig": ".stdio_server_config",
    "Step": ".step",
    "StepFeedback": ".step_feedback",
    "StepMetrics": ".step_metrics",
    "StepStatus": ".step_status",
    "StopReasonType": ".stop_reason_type",
    "StreamableHttpServerConfig": ".streamable_http_server_config",
    "StreamableHttpmcpServer": ".streamable_httpmcp_server",
    "SummarizedReasoningContent": ".summarized_reasoning_content",
    "SummarizedReasoningContentPart": ".summarized_reasoning_content_part",
    "SummaryMessage": ".summary_message",
    "SupervisorManager": ".supervisor_manager",
    "SupervisorManagerUpdate": ".supervisor_manager_update",
    "SystemMessage": ".system_message",
    "SystemMessageListResult": ".system_message_list_result",
    "TagSchema": ".tag_schema",
    "TemplatesListTemplateVersionsRequestOffset": ".templates_list_template_versions_request_offset",
    "TemplatesListTemplatesRequestOffset": ".templates_list_templates_request_offset",
    "TerminalToolRule": ".terminal_tool_rule",
    "TextContent": ".text_content",
    "TextResponseFormat": ".text_response_format",
    "TogetherModelSettings": ".together_model_settings",
    "TogetherModelSettingsResponseFormat": ".together_model_settings_response_format",
    "TogetherModelSettingsResponseFormat_JsonObject": ".together_model_settings_response_format",
    "TogetherModelSettingsResponseFormat_JsonSchema": ".together_model_settings_response_format",
    "TogetherModelSettingsResponseFormat_Text": ".together_model_settings_response_format",
    "Tool": ".tool",
    "ToolAnnotations": ".tool_annotations",
    "ToolCall": ".tool_call",
    "ToolCallContent": ".tool_call_content",
    "ToolCallDelta": ".tool_call_delta",
    "ToolCallMessage": ".tool_call_message",
    "ToolCallMessageToolCall": ".tool_call_message_tool_call",
    "ToolCallMessageToolCalls": ".tool_call_message_tool_calls",
    "ToolCallNode": ".tool_call_node",
    "ToolCreate": ".tool_create",
    "ToolEnvVarSchema": ".tool_env_var_schema",
    "ToolExecutionResult": ".tool_execution_result",
    "ToolExecutionResultStatus": ".tool_execution_result_status",
    "ToolJsonSchema": ".tool_json_schema",
    "ToolReturnContent": ".tool_return_content",
    "ToolReturnMessage": ".tool_return_message",
    "ToolReturnMessageMessageType": ".tool_return_message_message_type",
    "ToolReturnMessageStatus": ".tool_return_message_status",
    "ToolSearchResult": ".tool_search_result",
    "ToolType": ".tool_type",
    "TopLogprob": ".top_logprob",
    "UpdateAssistantMessage": ".update_assistant_message",
    "UpdateAssistantMessageContent": ".update_assistant_message_content",
    "UpdateReasoningMessage": ".update_reasoning_message",
    "UpdateSystemMessage": ".update_system_message",
    "UpdateUserMessage": ".update_user_message",
    "UpdateUserMessageContent": ".update_user_message_content",
    "UrlImage": ".url_image",
    "UsageStatistics": ".usage_statistics",
    "UsageStatisticsCompletionTokenDetails": ".usage_statistics_completion_token_details",
    "UsageStatisticsPromptTokenDetails": ".usage_statistics_prompt_token_details",
    "User": ".user",
    "UserCreate": ".user_create",
    "UserMessage": ".user_message",
    "UserMessageContent": ".user_message_content",
    "UserMessageListResult": ".user_message_list_result",
    "UserMessageListResultContent": ".user_message_list_result_content",
    "UserUpdate": ".user_update",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VectorDbProvider": ".vector_db_provider",
    "VoiceSleeptimeManager": ".voice_sleeptime_manager",
    "VoiceSleeptimeManagerUpdate": ".voice_sleeptime_manager_update",
    "XaiModelSettings": ".xai_model_settings",
    "XaiModelSettingsResponseFormat": ".xai_model_settings_response_format",
    "XaiModelSettingsResponseFormat_JsonObject": ".xai_model_settings_response_format",
    "XaiModelSettingsResponseFormat_JsonSchema": ".xai_model_settings_response_format",
    "XaiModelSettingsResponseFormat_Text": ".xai_model_settings_response_format",
    "ZaiModelSettings": ".zai_model_settings",
    "ZaiModelSettingsResponseFormat": ".zai_model_settings_response_format",
    "ZaiModelSettingsResponseFormat_JsonObject": ".zai_model_settings_response_format",
    "ZaiModelSettingsResponseFormat_JsonSchema": ".zai_model_settings_response_format",
    "ZaiModelSettingsResponseFormat_Text": ".zai_model_settings_response_format",
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
    "AgentEnvironmentVariable",
    "AgentFileAttachment",
    "AgentFileSchema",
    "AgentState",
    "AgentStateModelSettings",
    "AgentStateModelSettings_Anthropic",
    "AgentStateModelSettings_Azure",
    "AgentStateModelSettings_Bedrock",
    "AgentStateModelSettings_ChatgptOauth",
    "AgentStateModelSettings_Deepseek",
    "AgentStateModelSettings_GoogleAi",
    "AgentStateModelSettings_GoogleVertex",
    "AgentStateModelSettings_Groq",
    "AgentStateModelSettings_Openai",
    "AgentStateModelSettings_Together",
    "AgentStateModelSettings_Xai",
    "AgentStateModelSettings_Zai",
    "AgentStateResponseFormat",
    "AgentStateResponseFormat_JsonObject",
    "AgentStateResponseFormat_JsonSchema",
    "AgentStateResponseFormat_Text",
    "AgentStateToolRulesItem",
    "AgentStateToolRulesItem_Conditional",
    "AgentStateToolRulesItem_ConstrainChildTools",
    "AgentStateToolRulesItem_ContinueLoop",
    "AgentStateToolRulesItem_ExitLoop",
    "AgentStateToolRulesItem_MaxCountPerStep",
    "AgentStateToolRulesItem_ParentLastTool",
    "AgentStateToolRulesItem_RequiredBeforeExit",
    "AgentStateToolRulesItem_RequiresApproval",
    "AgentStateToolRulesItem_RunFirst",
    "AgentType",
    "Annotation",
    "AnnotationType",
    "AnnotationUrlCitation",
    "AnthropicModelSettings",
    "AnthropicModelSettingsEffort",
    "AnthropicModelSettingsResponseFormat",
    "AnthropicModelSettingsResponseFormat_JsonObject",
    "AnthropicModelSettingsResponseFormat_JsonSchema",
    "AnthropicModelSettingsResponseFormat_Text",
    "AnthropicModelSettingsVerbosity",
    "AnthropicThinking",
    "AnthropicThinkingType",
    "ApprovalCreate",
    "ApprovalCreateApprovalsItem",
    "ApprovalCreateApprovalsItem_Approval",
    "ApprovalCreateApprovalsItem_Tool",
    "ApprovalCreateType",
    "ApprovalRequestMessage",
    "ApprovalRequestMessageMessageType",
    "ApprovalRequestMessageToolCall",
    "ApprovalRequestMessageToolCalls",
    "ApprovalResponseMessage",
    "ApprovalResponseMessageApprovalsItem",
    "ApprovalResponseMessageApprovalsItem_Approval",
    "ApprovalResponseMessageApprovalsItem_Tool",
    "ApprovalReturn",
    "ApprovalReturnType",
    "ArchivalMemorySearchResponse",
    "ArchivalMemorySearchResult",
    "Archive",
    "AssistantMessage",
    "AssistantMessageContent",
    "AssistantMessageListResult",
    "AssistantMessageListResultContent",
    "Audio",
    "AuthRequest",
    "AuthResponse",
    "AzureModelSettings",
    "AzureModelSettingsResponseFormat",
    "AzureModelSettingsResponseFormat_JsonObject",
    "AzureModelSettingsResponseFormat_JsonSchema",
    "AzureModelSettingsResponseFormat_Text",
    "BadRequestErrorBody",
    "BadRequestErrorBodyErrorCode",
    "Base64Image",
    "BaseToolRuleSchema",
    "BatchJob",
    "BedrockModelSettings",
    "BedrockModelSettingsResponseFormat",
    "BedrockModelSettingsResponseFormat_JsonObject",
    "BedrockModelSettingsResponseFormat_JsonSchema",
    "BedrockModelSettingsResponseFormat_Text",
    "Block",
    "BlockResponse",
    "BlockSchema",
    "BlockUpdate",
    "BodyExportAgent",
    "ChatCompletion",
    "ChatCompletionAssistantMessageParam",
    "ChatCompletionAssistantMessageParamContent",
    "ChatCompletionAssistantMessageParamContentOneItem",
    "ChatCompletionAssistantMessageParamContentOneItem_Refusal",
    "ChatCompletionAssistantMessageParamContentOneItem_Text",
    "ChatCompletionAssistantMessageParamToolCallsItem",
    "ChatCompletionAssistantMessageParamToolCallsItem_Custom",
    "ChatCompletionAssistantMessageParamToolCallsItem_Function",
    "ChatCompletionAudio",
    "ChatCompletionContentPartImageParam",
    "ChatCompletionContentPartInputAudioParam",
    "ChatCompletionContentPartRefusalParam",
    "ChatCompletionContentPartTextParam",
    "ChatCompletionContentPartTextParamType",
    "ChatCompletionDeveloperMessageParam",
    "ChatCompletionDeveloperMessageParamContent",
    "ChatCompletionFunctionMessageParam",
    "ChatCompletionMessage",
    "ChatCompletionMessageCustomToolCall",
    "ChatCompletionMessageCustomToolCallParam",
    "ChatCompletionMessageFunctionToolCallInput",
    "ChatCompletionMessageFunctionToolCallInputType",
    "ChatCompletionMessageFunctionToolCallOutput",
    "ChatCompletionMessageFunctionToolCallOutputType",
    "ChatCompletionMessageFunctionToolCallParam",
    "ChatCompletionMessageRole",
    "ChatCompletionMessageToolCallsItem",
    "ChatCompletionMessageToolCallsItem_Custom",
    "ChatCompletionMessageToolCallsItem_Function",
    "ChatCompletionObject",
    "ChatCompletionServiceTier",
    "ChatCompletionSystemMessageParam",
    "ChatCompletionSystemMessageParamContent",
    "ChatCompletionTokenLogprob",
    "ChatCompletionToolMessageParam",
    "ChatCompletionToolMessageParamContent",
    "ChatCompletionUserMessageParam",
    "ChatCompletionUserMessageParamContent",
    "ChatCompletionUserMessageParamContentOneItem",
    "ChatCompletionUserMessageParamContentOneItem_File",
    "ChatCompletionUserMessageParamContentOneItem_ImageUrl",
    "ChatCompletionUserMessageParamContentOneItem_InputAudio",
    "ChatCompletionUserMessageParamContentOneItem_Text",
    "ChatGptoAuthModelSettings",
    "ChatGptoAuthReasoning",
    "ChatGptoAuthReasoningReasoningEffort",
    "ChildToolRule",
    "ChildToolRuleSchema",
    "Choice",
    "ChoiceFinishReason",
    "ChoiceLogprobs",
    "ClientToolSchema",
    "CodeInput",
    "CompactionRequest",
    "CompactionResponse",
    "CompactionSettingsInput",
    "CompactionSettingsInputMode",
    "CompactionSettingsInputModelSettings",
    "CompactionSettingsInputModelSettings_Anthropic",
    "CompactionSettingsInputModelSettings_Azure",
    "CompactionSettingsInputModelSettings_Bedrock",
    "CompactionSettingsInputModelSettings_ChatgptOauth",
    "CompactionSettingsInputModelSettings_Deepseek",
    "CompactionSettingsInputModelSettings_GoogleAi",
    "CompactionSettingsInputModelSettings_GoogleVertex",
    "CompactionSettingsInputModelSettings_Groq",
    "CompactionSettingsInputModelSettings_Openai",
    "CompactionSettingsInputModelSettings_Together",
    "CompactionSettingsInputModelSettings_Xai",
    "CompactionSettingsInputModelSettings_Zai",
    "CompactionSettingsOutput",
    "CompactionSettingsOutputMode",
    "CompactionSettingsOutputModelSettings",
    "CompactionSettingsOutputModelSettings_Anthropic",
    "CompactionSettingsOutputModelSettings_Azure",
    "CompactionSettingsOutputModelSettings_Bedrock",
    "CompactionSettingsOutputModelSettings_ChatgptOauth",
    "CompactionSettingsOutputModelSettings_Deepseek",
    "CompactionSettingsOutputModelSettings_GoogleAi",
    "CompactionSettingsOutputModelSettings_GoogleVertex",
    "CompactionSettingsOutputModelSettings_Groq",
    "CompactionSettingsOutputModelSettings_Openai",
    "CompactionSettingsOutputModelSettings_Together",
    "CompactionSettingsOutputModelSettings_Xai",
    "CompactionSettingsOutputModelSettings_Zai",
    "ComparisonOperator",
    "CompletionTokensDetails",
    "CompletionUsage",
    "ConditionalToolRule",
    "ConditionalToolRuleSchema",
    "ConflictErrorBody",
    "ContextWindowOverview",
    "ContinueToolRule",
    "Conversation",
    "CoreMemoryBlockSchema",
    "CreateBlock",
    "CreateSsemcpServer",
    "CreateStdioMcpServer",
    "CreateStreamableHttpmcpServer",
    "CustomInput",
    "CustomOutput",
    "DeepseekModelSettings",
    "DeepseekModelSettingsResponseFormat",
    "DeepseekModelSettingsResponseFormat_JsonObject",
    "DeepseekModelSettingsResponseFormat_JsonSchema",
    "DeepseekModelSettingsResponseFormat_Text",
    "DeleteDeploymentResponse",
    "DeploymentEntity",
    "DuplicateFileHandling",
    "DynamicManager",
    "DynamicManagerUpdate",
    "E2BSandboxConfig",
    "EmbeddingConfig",
    "EmbeddingConfigEmbeddingEndpointType",
    "EmbeddingModel",
    "EmbeddingModelEmbeddingEndpointType",
    "EmbeddingModelModelType",
    "EventMessage",
    "EventMessageEventType",
    "FeedbackType",
    "FeedsListFeedsRequestOffset",
    "FeedsListSubscriptionsRequestOffset",
    "File",
    "FileAgentSchema",
    "FileBlock",
    "FileFile",
    "FileMetadata",
    "FileProcessingStatus",
    "FileSchema",
    "FileStats",
    "Folder",
    "FunctionCallInput",
    "FunctionCallOutput",
    "FunctionDefinition",
    "FunctionOutput",
    "FunctionTool",
    "FunctionToolType",
    "GeminiThinkingConfig",
    "GenerateToolInput",
    "GenerateToolOutput",
    "GoogleAiModelSettings",
    "GoogleAiModelSettingsResponseSchema",
    "GoogleAiModelSettingsResponseSchema_JsonObject",
    "GoogleAiModelSettingsResponseSchema_JsonSchema",
    "GoogleAiModelSettingsResponseSchema_Text",
    "GoogleVertexModelSettings",
    "GoogleVertexModelSettingsResponseSchema",
    "GoogleVertexModelSettingsResponseSchema_JsonObject",
    "GoogleVertexModelSettingsResponseSchema_JsonSchema",
    "GoogleVertexModelSettingsResponseSchema_Text",
    "GroqModelSettings",
    "GroqModelSettingsResponseFormat",
    "GroqModelSettingsResponseFormat_JsonObject",
    "GroqModelSettingsResponseFormat_JsonSchema",
    "GroqModelSettingsResponseFormat_Text",
    "Group",
    "GroupSchema",
    "GroupSchemaManagerConfig",
    "GroupSchemaManagerConfig_Dynamic",
    "GroupSchemaManagerConfig_RoundRobin",
    "GroupSchemaManagerConfig_Sleeptime",
    "GroupSchemaManagerConfig_Supervisor",
    "GroupSchemaManagerConfig_VoiceSleeptime",
    "Health",
    "HiddenReasoningMessage",
    "HiddenReasoningMessageState",
    "HttpValidationError",
    "Identity",
    "IdentityProperty",
    "IdentityPropertyType",
    "IdentityPropertyValue",
    "IdentityType",
    "ImageContent",
    "ImageContentSource",
    "ImageContentSource_Base64",
    "ImageContentSource_Letta",
    "ImageContentSource_Url",
    "ImageUrl",
    "ImageUrlDetail",
    "ImportedAgentsResponse",
    "InitToolRule",
    "InputAudio",
    "InputAudioFormat",
    "InternalServerErrorBody",
    "InternalTemplateBlockCreate",
    "Job",
    "JobStatus",
    "JobType",
    "JsonObjectResponseFormat",
    "JsonSchemaResponseFormat",
    "LettaAssistantMessageContentUnion",
    "LettaAssistantMessageContentUnion_Text",
    "LettaBatchMessages",
    "LettaBatchRequest",
    "LettaBatchRequestInput",
    "LettaBatchRequestInputOneItem",
    "LettaBatchRequestInputOneItem_Image",
    "LettaBatchRequestInputOneItem_OmittedReasoning",
    "LettaBatchRequestInputOneItem_Reasoning",
    "LettaBatchRequestInputOneItem_RedactedReasoning",
    "LettaBatchRequestInputOneItem_SummarizedReasoning",
    "LettaBatchRequestInputOneItem_Text",
    "LettaBatchRequestInputOneItem_ToolCall",
    "LettaBatchRequestInputOneItem_ToolReturn",
    "LettaBatchRequestMessagesItem",
    "LettaErrorMessage",
    "LettaImage",
    "LettaMessageContentUnion",
    "LettaMessageContentUnion_Image",
    "LettaMessageContentUnion_OmittedReasoning",
    "LettaMessageContentUnion_Reasoning",
    "LettaMessageContentUnion_RedactedReasoning",
    "LettaMessageContentUnion_Text",
    "LettaMessageContentUnion_ToolCall",
    "LettaMessageContentUnion_ToolReturn",
    "LettaMessageUnion",
    "LettaMessageUnion_ApprovalRequestMessage",
    "LettaMessageUnion_ApprovalResponseMessage",
    "LettaMessageUnion_AssistantMessage",
    "LettaMessageUnion_Event",
    "LettaMessageUnion_HiddenReasoningMessage",
    "LettaMessageUnion_ReasoningMessage",
    "LettaMessageUnion_Summary",
    "LettaMessageUnion_SystemMessage",
    "LettaMessageUnion_ToolCallMessage",
    "LettaMessageUnion_ToolReturnMessage",
    "LettaMessageUnion_UserMessage",
    "LettaPing",
    "LettaRequest",
    "LettaRequestConfig",
    "LettaRequestInput",
    "LettaRequestInputOneItem",
    "LettaRequestInputOneItem_Image",
    "LettaRequestInputOneItem_OmittedReasoning",
    "LettaRequestInputOneItem_Reasoning",
    "LettaRequestInputOneItem_RedactedReasoning",
    "LettaRequestInputOneItem_SummarizedReasoning",
    "LettaRequestInputOneItem_Text",
    "LettaRequestInputOneItem_ToolCall",
    "LettaRequestInputOneItem_ToolReturn",
    "LettaRequestMessagesItem",
    "LettaResponse",
    "LettaSchemasAgentFileAgentSchema",
    "LettaSchemasAgentFileAgentSchemaModelSettings",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Anthropic",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Azure",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Bedrock",
    "LettaSchemasAgentFileAgentSchemaModelSettings_ChatgptOauth",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Deepseek",
    "LettaSchemasAgentFileAgentSchemaModelSettings_GoogleAi",
    "LettaSchemasAgentFileAgentSchemaModelSettings_GoogleVertex",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Groq",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Openai",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Together",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Xai",
    "LettaSchemasAgentFileAgentSchemaModelSettings_Zai",
    "LettaSchemasAgentFileAgentSchemaResponseFormat",
    "LettaSchemasAgentFileAgentSchemaResponseFormat_JsonObject",
    "LettaSchemasAgentFileAgentSchemaResponseFormat_JsonSchema",
    "LettaSchemasAgentFileAgentSchemaResponseFormat_Text",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_Conditional",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_ConstrainChildTools",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_ContinueLoop",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_ExitLoop",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_MaxCountPerStep",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_ParentLastTool",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_RequiredBeforeExit",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_RequiresApproval",
    "LettaSchemasAgentFileAgentSchemaToolRulesItem_RunFirst",
    "LettaSchemasAgentFileMessageSchema",
    "LettaSchemasAgentFileMessageSchemaApprovalsItem",
    "LettaSchemasAgentFileMessageSchemaContent",
    "LettaSchemasAgentFileMessageSchemaType",
    "LettaSchemasAgentFileToolSchema",
    "LettaSchemasLettaMessageToolReturn",
    "LettaSchemasLettaMessageToolReturnStatus",
    "LettaSchemasLettaMessageToolReturnToolReturn",
    "LettaSchemasLettaMessageToolReturnType",
    "LettaSchemasMcpServerToolExecuteRequest",
    "LettaSchemasMcpServerUpdateSsemcpServer",
    "LettaSchemasMcpServerUpdateStdioMcpServer",
    "LettaSchemasMcpServerUpdateStreamableHttpmcpServer",
    "LettaSchemasMcpUpdateSsemcpServer",
    "LettaSchemasMcpUpdateStdioMcpServer",
    "LettaSchemasMcpUpdateStreamableHttpmcpServer",
    "LettaSchemasMessageToolReturnInput",
    "LettaSchemasMessageToolReturnInputFuncResponse",
    "LettaSchemasMessageToolReturnInputFuncResponseOneItem",
    "LettaSchemasMessageToolReturnInputFuncResponseOneItem_Image",
    "LettaSchemasMessageToolReturnInputFuncResponseOneItem_Text",
    "LettaSchemasMessageToolReturnInputStatus",
    "LettaSchemasMessageToolReturnOutput",
    "LettaSchemasMessageToolReturnOutputFuncResponse",
    "LettaSchemasMessageToolReturnOutputFuncResponseOneItem",
    "LettaSchemasMessageToolReturnOutputFuncResponseOneItem_Image",
    "LettaSchemasMessageToolReturnOutputFuncResponseOneItem_Text",
    "LettaSchemasMessageToolReturnOutputStatus",
    "LettaSerializeSchemasPydanticAgentSchemaAgentSchema",
    "LettaSerializeSchemasPydanticAgentSchemaAgentSchemaToolRulesItem",
    "LettaSerializeSchemasPydanticAgentSchemaMessageSchema",
    "LettaSerializeSchemasPydanticAgentSchemaToolSchema",
    "LettaStopReason",
    "LettaStopReasonMessageType",
    "LettaStreamingRequest",
    "LettaStreamingRequestInput",
    "LettaStreamingRequestInputOneItem",
    "LettaStreamingRequestInputOneItem_Image",
    "LettaStreamingRequestInputOneItem_OmittedReasoning",
    "LettaStreamingRequestInputOneItem_Reasoning",
    "LettaStreamingRequestInputOneItem_RedactedReasoning",
    "LettaStreamingRequestInputOneItem_SummarizedReasoning",
    "LettaStreamingRequestInputOneItem_Text",
    "LettaStreamingRequestInputOneItem_ToolCall",
    "LettaStreamingRequestInputOneItem_ToolReturn",
    "LettaStreamingRequestMessagesItem",
    "LettaStreamingResponse",
    "LettaStreamingResponse_ApprovalRequestMessage",
    "LettaStreamingResponse_ApprovalResponseMessage",
    "LettaStreamingResponse_AssistantMessage",
    "LettaStreamingResponse_ErrorMessage",
    "LettaStreamingResponse_HiddenReasoningMessage",
    "LettaStreamingResponse_Ping",
    "LettaStreamingResponse_ReasoningMessage",
    "LettaStreamingResponse_StopReason",
    "LettaStreamingResponse_SystemMessage",
    "LettaStreamingResponse_ToolCallMessage",
    "LettaStreamingResponse_ToolReturnMessage",
    "LettaStreamingResponse_UsageStatistics",
    "LettaStreamingResponse_UserMessage",
    "LettaToolReturnContentUnion",
    "LettaToolReturnContentUnion_Image",
    "LettaToolReturnContentUnion_Text",
    "LettaUsageStatistics",
    "LettaUsageStatisticsMessageType",
    "LettaUserMessageContentUnion",
    "LettaUserMessageContentUnion_Image",
    "LettaUserMessageContentUnion_Text",
    "ListDeploymentEntitiesResponse",
    "LlmConfig",
    "LlmConfigCompatibilityType",
    "LlmConfigEffort",
    "LlmConfigModelEndpointType",
    "LlmConfigReasoningEffort",
    "LlmConfigResponseFormat",
    "LlmConfigResponseFormat_JsonObject",
    "LlmConfigResponseFormat_JsonSchema",
    "LlmConfigResponseFormat_Text",
    "LlmConfigVerbosity",
    "LocalSandboxConfig",
    "ManagerType",
    "MaxCountPerStepToolRule",
    "MaxCountPerStepToolRuleSchema",
    "McpServerSchema",
    "McpServerType",
    "McpTool",
    "McpToolHealth",
    "Memory",
    "MemoryAgentType",
    "Message",
    "MessageApprovalsItem",
    "MessageContentItem",
    "MessageContentItem_Image",
    "MessageContentItem_OmittedReasoning",
    "MessageContentItem_Reasoning",
    "MessageContentItem_RedactedReasoning",
    "MessageContentItem_SummarizedReasoning",
    "MessageContentItem_Text",
    "MessageContentItem_ToolCall",
    "MessageContentItem_ToolReturn",
    "MessageCreate",
    "MessageCreateContent",
    "MessageCreateRole",
    "MessageCreateType",
    "MessageRole",
    "MessageSearchResult",
    "MessageType",
    "ModalSandboxConfig",
    "ModalSandboxConfigLanguage",
    "Model",
    "ModelCompatibilityType",
    "ModelEffort",
    "ModelModelEndpointType",
    "ModelModelType",
    "ModelReasoningEffort",
    "ModelResponseFormat",
    "ModelResponseFormat_JsonObject",
    "ModelResponseFormat_JsonSchema",
    "ModelResponseFormat_Text",
    "ModelVerbosity",
    "ModifyApprovalRequest",
    "NotFoundErrorBody",
    "NotFoundErrorBodyErrorCode",
    "NotFoundErrorBodyMessage",
    "NpmRequirement",
    "OmittedReasoningContent",
    "OpenAiModelSettings",
    "OpenAiModelSettingsResponseFormat",
    "OpenAiModelSettingsResponseFormat_JsonObject",
    "OpenAiModelSettingsResponseFormat_JsonSchema",
    "OpenAiModelSettingsResponseFormat_Text",
    "OpenAiReasoning",
    "OpenAiReasoningReasoningEffort",
    "OpenaiTypesChatChatCompletionMessageFunctionToolCallFunction",
    "OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction",
    "Organization",
    "OrganizationCreate",
    "OrganizationSourcesStats",
    "OrganizationUpdate",
    "PaginatedAgentFiles",
    "ParameterProperties",
    "ParametersSchema",
    "ParentToolRule",
    "Passage",
    "PassageSearchResult",
    "PaymentRequiredErrorBody",
    "PipRequirement",
    "PipelinesListPipelinesRequestOffset",
    "ProjectsListProjectsRequestOffset",
    "PromptTokensDetails",
    "Provider",
    "ProviderCategory",
    "ProviderTrace",
    "ProviderType",
    "ReasoningContent",
    "ReasoningMessage",
    "ReasoningMessageListResult",
    "ReasoningMessageSource",
    "RedactedReasoningContent",
    "RequiredBeforeExitToolRule",
    "RequiresApprovalToolRule",
    "RetrieveStreamRequest",
    "RoundRobinManager",
    "RoundRobinManagerUpdate",
    "Run",
    "RunMetrics",
    "RunStatus",
    "SandboxConfig",
    "SandboxConfigCreate",
    "SandboxConfigCreateConfig",
    "SandboxConfigUpdate",
    "SandboxConfigUpdateConfig",
    "SandboxEnvironmentVariable",
    "SandboxEnvironmentVariableCreate",
    "SandboxEnvironmentVariableUpdate",
    "SandboxType",
    "SleeptimeManager",
    "SleeptimeManagerUpdate",
    "Source",
    "SourceCreate",
    "SourceSchema",
    "SourceStats",
    "SourceUpdate",
    "SseServerConfig",
    "SsemcpServer",
    "StdioMcpServer",
    "StdioServerConfig",
    "Step",
    "StepFeedback",
    "StepMetrics",
    "StepStatus",
    "StopReasonType",
    "StreamableHttpServerConfig",
    "StreamableHttpmcpServer",
    "SummarizedReasoningContent",
    "SummarizedReasoningContentPart",
    "SummaryMessage",
    "SupervisorManager",
    "SupervisorManagerUpdate",
    "SystemMessage",
    "SystemMessageListResult",
    "TagSchema",
    "TemplatesListTemplateVersionsRequestOffset",
    "TemplatesListTemplatesRequestOffset",
    "TerminalToolRule",
    "TextContent",
    "TextResponseFormat",
    "TogetherModelSettings",
    "TogetherModelSettingsResponseFormat",
    "TogetherModelSettingsResponseFormat_JsonObject",
    "TogetherModelSettingsResponseFormat_JsonSchema",
    "TogetherModelSettingsResponseFormat_Text",
    "Tool",
    "ToolAnnotations",
    "ToolCall",
    "ToolCallContent",
    "ToolCallDelta",
    "ToolCallMessage",
    "ToolCallMessageToolCall",
    "ToolCallMessageToolCalls",
    "ToolCallNode",
    "ToolCreate",
    "ToolEnvVarSchema",
    "ToolExecutionResult",
    "ToolExecutionResultStatus",
    "ToolJsonSchema",
    "ToolReturnContent",
    "ToolReturnMessage",
    "ToolReturnMessageMessageType",
    "ToolReturnMessageStatus",
    "ToolSearchResult",
    "ToolType",
    "TopLogprob",
    "UpdateAssistantMessage",
    "UpdateAssistantMessageContent",
    "UpdateReasoningMessage",
    "UpdateSystemMessage",
    "UpdateUserMessage",
    "UpdateUserMessageContent",
    "UrlImage",
    "UsageStatistics",
    "UsageStatisticsCompletionTokenDetails",
    "UsageStatisticsPromptTokenDetails",
    "User",
    "UserCreate",
    "UserMessage",
    "UserMessageContent",
    "UserMessageListResult",
    "UserMessageListResultContent",
    "UserUpdate",
    "ValidationError",
    "ValidationErrorLocItem",
    "VectorDbProvider",
    "VoiceSleeptimeManager",
    "VoiceSleeptimeManagerUpdate",
    "XaiModelSettings",
    "XaiModelSettingsResponseFormat",
    "XaiModelSettingsResponseFormat_JsonObject",
    "XaiModelSettingsResponseFormat_JsonSchema",
    "XaiModelSettingsResponseFormat_Text",
    "ZaiModelSettings",
    "ZaiModelSettingsResponseFormat",
    "ZaiModelSettingsResponseFormat_JsonObject",
    "ZaiModelSettingsResponseFormat_JsonSchema",
    "ZaiModelSettingsResponseFormat_Text",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_provider import AddProvider
    from .agent_capabilities import AgentCapabilities
    from .agent_card_input import AgentCardInput
    from .agent_card_output import AgentCardOutput
    from .agent_card_signature import AgentCardSignature
    from .agent_extension import AgentExtension
    from .agent_interface import AgentInterface
    from .agent_provider import AgentProvider
    from .agent_skill import AgentSkill
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output1 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output10 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output11 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output12 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output13 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output14 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output15 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output16 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output17 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output1registry import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1Registry,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output1source import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1Source,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output1state import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1State,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2registry import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Registry,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2source import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Source,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2state import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2State,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3registry import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3Registry,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3source import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3Source,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3state import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3State,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output4 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output5 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output6 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput6,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output7 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput7,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output8 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8,
    )
    from .agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output9 import (
        AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9,
    )
    from .api_key_security_scheme import ApiKeySecurityScheme
    from .artifact_input import ArtifactInput
    from .artifact_output import ArtifactOutput
    from .audio import Audio
    from .authorization_code_o_auth_flow import AuthorizationCodeOAuthFlow
    from .authorization_code_request import AuthorizationCodeRequest
    from .build_configuration import BuildConfiguration
    from .build_state import BuildState
    from .chat_completion_allowed_tool_choice_param import ChatCompletionAllowedToolChoiceParam
    from .chat_completion_allowed_tool_choice_param_type import ChatCompletionAllowedToolChoiceParamType
    from .chat_completion_allowed_tools_param import ChatCompletionAllowedToolsParam
    from .chat_completion_allowed_tools_param_mode import ChatCompletionAllowedToolsParamMode
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
    from .chat_completion_audio_param import ChatCompletionAudioParam
    from .chat_completion_audio_param_format import ChatCompletionAudioParamFormat
    from .chat_completion_audio_param_voice import ChatCompletionAudioParamVoice
    from .chat_completion_audio_param_voice_one import ChatCompletionAudioParamVoiceOne
    from .chat_completion_content_part_image_param import ChatCompletionContentPartImageParam
    from .chat_completion_content_part_input_audio_param import ChatCompletionContentPartInputAudioParam
    from .chat_completion_content_part_refusal_param import ChatCompletionContentPartRefusalParam
    from .chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
    from .chat_completion_content_part_text_param_type import ChatCompletionContentPartTextParamType
    from .chat_completion_developer_message_param import ChatCompletionDeveloperMessageParam
    from .chat_completion_developer_message_param_content import ChatCompletionDeveloperMessageParamContent
    from .chat_completion_function_call_option_param import ChatCompletionFunctionCallOptionParam
    from .chat_completion_function_message_param import ChatCompletionFunctionMessageParam
    from .chat_completion_function_tool_param import ChatCompletionFunctionToolParam
    from .chat_completion_function_tool_param_type import ChatCompletionFunctionToolParamType
    from .chat_completion_message_custom_tool_call_param import ChatCompletionMessageCustomToolCallParam
    from .chat_completion_message_function_tool_call_param import ChatCompletionMessageFunctionToolCallParam
    from .chat_completion_named_tool_choice_custom_param import ChatCompletionNamedToolChoiceCustomParam
    from .chat_completion_named_tool_choice_custom_param_type import ChatCompletionNamedToolChoiceCustomParamType
    from .chat_completion_named_tool_choice_param import ChatCompletionNamedToolChoiceParam
    from .chat_completion_named_tool_choice_param_type import ChatCompletionNamedToolChoiceParamType
    from .chat_completion_prediction_content_param import ChatCompletionPredictionContentParam
    from .chat_completion_prediction_content_param_content import ChatCompletionPredictionContentParamContent
    from .chat_completion_prediction_content_param_type import ChatCompletionPredictionContentParamType
    from .chat_completion_stream_options_param import ChatCompletionStreamOptionsParam
    from .chat_completion_system_message_param import ChatCompletionSystemMessageParam
    from .chat_completion_system_message_param_content import ChatCompletionSystemMessageParamContent
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
    from .client_credentials_o_auth_flow import ClientCredentialsOAuthFlow
    from .connector_preset_response import ConnectorPresetResponse
    from .connector_response import ConnectorResponse
    from .connector_response_auth_request import ConnectorResponseAuthRequest, ConnectorResponseAuthRequest_Code
    from .connector_state import ConnectorState
    from .context import Context
    from .context_history_item import ContextHistoryItem
    from .context_history_item_create_request import ContextHistoryItemCreateRequest
    from .context_history_item_data_input import ContextHistoryItemDataInput
    from .context_history_item_data_output import ContextHistoryItemDataOutput
    from .context_history_item_kind import ContextHistoryItemKind
    from .context_permissions_grant import ContextPermissionsGrant
    from .context_permissions_grant_context_data_item import ContextPermissionsGrantContextDataItem
    from .context_permissions_grant_files_item import ContextPermissionsGrantFilesItem
    from .context_permissions_grant_vector_stores_item import ContextPermissionsGrantVectorStoresItem
    from .context_token_response import ContextTokenResponse
    from .create_provider_build_request import CreateProviderBuildRequest
    from .create_provider_request import CreateProviderRequest
    from .create_provider_request_location import CreateProviderRequestLocation
    from .data_part import DataPart
    from .discovery_state import DiscoveryState
    from .docker_image_id import DockerImageId
    from .docker_image_provider_location import DockerImageProviderLocation
    from .document_type import DocumentType
    from .env_var import EnvVar
    from .extracted_file_info import ExtractedFileInfo
    from .extraction_format import ExtractionFormat
    from .extraction_metadata import ExtractionMetadata
    from .extraction_status import ExtractionStatus
    from .file_file import FileFile
    from .file_input import FileInput
    from .file_list_query import FileListQuery
    from .file_output import FileOutput
    from .file_part import FilePart
    from .file_part_file import FilePartFile
    from .file_system_model_provider_registry_location import FileSystemModelProviderRegistryLocation
    from .file_system_registry_location import FileSystemRegistryLocation
    from .file_type import FileType
    from .file_with_bytes import FileWithBytes
    from .file_with_uri import FileWithUri
    from .function_call import FunctionCall
    from .function_definition import FunctionDefinition
    from .github_registry_location import GithubRegistryLocation
    from .github_url import GithubUrl
    from .github_version_type import GithubVersionType
    from .global_permission_grant import GlobalPermissionGrant
    from .global_permission_grant_a2a_proxy import GlobalPermissionGrantA2AProxy
    from .global_permission_grant_a2a_proxy_zero_item import GlobalPermissionGrantA2AProxyZeroItem
    from .global_permission_grant_connectors_item import GlobalPermissionGrantConnectorsItem
    from .global_permission_grant_context_data_item import GlobalPermissionGrantContextDataItem
    from .global_permission_grant_contexts_item import GlobalPermissionGrantContextsItem
    from .global_permission_grant_embeddings_item import GlobalPermissionGrantEmbeddingsItem
    from .global_permission_grant_embeddings_item_zero import GlobalPermissionGrantEmbeddingsItemZero
    from .global_permission_grant_feedback_item import GlobalPermissionGrantFeedbackItem
    from .global_permission_grant_files_item import GlobalPermissionGrantFilesItem
    from .global_permission_grant_llm_item import GlobalPermissionGrantLlmItem
    from .global_permission_grant_llm_item_zero import GlobalPermissionGrantLlmItemZero
    from .global_permission_grant_model_providers_item import GlobalPermissionGrantModelProvidersItem
    from .global_permission_grant_provider_variables_item import GlobalPermissionGrantProviderVariablesItem
    from .global_permission_grant_providers_item import GlobalPermissionGrantProvidersItem
    from .global_permission_grant_vector_stores_item import GlobalPermissionGrantVectorStoresItem
    from .http_auth_security_scheme import HttpAuthSecurityScheme
    from .http_validation_error import HttpValidationError
    from .image_url import ImageUrl
    from .image_url_detail import ImageUrlDetail
    from .implicit_o_auth_flow import ImplicitOAuthFlow
    from .in_ import In
    from .input_audio import InputAudio
    from .input_audio_format import InputAudioFormat
    from .json_schema import JsonSchema
    from .list_variables_schema import ListVariablesSchema
    from .message_input import MessageInput
    from .message_input_kind import MessageInputKind
    from .message_output import MessageOutput
    from .message_output_kind import MessageOutputKind
    from .model import Model
    from .model_capability import ModelCapability
    from .model_object import ModelObject
    from .model_provider import ModelProvider
    from .model_provider_info import ModelProviderInfo
    from .model_provider_state import ModelProviderState
    from .model_provider_type import ModelProviderType
    from .model_with_score import ModelWithScore
    from .mutual_tls_security_scheme import MutualTlsSecurityScheme
    from .network_provider_location import NetworkProviderLocation
    from .network_registry_location import NetworkRegistryLocation
    from .no_action import NoAction
    from .o_auth2security_scheme_input import OAuth2SecuritySchemeInput
    from .o_auth2security_scheme_output import OAuth2SecuritySchemeOutput
    from .o_auth_flows import OAuthFlows
    from .on_complete_action import (
        OnCompleteAction,
        OnCompleteAction_AddProvider,
        OnCompleteAction_NoAction,
        OnCompleteAction_UpdateProvider,
    )
    from .open_ai_page_model import OpenAiPageModel
    from .open_ai_page_model_object import OpenAiPageModelObject
    from .open_id_connect_security_scheme import OpenIdConnectSecurityScheme
    from .openai_types_chat_chat_completion_message_custom_tool_call_param_custom import (
        OpenaiTypesChatChatCompletionMessageCustomToolCallParamCustom,
    )
    from .openai_types_chat_chat_completion_message_function_tool_call_param_function import (
        OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction,
    )
    from .openai_types_chat_chat_completion_named_tool_choice_custom_param_custom import (
        OpenaiTypesChatChatCompletionNamedToolChoiceCustomParamCustom,
    )
    from .openai_types_chat_chat_completion_named_tool_choice_param_function import (
        OpenaiTypesChatChatCompletionNamedToolChoiceParamFunction,
    )
    from .openai_types_chat_completion_create_params_function import OpenaiTypesChatCompletionCreateParamsFunction
    from .paginated_result_connector_preset_response import PaginatedResultConnectorPresetResponse
    from .paginated_result_connector_response import PaginatedResultConnectorResponse
    from .paginated_result_context import PaginatedResultContext
    from .paginated_result_context_history_item import PaginatedResultContextHistoryItem
    from .paginated_result_file import PaginatedResultFile
    from .paginated_result_model_output import PaginatedResultModelOutput
    from .paginated_result_model_provider import PaginatedResultModelProvider
    from .paginated_result_model_with_score import PaginatedResultModelWithScore
    from .paginated_result_provider_build import PaginatedResultProviderBuild
    from .paginated_result_user_feedback_response import PaginatedResultUserFeedbackResponse
    from .paginated_result_vector_store_document import PaginatedResultVectorStoreDocument
    from .paginated_result_vector_store_search_result import PaginatedResultVectorStoreSearchResult
    from .part_input import PartInput, PartInput_Data, PartInput_File, PartInput_Text
    from .part_output import PartOutput, PartOutput_Data, PartOutput_File, PartOutput_Text
    from .password_o_auth_flow import PasswordOAuthFlow
    from .provider_build import ProviderBuild
    from .provider_deployment_state import ProviderDeploymentState
    from .provider_discovery import ProviderDiscovery
    from .provider_error_message import ProviderErrorMessage
    from .provider_type import ProviderType
    from .provider_with_state import ProviderWithState
    from .provider_with_state_registry import ProviderWithStateRegistry
    from .provider_with_state_source import ProviderWithStateSource
    from .provider_with_state_state import ProviderWithStateState
    from .resolved_docker_image_id import ResolvedDockerImageId
    from .resolved_github_url import ResolvedGithubUrl
    from .response_format_json_object import ResponseFormatJsonObject
    from .response_format_json_object_type import ResponseFormatJsonObjectType
    from .response_format_json_schema import ResponseFormatJsonSchema
    from .response_format_json_schema_type import ResponseFormatJsonSchemaType
    from .response_format_text import ResponseFormatText
    from .response_format_text_type import ResponseFormatTextType
    from .role import Role
    from .security_scheme_input import (
        SecuritySchemeInput,
        SecuritySchemeInput_ApiKey,
        SecuritySchemeInput_Http,
        SecuritySchemeInput_MutualTls,
        SecuritySchemeInput_Oauth2,
        SecuritySchemeInput_OpenIdConnect,
    )
    from .security_scheme_output import (
        SecuritySchemeOutput,
        SecuritySchemeOutput_ApiKey,
        SecuritySchemeOutput_Http,
        SecuritySchemeOutput_MutualTls,
        SecuritySchemeOutput_Oauth2,
        SecuritySchemeOutput_OpenIdConnect,
    )
    from .text_extraction_request import TextExtractionRequest
    from .text_extraction_settings import TextExtractionSettings
    from .text_part import TextPart
    from .unmanaged_state import UnmanagedState
    from .update_provider import UpdateProvider
    from .update_variables_request import UpdateVariablesRequest
    from .user import User
    from .user_feedback_response import UserFeedbackResponse
    from .user_response import UserResponse
    from .user_role import UserRole
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .vector_store_document import VectorStoreDocument
    from .vector_store_item import VectorStoreItem
    from .vector_store_item_model_id import VectorStoreItemModelId
    from .vector_store_item_model_id_one import VectorStoreItemModelIdOne
    from .vector_store_search_result import VectorStoreSearchResult
    from .vector_store_stats import VectorStoreStats
    from .version_info import VersionInfo
    from .web_search_options import WebSearchOptions
    from .web_search_options_search_context_size import WebSearchOptionsSearchContextSize
    from .web_search_options_user_location import WebSearchOptionsUserLocation
    from .web_search_options_user_location_approximate import WebSearchOptionsUserLocationApproximate
    from .web_search_options_user_location_type import WebSearchOptionsUserLocationType
_dynamic_imports: typing.Dict[str, str] = {
    "AddProvider": ".add_provider",
    "AgentCapabilities": ".agent_capabilities",
    "AgentCardInput": ".agent_card_input",
    "AgentCardOutput": ".agent_card_output",
    "AgentCardSignature": ".agent_card_signature",
    "AgentExtension": ".agent_extension",
    "AgentInterface": ".agent_interface",
    "AgentProvider": ".agent_provider",
    "AgentSkill": ".agent_skill",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output1",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output10",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output11",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output12",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output13",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output14",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output15",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output16",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output17",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1Registry": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output1registry",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1Source": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output1source",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1State": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output1state",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Registry": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2registry",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Source": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2source",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2State": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output2state",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3Registry": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3registry",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3Source": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3source",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3State": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output3state",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output4",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output5",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput6": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output6",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput7": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output7",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output8",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9": ".agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output9",
    "ApiKeySecurityScheme": ".api_key_security_scheme",
    "ArtifactInput": ".artifact_input",
    "ArtifactOutput": ".artifact_output",
    "Audio": ".audio",
    "AuthorizationCodeOAuthFlow": ".authorization_code_o_auth_flow",
    "AuthorizationCodeRequest": ".authorization_code_request",
    "BuildConfiguration": ".build_configuration",
    "BuildState": ".build_state",
    "ChatCompletionAllowedToolChoiceParam": ".chat_completion_allowed_tool_choice_param",
    "ChatCompletionAllowedToolChoiceParamType": ".chat_completion_allowed_tool_choice_param_type",
    "ChatCompletionAllowedToolsParam": ".chat_completion_allowed_tools_param",
    "ChatCompletionAllowedToolsParamMode": ".chat_completion_allowed_tools_param_mode",
    "ChatCompletionAssistantMessageParam": ".chat_completion_assistant_message_param",
    "ChatCompletionAssistantMessageParamContent": ".chat_completion_assistant_message_param_content",
    "ChatCompletionAssistantMessageParamContentOneItem": ".chat_completion_assistant_message_param_content_one_item",
    "ChatCompletionAssistantMessageParamContentOneItem_Refusal": ".chat_completion_assistant_message_param_content_one_item",
    "ChatCompletionAssistantMessageParamContentOneItem_Text": ".chat_completion_assistant_message_param_content_one_item",
    "ChatCompletionAssistantMessageParamToolCallsItem": ".chat_completion_assistant_message_param_tool_calls_item",
    "ChatCompletionAssistantMessageParamToolCallsItem_Custom": ".chat_completion_assistant_message_param_tool_calls_item",
    "ChatCompletionAssistantMessageParamToolCallsItem_Function": ".chat_completion_assistant_message_param_tool_calls_item",
    "ChatCompletionAudioParam": ".chat_completion_audio_param",
    "ChatCompletionAudioParamFormat": ".chat_completion_audio_param_format",
    "ChatCompletionAudioParamVoice": ".chat_completion_audio_param_voice",
    "ChatCompletionAudioParamVoiceOne": ".chat_completion_audio_param_voice_one",
    "ChatCompletionContentPartImageParam": ".chat_completion_content_part_image_param",
    "ChatCompletionContentPartInputAudioParam": ".chat_completion_content_part_input_audio_param",
    "ChatCompletionContentPartRefusalParam": ".chat_completion_content_part_refusal_param",
    "ChatCompletionContentPartTextParam": ".chat_completion_content_part_text_param",
    "ChatCompletionContentPartTextParamType": ".chat_completion_content_part_text_param_type",
    "ChatCompletionDeveloperMessageParam": ".chat_completion_developer_message_param",
    "ChatCompletionDeveloperMessageParamContent": ".chat_completion_developer_message_param_content",
    "ChatCompletionFunctionCallOptionParam": ".chat_completion_function_call_option_param",
    "ChatCompletionFunctionMessageParam": ".chat_completion_function_message_param",
    "ChatCompletionFunctionToolParam": ".chat_completion_function_tool_param",
    "ChatCompletionFunctionToolParamType": ".chat_completion_function_tool_param_type",
    "ChatCompletionMessageCustomToolCallParam": ".chat_completion_message_custom_tool_call_param",
    "ChatCompletionMessageFunctionToolCallParam": ".chat_completion_message_function_tool_call_param",
    "ChatCompletionNamedToolChoiceCustomParam": ".chat_completion_named_tool_choice_custom_param",
    "ChatCompletionNamedToolChoiceCustomParamType": ".chat_completion_named_tool_choice_custom_param_type",
    "ChatCompletionNamedToolChoiceParam": ".chat_completion_named_tool_choice_param",
    "ChatCompletionNamedToolChoiceParamType": ".chat_completion_named_tool_choice_param_type",
    "ChatCompletionPredictionContentParam": ".chat_completion_prediction_content_param",
    "ChatCompletionPredictionContentParamContent": ".chat_completion_prediction_content_param_content",
    "ChatCompletionPredictionContentParamType": ".chat_completion_prediction_content_param_type",
    "ChatCompletionStreamOptionsParam": ".chat_completion_stream_options_param",
    "ChatCompletionSystemMessageParam": ".chat_completion_system_message_param",
    "ChatCompletionSystemMessageParamContent": ".chat_completion_system_message_param_content",
    "ChatCompletionToolMessageParam": ".chat_completion_tool_message_param",
    "ChatCompletionToolMessageParamContent": ".chat_completion_tool_message_param_content",
    "ChatCompletionUserMessageParam": ".chat_completion_user_message_param",
    "ChatCompletionUserMessageParamContent": ".chat_completion_user_message_param_content",
    "ChatCompletionUserMessageParamContentOneItem": ".chat_completion_user_message_param_content_one_item",
    "ChatCompletionUserMessageParamContentOneItem_File": ".chat_completion_user_message_param_content_one_item",
    "ChatCompletionUserMessageParamContentOneItem_ImageUrl": ".chat_completion_user_message_param_content_one_item",
    "ChatCompletionUserMessageParamContentOneItem_InputAudio": ".chat_completion_user_message_param_content_one_item",
    "ChatCompletionUserMessageParamContentOneItem_Text": ".chat_completion_user_message_param_content_one_item",
    "ClientCredentialsOAuthFlow": ".client_credentials_o_auth_flow",
    "ConnectorPresetResponse": ".connector_preset_response",
    "ConnectorResponse": ".connector_response",
    "ConnectorResponseAuthRequest": ".connector_response_auth_request",
    "ConnectorResponseAuthRequest_Code": ".connector_response_auth_request",
    "ConnectorState": ".connector_state",
    "Context": ".context",
    "ContextHistoryItem": ".context_history_item",
    "ContextHistoryItemCreateRequest": ".context_history_item_create_request",
    "ContextHistoryItemDataInput": ".context_history_item_data_input",
    "ContextHistoryItemDataOutput": ".context_history_item_data_output",
    "ContextHistoryItemKind": ".context_history_item_kind",
    "ContextPermissionsGrant": ".context_permissions_grant",
    "ContextPermissionsGrantContextDataItem": ".context_permissions_grant_context_data_item",
    "ContextPermissionsGrantFilesItem": ".context_permissions_grant_files_item",
    "ContextPermissionsGrantVectorStoresItem": ".context_permissions_grant_vector_stores_item",
    "ContextTokenResponse": ".context_token_response",
    "CreateProviderBuildRequest": ".create_provider_build_request",
    "CreateProviderRequest": ".create_provider_request",
    "CreateProviderRequestLocation": ".create_provider_request_location",
    "DataPart": ".data_part",
    "DiscoveryState": ".discovery_state",
    "DockerImageId": ".docker_image_id",
    "DockerImageProviderLocation": ".docker_image_provider_location",
    "DocumentType": ".document_type",
    "EnvVar": ".env_var",
    "ExtractedFileInfo": ".extracted_file_info",
    "ExtractionFormat": ".extraction_format",
    "ExtractionMetadata": ".extraction_metadata",
    "ExtractionStatus": ".extraction_status",
    "FileFile": ".file_file",
    "FileInput": ".file_input",
    "FileListQuery": ".file_list_query",
    "FileOutput": ".file_output",
    "FilePart": ".file_part",
    "FilePartFile": ".file_part_file",
    "FileSystemModelProviderRegistryLocation": ".file_system_model_provider_registry_location",
    "FileSystemRegistryLocation": ".file_system_registry_location",
    "FileType": ".file_type",
    "FileWithBytes": ".file_with_bytes",
    "FileWithUri": ".file_with_uri",
    "FunctionCall": ".function_call",
    "FunctionDefinition": ".function_definition",
    "GithubRegistryLocation": ".github_registry_location",
    "GithubUrl": ".github_url",
    "GithubVersionType": ".github_version_type",
    "GlobalPermissionGrant": ".global_permission_grant",
    "GlobalPermissionGrantA2AProxy": ".global_permission_grant_a2a_proxy",
    "GlobalPermissionGrantA2AProxyZeroItem": ".global_permission_grant_a2a_proxy_zero_item",
    "GlobalPermissionGrantConnectorsItem": ".global_permission_grant_connectors_item",
    "GlobalPermissionGrantContextDataItem": ".global_permission_grant_context_data_item",
    "GlobalPermissionGrantContextsItem": ".global_permission_grant_contexts_item",
    "GlobalPermissionGrantEmbeddingsItem": ".global_permission_grant_embeddings_item",
    "GlobalPermissionGrantEmbeddingsItemZero": ".global_permission_grant_embeddings_item_zero",
    "GlobalPermissionGrantFeedbackItem": ".global_permission_grant_feedback_item",
    "GlobalPermissionGrantFilesItem": ".global_permission_grant_files_item",
    "GlobalPermissionGrantLlmItem": ".global_permission_grant_llm_item",
    "GlobalPermissionGrantLlmItemZero": ".global_permission_grant_llm_item_zero",
    "GlobalPermissionGrantModelProvidersItem": ".global_permission_grant_model_providers_item",
    "GlobalPermissionGrantProviderVariablesItem": ".global_permission_grant_provider_variables_item",
    "GlobalPermissionGrantProvidersItem": ".global_permission_grant_providers_item",
    "GlobalPermissionGrantVectorStoresItem": ".global_permission_grant_vector_stores_item",
    "HttpAuthSecurityScheme": ".http_auth_security_scheme",
    "HttpValidationError": ".http_validation_error",
    "ImageUrl": ".image_url",
    "ImageUrlDetail": ".image_url_detail",
    "ImplicitOAuthFlow": ".implicit_o_auth_flow",
    "In": ".in_",
    "InputAudio": ".input_audio",
    "InputAudioFormat": ".input_audio_format",
    "JsonSchema": ".json_schema",
    "ListVariablesSchema": ".list_variables_schema",
    "MessageInput": ".message_input",
    "MessageInputKind": ".message_input_kind",
    "MessageOutput": ".message_output",
    "MessageOutputKind": ".message_output_kind",
    "Model": ".model",
    "ModelCapability": ".model_capability",
    "ModelObject": ".model_object",
    "ModelProvider": ".model_provider",
    "ModelProviderInfo": ".model_provider_info",
    "ModelProviderState": ".model_provider_state",
    "ModelProviderType": ".model_provider_type",
    "ModelWithScore": ".model_with_score",
    "MutualTlsSecurityScheme": ".mutual_tls_security_scheme",
    "NetworkProviderLocation": ".network_provider_location",
    "NetworkRegistryLocation": ".network_registry_location",
    "NoAction": ".no_action",
    "OAuth2SecuritySchemeInput": ".o_auth2security_scheme_input",
    "OAuth2SecuritySchemeOutput": ".o_auth2security_scheme_output",
    "OAuthFlows": ".o_auth_flows",
    "OnCompleteAction": ".on_complete_action",
    "OnCompleteAction_AddProvider": ".on_complete_action",
    "OnCompleteAction_NoAction": ".on_complete_action",
    "OnCompleteAction_UpdateProvider": ".on_complete_action",
    "OpenAiPageModel": ".open_ai_page_model",
    "OpenAiPageModelObject": ".open_ai_page_model_object",
    "OpenIdConnectSecurityScheme": ".open_id_connect_security_scheme",
    "OpenaiTypesChatChatCompletionMessageCustomToolCallParamCustom": ".openai_types_chat_chat_completion_message_custom_tool_call_param_custom",
    "OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction": ".openai_types_chat_chat_completion_message_function_tool_call_param_function",
    "OpenaiTypesChatChatCompletionNamedToolChoiceCustomParamCustom": ".openai_types_chat_chat_completion_named_tool_choice_custom_param_custom",
    "OpenaiTypesChatChatCompletionNamedToolChoiceParamFunction": ".openai_types_chat_chat_completion_named_tool_choice_param_function",
    "OpenaiTypesChatCompletionCreateParamsFunction": ".openai_types_chat_completion_create_params_function",
    "PaginatedResultConnectorPresetResponse": ".paginated_result_connector_preset_response",
    "PaginatedResultConnectorResponse": ".paginated_result_connector_response",
    "PaginatedResultContext": ".paginated_result_context",
    "PaginatedResultContextHistoryItem": ".paginated_result_context_history_item",
    "PaginatedResultFile": ".paginated_result_file",
    "PaginatedResultModelOutput": ".paginated_result_model_output",
    "PaginatedResultModelProvider": ".paginated_result_model_provider",
    "PaginatedResultModelWithScore": ".paginated_result_model_with_score",
    "PaginatedResultProviderBuild": ".paginated_result_provider_build",
    "PaginatedResultUserFeedbackResponse": ".paginated_result_user_feedback_response",
    "PaginatedResultVectorStoreDocument": ".paginated_result_vector_store_document",
    "PaginatedResultVectorStoreSearchResult": ".paginated_result_vector_store_search_result",
    "PartInput": ".part_input",
    "PartInput_Data": ".part_input",
    "PartInput_File": ".part_input",
    "PartInput_Text": ".part_input",
    "PartOutput": ".part_output",
    "PartOutput_Data": ".part_output",
    "PartOutput_File": ".part_output",
    "PartOutput_Text": ".part_output",
    "PasswordOAuthFlow": ".password_o_auth_flow",
    "ProviderBuild": ".provider_build",
    "ProviderDeploymentState": ".provider_deployment_state",
    "ProviderDiscovery": ".provider_discovery",
    "ProviderErrorMessage": ".provider_error_message",
    "ProviderType": ".provider_type",
    "ProviderWithState": ".provider_with_state",
    "ProviderWithStateRegistry": ".provider_with_state_registry",
    "ProviderWithStateSource": ".provider_with_state_source",
    "ProviderWithStateState": ".provider_with_state_state",
    "ResolvedDockerImageId": ".resolved_docker_image_id",
    "ResolvedGithubUrl": ".resolved_github_url",
    "ResponseFormatJsonObject": ".response_format_json_object",
    "ResponseFormatJsonObjectType": ".response_format_json_object_type",
    "ResponseFormatJsonSchema": ".response_format_json_schema",
    "ResponseFormatJsonSchemaType": ".response_format_json_schema_type",
    "ResponseFormatText": ".response_format_text",
    "ResponseFormatTextType": ".response_format_text_type",
    "Role": ".role",
    "SecuritySchemeInput": ".security_scheme_input",
    "SecuritySchemeInput_ApiKey": ".security_scheme_input",
    "SecuritySchemeInput_Http": ".security_scheme_input",
    "SecuritySchemeInput_MutualTls": ".security_scheme_input",
    "SecuritySchemeInput_Oauth2": ".security_scheme_input",
    "SecuritySchemeInput_OpenIdConnect": ".security_scheme_input",
    "SecuritySchemeOutput": ".security_scheme_output",
    "SecuritySchemeOutput_ApiKey": ".security_scheme_output",
    "SecuritySchemeOutput_Http": ".security_scheme_output",
    "SecuritySchemeOutput_MutualTls": ".security_scheme_output",
    "SecuritySchemeOutput_Oauth2": ".security_scheme_output",
    "SecuritySchemeOutput_OpenIdConnect": ".security_scheme_output",
    "TextExtractionRequest": ".text_extraction_request",
    "TextExtractionSettings": ".text_extraction_settings",
    "TextPart": ".text_part",
    "UnmanagedState": ".unmanaged_state",
    "UpdateProvider": ".update_provider",
    "UpdateVariablesRequest": ".update_variables_request",
    "User": ".user",
    "UserFeedbackResponse": ".user_feedback_response",
    "UserResponse": ".user_response",
    "UserRole": ".user_role",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VectorStoreDocument": ".vector_store_document",
    "VectorStoreItem": ".vector_store_item",
    "VectorStoreItemModelId": ".vector_store_item_model_id",
    "VectorStoreItemModelIdOne": ".vector_store_item_model_id_one",
    "VectorStoreSearchResult": ".vector_store_search_result",
    "VectorStoreStats": ".vector_store_stats",
    "VersionInfo": ".version_info",
    "WebSearchOptions": ".web_search_options",
    "WebSearchOptionsSearchContextSize": ".web_search_options_search_context_size",
    "WebSearchOptionsUserLocation": ".web_search_options_user_location",
    "WebSearchOptionsUserLocationApproximate": ".web_search_options_user_location_approximate",
    "WebSearchOptionsUserLocationType": ".web_search_options_user_location_type",
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
    "AddProvider",
    "AgentCapabilities",
    "AgentCardInput",
    "AgentCardOutput",
    "AgentCardSignature",
    "AgentExtension",
    "AgentInterface",
    "AgentProvider",
    "AgentSkill",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput10",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput11",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput16",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput17",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1Registry",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1Source",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput1State",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Registry",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2Source",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput2State",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3Registry",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3Source",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput3State",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput4",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput5",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput6",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput7",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput8",
    "AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput9",
    "ApiKeySecurityScheme",
    "ArtifactInput",
    "ArtifactOutput",
    "Audio",
    "AuthorizationCodeOAuthFlow",
    "AuthorizationCodeRequest",
    "BuildConfiguration",
    "BuildState",
    "ChatCompletionAllowedToolChoiceParam",
    "ChatCompletionAllowedToolChoiceParamType",
    "ChatCompletionAllowedToolsParam",
    "ChatCompletionAllowedToolsParamMode",
    "ChatCompletionAssistantMessageParam",
    "ChatCompletionAssistantMessageParamContent",
    "ChatCompletionAssistantMessageParamContentOneItem",
    "ChatCompletionAssistantMessageParamContentOneItem_Refusal",
    "ChatCompletionAssistantMessageParamContentOneItem_Text",
    "ChatCompletionAssistantMessageParamToolCallsItem",
    "ChatCompletionAssistantMessageParamToolCallsItem_Custom",
    "ChatCompletionAssistantMessageParamToolCallsItem_Function",
    "ChatCompletionAudioParam",
    "ChatCompletionAudioParamFormat",
    "ChatCompletionAudioParamVoice",
    "ChatCompletionAudioParamVoiceOne",
    "ChatCompletionContentPartImageParam",
    "ChatCompletionContentPartInputAudioParam",
    "ChatCompletionContentPartRefusalParam",
    "ChatCompletionContentPartTextParam",
    "ChatCompletionContentPartTextParamType",
    "ChatCompletionDeveloperMessageParam",
    "ChatCompletionDeveloperMessageParamContent",
    "ChatCompletionFunctionCallOptionParam",
    "ChatCompletionFunctionMessageParam",
    "ChatCompletionFunctionToolParam",
    "ChatCompletionFunctionToolParamType",
    "ChatCompletionMessageCustomToolCallParam",
    "ChatCompletionMessageFunctionToolCallParam",
    "ChatCompletionNamedToolChoiceCustomParam",
    "ChatCompletionNamedToolChoiceCustomParamType",
    "ChatCompletionNamedToolChoiceParam",
    "ChatCompletionNamedToolChoiceParamType",
    "ChatCompletionPredictionContentParam",
    "ChatCompletionPredictionContentParamContent",
    "ChatCompletionPredictionContentParamType",
    "ChatCompletionStreamOptionsParam",
    "ChatCompletionSystemMessageParam",
    "ChatCompletionSystemMessageParamContent",
    "ChatCompletionToolMessageParam",
    "ChatCompletionToolMessageParamContent",
    "ChatCompletionUserMessageParam",
    "ChatCompletionUserMessageParamContent",
    "ChatCompletionUserMessageParamContentOneItem",
    "ChatCompletionUserMessageParamContentOneItem_File",
    "ChatCompletionUserMessageParamContentOneItem_ImageUrl",
    "ChatCompletionUserMessageParamContentOneItem_InputAudio",
    "ChatCompletionUserMessageParamContentOneItem_Text",
    "ClientCredentialsOAuthFlow",
    "ConnectorPresetResponse",
    "ConnectorResponse",
    "ConnectorResponseAuthRequest",
    "ConnectorResponseAuthRequest_Code",
    "ConnectorState",
    "Context",
    "ContextHistoryItem",
    "ContextHistoryItemCreateRequest",
    "ContextHistoryItemDataInput",
    "ContextHistoryItemDataOutput",
    "ContextHistoryItemKind",
    "ContextPermissionsGrant",
    "ContextPermissionsGrantContextDataItem",
    "ContextPermissionsGrantFilesItem",
    "ContextPermissionsGrantVectorStoresItem",
    "ContextTokenResponse",
    "CreateProviderBuildRequest",
    "CreateProviderRequest",
    "CreateProviderRequestLocation",
    "DataPart",
    "DiscoveryState",
    "DockerImageId",
    "DockerImageProviderLocation",
    "DocumentType",
    "EnvVar",
    "ExtractedFileInfo",
    "ExtractionFormat",
    "ExtractionMetadata",
    "ExtractionStatus",
    "FileFile",
    "FileInput",
    "FileListQuery",
    "FileOutput",
    "FilePart",
    "FilePartFile",
    "FileSystemModelProviderRegistryLocation",
    "FileSystemRegistryLocation",
    "FileType",
    "FileWithBytes",
    "FileWithUri",
    "FunctionCall",
    "FunctionDefinition",
    "GithubRegistryLocation",
    "GithubUrl",
    "GithubVersionType",
    "GlobalPermissionGrant",
    "GlobalPermissionGrantA2AProxy",
    "GlobalPermissionGrantA2AProxyZeroItem",
    "GlobalPermissionGrantConnectorsItem",
    "GlobalPermissionGrantContextDataItem",
    "GlobalPermissionGrantContextsItem",
    "GlobalPermissionGrantEmbeddingsItem",
    "GlobalPermissionGrantEmbeddingsItemZero",
    "GlobalPermissionGrantFeedbackItem",
    "GlobalPermissionGrantFilesItem",
    "GlobalPermissionGrantLlmItem",
    "GlobalPermissionGrantLlmItemZero",
    "GlobalPermissionGrantModelProvidersItem",
    "GlobalPermissionGrantProviderVariablesItem",
    "GlobalPermissionGrantProvidersItem",
    "GlobalPermissionGrantVectorStoresItem",
    "HttpAuthSecurityScheme",
    "HttpValidationError",
    "ImageUrl",
    "ImageUrlDetail",
    "ImplicitOAuthFlow",
    "In",
    "InputAudio",
    "InputAudioFormat",
    "JsonSchema",
    "ListVariablesSchema",
    "MessageInput",
    "MessageInputKind",
    "MessageOutput",
    "MessageOutputKind",
    "Model",
    "ModelCapability",
    "ModelObject",
    "ModelProvider",
    "ModelProviderInfo",
    "ModelProviderState",
    "ModelProviderType",
    "ModelWithScore",
    "MutualTlsSecurityScheme",
    "NetworkProviderLocation",
    "NetworkRegistryLocation",
    "NoAction",
    "OAuth2SecuritySchemeInput",
    "OAuth2SecuritySchemeOutput",
    "OAuthFlows",
    "OnCompleteAction",
    "OnCompleteAction_AddProvider",
    "OnCompleteAction_NoAction",
    "OnCompleteAction_UpdateProvider",
    "OpenAiPageModel",
    "OpenAiPageModelObject",
    "OpenIdConnectSecurityScheme",
    "OpenaiTypesChatChatCompletionMessageCustomToolCallParamCustom",
    "OpenaiTypesChatChatCompletionMessageFunctionToolCallParamFunction",
    "OpenaiTypesChatChatCompletionNamedToolChoiceCustomParamCustom",
    "OpenaiTypesChatChatCompletionNamedToolChoiceParamFunction",
    "OpenaiTypesChatCompletionCreateParamsFunction",
    "PaginatedResultConnectorPresetResponse",
    "PaginatedResultConnectorResponse",
    "PaginatedResultContext",
    "PaginatedResultContextHistoryItem",
    "PaginatedResultFile",
    "PaginatedResultModelOutput",
    "PaginatedResultModelProvider",
    "PaginatedResultModelWithScore",
    "PaginatedResultProviderBuild",
    "PaginatedResultUserFeedbackResponse",
    "PaginatedResultVectorStoreDocument",
    "PaginatedResultVectorStoreSearchResult",
    "PartInput",
    "PartInput_Data",
    "PartInput_File",
    "PartInput_Text",
    "PartOutput",
    "PartOutput_Data",
    "PartOutput_File",
    "PartOutput_Text",
    "PasswordOAuthFlow",
    "ProviderBuild",
    "ProviderDeploymentState",
    "ProviderDiscovery",
    "ProviderErrorMessage",
    "ProviderType",
    "ProviderWithState",
    "ProviderWithStateRegistry",
    "ProviderWithStateSource",
    "ProviderWithStateState",
    "ResolvedDockerImageId",
    "ResolvedGithubUrl",
    "ResponseFormatJsonObject",
    "ResponseFormatJsonObjectType",
    "ResponseFormatJsonSchema",
    "ResponseFormatJsonSchemaType",
    "ResponseFormatText",
    "ResponseFormatTextType",
    "Role",
    "SecuritySchemeInput",
    "SecuritySchemeInput_ApiKey",
    "SecuritySchemeInput_Http",
    "SecuritySchemeInput_MutualTls",
    "SecuritySchemeInput_Oauth2",
    "SecuritySchemeInput_OpenIdConnect",
    "SecuritySchemeOutput",
    "SecuritySchemeOutput_ApiKey",
    "SecuritySchemeOutput_Http",
    "SecuritySchemeOutput_MutualTls",
    "SecuritySchemeOutput_Oauth2",
    "SecuritySchemeOutput_OpenIdConnect",
    "TextExtractionRequest",
    "TextExtractionSettings",
    "TextPart",
    "UnmanagedState",
    "UpdateProvider",
    "UpdateVariablesRequest",
    "User",
    "UserFeedbackResponse",
    "UserResponse",
    "UserRole",
    "ValidationError",
    "ValidationErrorLocItem",
    "VectorStoreDocument",
    "VectorStoreItem",
    "VectorStoreItemModelId",
    "VectorStoreItemModelIdOne",
    "VectorStoreSearchResult",
    "VectorStoreStats",
    "VersionInfo",
    "WebSearchOptions",
    "WebSearchOptionsSearchContextSize",
    "WebSearchOptionsUserLocation",
    "WebSearchOptionsUserLocationApproximate",
    "WebSearchOptionsUserLocationType",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .agents_get_agent_variables_response import AgentsGetAgentVariablesResponse
    from .agents_search_deployed_agents_request_combinator import AgentsSearchDeployedAgentsRequestCombinator
    from .agents_search_deployed_agents_request_search_item import (
        AgentsSearchDeployedAgentsRequestSearchItem,
        AgentsSearchDeployedAgentsRequestSearchItem_AgentId,
        AgentsSearchDeployedAgentsRequestSearchItem_Identity,
        AgentsSearchDeployedAgentsRequestSearchItem_Name,
        AgentsSearchDeployedAgentsRequestSearchItem_Tags,
        AgentsSearchDeployedAgentsRequestSearchItem_TemplateName,
        AgentsSearchDeployedAgentsRequestSearchItem_Version,
    )
    from .agents_search_deployed_agents_request_search_item_agent_id import (
        AgentsSearchDeployedAgentsRequestSearchItemAgentId,
    )
    from .agents_search_deployed_agents_request_search_item_agent_id_operator import (
        AgentsSearchDeployedAgentsRequestSearchItemAgentIdOperator,
    )
    from .agents_search_deployed_agents_request_search_item_identity import (
        AgentsSearchDeployedAgentsRequestSearchItemIdentity,
    )
    from .agents_search_deployed_agents_request_search_item_identity_operator import (
        AgentsSearchDeployedAgentsRequestSearchItemIdentityOperator,
    )
    from .agents_search_deployed_agents_request_search_item_name import AgentsSearchDeployedAgentsRequestSearchItemName
    from .agents_search_deployed_agents_request_search_item_name_operator import (
        AgentsSearchDeployedAgentsRequestSearchItemNameOperator,
    )
    from .agents_search_deployed_agents_request_search_item_tags import AgentsSearchDeployedAgentsRequestSearchItemTags
    from .agents_search_deployed_agents_request_search_item_tags_operator import (
        AgentsSearchDeployedAgentsRequestSearchItemTagsOperator,
    )
    from .agents_search_deployed_agents_request_search_item_template_name import (
        AgentsSearchDeployedAgentsRequestSearchItemTemplateName,
    )
    from .agents_search_deployed_agents_request_search_item_template_name_operator import (
        AgentsSearchDeployedAgentsRequestSearchItemTemplateNameOperator,
    )
    from .agents_search_deployed_agents_request_search_item_version import (
        AgentsSearchDeployedAgentsRequestSearchItemVersion,
    )
    from .agents_search_deployed_agents_request_sort_by import AgentsSearchDeployedAgentsRequestSortBy
    from .agents_search_deployed_agents_response import AgentsSearchDeployedAgentsResponse
    from .create_agent_request_model_settings import (
        CreateAgentRequestModelSettings,
        CreateAgentRequestModelSettings_Anthropic,
        CreateAgentRequestModelSettings_Azure,
        CreateAgentRequestModelSettings_Bedrock,
        CreateAgentRequestModelSettings_ChatgptOauth,
        CreateAgentRequestModelSettings_Deepseek,
        CreateAgentRequestModelSettings_GoogleAi,
        CreateAgentRequestModelSettings_GoogleVertex,
        CreateAgentRequestModelSettings_Groq,
        CreateAgentRequestModelSettings_Openai,
        CreateAgentRequestModelSettings_Together,
        CreateAgentRequestModelSettings_Xai,
        CreateAgentRequestModelSettings_Zai,
    )
    from .create_agent_request_response_format import (
        CreateAgentRequestResponseFormat,
        CreateAgentRequestResponseFormat_JsonObject,
        CreateAgentRequestResponseFormat_JsonSchema,
        CreateAgentRequestResponseFormat_Text,
    )
    from .create_agent_request_tool_rules_item import (
        CreateAgentRequestToolRulesItem,
        CreateAgentRequestToolRulesItem_Conditional,
        CreateAgentRequestToolRulesItem_ConstrainChildTools,
        CreateAgentRequestToolRulesItem_ContinueLoop,
        CreateAgentRequestToolRulesItem_ExitLoop,
        CreateAgentRequestToolRulesItem_MaxCountPerStep,
        CreateAgentRequestToolRulesItem_ParentLastTool,
        CreateAgentRequestToolRulesItem_RequiredBeforeExit,
        CreateAgentRequestToolRulesItem_RequiresApproval,
        CreateAgentRequestToolRulesItem_RunFirst,
    )
    from .letta_async_request_input import LettaAsyncRequestInput
    from .letta_async_request_input_one_item import (
        LettaAsyncRequestInputOneItem,
        LettaAsyncRequestInputOneItem_Image,
        LettaAsyncRequestInputOneItem_OmittedReasoning,
        LettaAsyncRequestInputOneItem_Reasoning,
        LettaAsyncRequestInputOneItem_RedactedReasoning,
        LettaAsyncRequestInputOneItem_SummarizedReasoning,
        LettaAsyncRequestInputOneItem_Text,
        LettaAsyncRequestInputOneItem_ToolCall,
        LettaAsyncRequestInputOneItem_ToolReturn,
    )
    from .letta_async_request_messages_item import LettaAsyncRequestMessagesItem
    from .list_agent_sources_request_order import ListAgentSourcesRequestOrder
    from .list_agent_sources_request_order_by import ListAgentSourcesRequestOrderBy
    from .list_agents_request_include_item import ListAgentsRequestIncludeItem
    from .list_agents_request_order import ListAgentsRequestOrder
    from .list_agents_request_order_by import ListAgentsRequestOrderBy
    from .list_core_memory_blocks_request_order import ListCoreMemoryBlocksRequestOrder
    from .list_core_memory_blocks_request_order_by import ListCoreMemoryBlocksRequestOrderBy
    from .list_files_for_agent_request_order import ListFilesForAgentRequestOrder
    from .list_files_for_agent_request_order_by import ListFilesForAgentRequestOrderBy
    from .list_folders_for_agent_request_order import ListFoldersForAgentRequestOrder
    from .list_folders_for_agent_request_order_by import ListFoldersForAgentRequestOrderBy
    from .list_groups_for_agent_request_order import ListGroupsForAgentRequestOrder
    from .list_groups_for_agent_request_order_by import ListGroupsForAgentRequestOrderBy
    from .list_messages_request_order import ListMessagesRequestOrder
    from .list_messages_request_order_by import ListMessagesRequestOrderBy
    from .list_tools_for_agent_request_order import ListToolsForAgentRequestOrder
    from .list_tools_for_agent_request_order_by import ListToolsForAgentRequestOrderBy
    from .message_search_request_search_mode import MessageSearchRequestSearchMode
    from .modify_message_request_body import (
        ModifyMessageRequestBody,
        ModifyMessageRequestBody_AssistantMessage,
        ModifyMessageRequestBody_ReasoningMessage,
        ModifyMessageRequestBody_SystemMessage,
        ModifyMessageRequestBody_UserMessage,
    )
    from .modify_message_response import (
        ModifyMessageResponse,
        ModifyMessageResponse_ApprovalRequestMessage,
        ModifyMessageResponse_ApprovalResponseMessage,
        ModifyMessageResponse_AssistantMessage,
        ModifyMessageResponse_Event,
        ModifyMessageResponse_HiddenReasoningMessage,
        ModifyMessageResponse_ReasoningMessage,
        ModifyMessageResponse_Summary,
        ModifyMessageResponse_SystemMessage,
        ModifyMessageResponse_ToolCallMessage,
        ModifyMessageResponse_ToolReturnMessage,
        ModifyMessageResponse_UserMessage,
    )
    from .preview_model_request_request_body import PreviewModelRequestRequestBody
    from .retrieve_agent_request_include_item import RetrieveAgentRequestIncludeItem
    from .search_archival_memory_request_tag_match_mode import SearchArchivalMemoryRequestTagMatchMode
    from .update_agent_model_settings import (
        UpdateAgentModelSettings,
        UpdateAgentModelSettings_Anthropic,
        UpdateAgentModelSettings_Azure,
        UpdateAgentModelSettings_Bedrock,
        UpdateAgentModelSettings_ChatgptOauth,
        UpdateAgentModelSettings_Deepseek,
        UpdateAgentModelSettings_GoogleAi,
        UpdateAgentModelSettings_GoogleVertex,
        UpdateAgentModelSettings_Groq,
        UpdateAgentModelSettings_Openai,
        UpdateAgentModelSettings_Together,
        UpdateAgentModelSettings_Xai,
        UpdateAgentModelSettings_Zai,
    )
    from .update_agent_response_format import (
        UpdateAgentResponseFormat,
        UpdateAgentResponseFormat_JsonObject,
        UpdateAgentResponseFormat_JsonSchema,
        UpdateAgentResponseFormat_Text,
    )
    from .update_agent_tool_rules_item import (
        UpdateAgentToolRulesItem,
        UpdateAgentToolRulesItem_Conditional,
        UpdateAgentToolRulesItem_ConstrainChildTools,
        UpdateAgentToolRulesItem_ContinueLoop,
        UpdateAgentToolRulesItem_ExitLoop,
        UpdateAgentToolRulesItem_MaxCountPerStep,
        UpdateAgentToolRulesItem_ParentLastTool,
        UpdateAgentToolRulesItem_RequiredBeforeExit,
        UpdateAgentToolRulesItem_RequiresApproval,
        UpdateAgentToolRulesItem_RunFirst,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AgentsGetAgentVariablesResponse": ".agents_get_agent_variables_response",
    "AgentsSearchDeployedAgentsRequestCombinator": ".agents_search_deployed_agents_request_combinator",
    "AgentsSearchDeployedAgentsRequestSearchItem": ".agents_search_deployed_agents_request_search_item",
    "AgentsSearchDeployedAgentsRequestSearchItemAgentId": ".agents_search_deployed_agents_request_search_item_agent_id",
    "AgentsSearchDeployedAgentsRequestSearchItemAgentIdOperator": ".agents_search_deployed_agents_request_search_item_agent_id_operator",
    "AgentsSearchDeployedAgentsRequestSearchItemIdentity": ".agents_search_deployed_agents_request_search_item_identity",
    "AgentsSearchDeployedAgentsRequestSearchItemIdentityOperator": ".agents_search_deployed_agents_request_search_item_identity_operator",
    "AgentsSearchDeployedAgentsRequestSearchItemName": ".agents_search_deployed_agents_request_search_item_name",
    "AgentsSearchDeployedAgentsRequestSearchItemNameOperator": ".agents_search_deployed_agents_request_search_item_name_operator",
    "AgentsSearchDeployedAgentsRequestSearchItemTags": ".agents_search_deployed_agents_request_search_item_tags",
    "AgentsSearchDeployedAgentsRequestSearchItemTagsOperator": ".agents_search_deployed_agents_request_search_item_tags_operator",
    "AgentsSearchDeployedAgentsRequestSearchItemTemplateName": ".agents_search_deployed_agents_request_search_item_template_name",
    "AgentsSearchDeployedAgentsRequestSearchItemTemplateNameOperator": ".agents_search_deployed_agents_request_search_item_template_name_operator",
    "AgentsSearchDeployedAgentsRequestSearchItemVersion": ".agents_search_deployed_agents_request_search_item_version",
    "AgentsSearchDeployedAgentsRequestSearchItem_AgentId": ".agents_search_deployed_agents_request_search_item",
    "AgentsSearchDeployedAgentsRequestSearchItem_Identity": ".agents_search_deployed_agents_request_search_item",
    "AgentsSearchDeployedAgentsRequestSearchItem_Name": ".agents_search_deployed_agents_request_search_item",
    "AgentsSearchDeployedAgentsRequestSearchItem_Tags": ".agents_search_deployed_agents_request_search_item",
    "AgentsSearchDeployedAgentsRequestSearchItem_TemplateName": ".agents_search_deployed_agents_request_search_item",
    "AgentsSearchDeployedAgentsRequestSearchItem_Version": ".agents_search_deployed_agents_request_search_item",
    "AgentsSearchDeployedAgentsRequestSortBy": ".agents_search_deployed_agents_request_sort_by",
    "AgentsSearchDeployedAgentsResponse": ".agents_search_deployed_agents_response",
    "CreateAgentRequestModelSettings": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_Anthropic": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_Azure": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_Bedrock": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_ChatgptOauth": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_Deepseek": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_GoogleAi": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_GoogleVertex": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_Groq": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_Openai": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_Together": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_Xai": ".create_agent_request_model_settings",
    "CreateAgentRequestModelSettings_Zai": ".create_agent_request_model_settings",
    "CreateAgentRequestResponseFormat": ".create_agent_request_response_format",
    "CreateAgentRequestResponseFormat_JsonObject": ".create_agent_request_response_format",
    "CreateAgentRequestResponseFormat_JsonSchema": ".create_agent_request_response_format",
    "CreateAgentRequestResponseFormat_Text": ".create_agent_request_response_format",
    "CreateAgentRequestToolRulesItem": ".create_agent_request_tool_rules_item",
    "CreateAgentRequestToolRulesItem_Conditional": ".create_agent_request_tool_rules_item",
    "CreateAgentRequestToolRulesItem_ConstrainChildTools": ".create_agent_request_tool_rules_item",
    "CreateAgentRequestToolRulesItem_ContinueLoop": ".create_agent_request_tool_rules_item",
    "CreateAgentRequestToolRulesItem_ExitLoop": ".create_agent_request_tool_rules_item",
    "CreateAgentRequestToolRulesItem_MaxCountPerStep": ".create_agent_request_tool_rules_item",
    "CreateAgentRequestToolRulesItem_ParentLastTool": ".create_agent_request_tool_rules_item",
    "CreateAgentRequestToolRulesItem_RequiredBeforeExit": ".create_agent_request_tool_rules_item",
    "CreateAgentRequestToolRulesItem_RequiresApproval": ".create_agent_request_tool_rules_item",
    "CreateAgentRequestToolRulesItem_RunFirst": ".create_agent_request_tool_rules_item",
    "LettaAsyncRequestInput": ".letta_async_request_input",
    "LettaAsyncRequestInputOneItem": ".letta_async_request_input_one_item",
    "LettaAsyncRequestInputOneItem_Image": ".letta_async_request_input_one_item",
    "LettaAsyncRequestInputOneItem_OmittedReasoning": ".letta_async_request_input_one_item",
    "LettaAsyncRequestInputOneItem_Reasoning": ".letta_async_request_input_one_item",
    "LettaAsyncRequestInputOneItem_RedactedReasoning": ".letta_async_request_input_one_item",
    "LettaAsyncRequestInputOneItem_SummarizedReasoning": ".letta_async_request_input_one_item",
    "LettaAsyncRequestInputOneItem_Text": ".letta_async_request_input_one_item",
    "LettaAsyncRequestInputOneItem_ToolCall": ".letta_async_request_input_one_item",
    "LettaAsyncRequestInputOneItem_ToolReturn": ".letta_async_request_input_one_item",
    "LettaAsyncRequestMessagesItem": ".letta_async_request_messages_item",
    "ListAgentSourcesRequestOrder": ".list_agent_sources_request_order",
    "ListAgentSourcesRequestOrderBy": ".list_agent_sources_request_order_by",
    "ListAgentsRequestIncludeItem": ".list_agents_request_include_item",
    "ListAgentsRequestOrder": ".list_agents_request_order",
    "ListAgentsRequestOrderBy": ".list_agents_request_order_by",
    "ListCoreMemoryBlocksRequestOrder": ".list_core_memory_blocks_request_order",
    "ListCoreMemoryBlocksRequestOrderBy": ".list_core_memory_blocks_request_order_by",
    "ListFilesForAgentRequestOrder": ".list_files_for_agent_request_order",
    "ListFilesForAgentRequestOrderBy": ".list_files_for_agent_request_order_by",
    "ListFoldersForAgentRequestOrder": ".list_folders_for_agent_request_order",
    "ListFoldersForAgentRequestOrderBy": ".list_folders_for_agent_request_order_by",
    "ListGroupsForAgentRequestOrder": ".list_groups_for_agent_request_order",
    "ListGroupsForAgentRequestOrderBy": ".list_groups_for_agent_request_order_by",
    "ListMessagesRequestOrder": ".list_messages_request_order",
    "ListMessagesRequestOrderBy": ".list_messages_request_order_by",
    "ListToolsForAgentRequestOrder": ".list_tools_for_agent_request_order",
    "ListToolsForAgentRequestOrderBy": ".list_tools_for_agent_request_order_by",
    "MessageSearchRequestSearchMode": ".message_search_request_search_mode",
    "ModifyMessageRequestBody": ".modify_message_request_body",
    "ModifyMessageRequestBody_AssistantMessage": ".modify_message_request_body",
    "ModifyMessageRequestBody_ReasoningMessage": ".modify_message_request_body",
    "ModifyMessageRequestBody_SystemMessage": ".modify_message_request_body",
    "ModifyMessageRequestBody_UserMessage": ".modify_message_request_body",
    "ModifyMessageResponse": ".modify_message_response",
    "ModifyMessageResponse_ApprovalRequestMessage": ".modify_message_response",
    "ModifyMessageResponse_ApprovalResponseMessage": ".modify_message_response",
    "ModifyMessageResponse_AssistantMessage": ".modify_message_response",
    "ModifyMessageResponse_Event": ".modify_message_response",
    "ModifyMessageResponse_HiddenReasoningMessage": ".modify_message_response",
    "ModifyMessageResponse_ReasoningMessage": ".modify_message_response",
    "ModifyMessageResponse_Summary": ".modify_message_response",
    "ModifyMessageResponse_SystemMessage": ".modify_message_response",
    "ModifyMessageResponse_ToolCallMessage": ".modify_message_response",
    "ModifyMessageResponse_ToolReturnMessage": ".modify_message_response",
    "ModifyMessageResponse_UserMessage": ".modify_message_response",
    "PreviewModelRequestRequestBody": ".preview_model_request_request_body",
    "RetrieveAgentRequestIncludeItem": ".retrieve_agent_request_include_item",
    "SearchArchivalMemoryRequestTagMatchMode": ".search_archival_memory_request_tag_match_mode",
    "UpdateAgentModelSettings": ".update_agent_model_settings",
    "UpdateAgentModelSettings_Anthropic": ".update_agent_model_settings",
    "UpdateAgentModelSettings_Azure": ".update_agent_model_settings",
    "UpdateAgentModelSettings_Bedrock": ".update_agent_model_settings",
    "UpdateAgentModelSettings_ChatgptOauth": ".update_agent_model_settings",
    "UpdateAgentModelSettings_Deepseek": ".update_agent_model_settings",
    "UpdateAgentModelSettings_GoogleAi": ".update_agent_model_settings",
    "UpdateAgentModelSettings_GoogleVertex": ".update_agent_model_settings",
    "UpdateAgentModelSettings_Groq": ".update_agent_model_settings",
    "UpdateAgentModelSettings_Openai": ".update_agent_model_settings",
    "UpdateAgentModelSettings_Together": ".update_agent_model_settings",
    "UpdateAgentModelSettings_Xai": ".update_agent_model_settings",
    "UpdateAgentModelSettings_Zai": ".update_agent_model_settings",
    "UpdateAgentResponseFormat": ".update_agent_response_format",
    "UpdateAgentResponseFormat_JsonObject": ".update_agent_response_format",
    "UpdateAgentResponseFormat_JsonSchema": ".update_agent_response_format",
    "UpdateAgentResponseFormat_Text": ".update_agent_response_format",
    "UpdateAgentToolRulesItem": ".update_agent_tool_rules_item",
    "UpdateAgentToolRulesItem_Conditional": ".update_agent_tool_rules_item",
    "UpdateAgentToolRulesItem_ConstrainChildTools": ".update_agent_tool_rules_item",
    "UpdateAgentToolRulesItem_ContinueLoop": ".update_agent_tool_rules_item",
    "UpdateAgentToolRulesItem_ExitLoop": ".update_agent_tool_rules_item",
    "UpdateAgentToolRulesItem_MaxCountPerStep": ".update_agent_tool_rules_item",
    "UpdateAgentToolRulesItem_ParentLastTool": ".update_agent_tool_rules_item",
    "UpdateAgentToolRulesItem_RequiredBeforeExit": ".update_agent_tool_rules_item",
    "UpdateAgentToolRulesItem_RequiresApproval": ".update_agent_tool_rules_item",
    "UpdateAgentToolRulesItem_RunFirst": ".update_agent_tool_rules_item",
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
    "AgentsGetAgentVariablesResponse",
    "AgentsSearchDeployedAgentsRequestCombinator",
    "AgentsSearchDeployedAgentsRequestSearchItem",
    "AgentsSearchDeployedAgentsRequestSearchItemAgentId",
    "AgentsSearchDeployedAgentsRequestSearchItemAgentIdOperator",
    "AgentsSearchDeployedAgentsRequestSearchItemIdentity",
    "AgentsSearchDeployedAgentsRequestSearchItemIdentityOperator",
    "AgentsSearchDeployedAgentsRequestSearchItemName",
    "AgentsSearchDeployedAgentsRequestSearchItemNameOperator",
    "AgentsSearchDeployedAgentsRequestSearchItemTags",
    "AgentsSearchDeployedAgentsRequestSearchItemTagsOperator",
    "AgentsSearchDeployedAgentsRequestSearchItemTemplateName",
    "AgentsSearchDeployedAgentsRequestSearchItemTemplateNameOperator",
    "AgentsSearchDeployedAgentsRequestSearchItemVersion",
    "AgentsSearchDeployedAgentsRequestSearchItem_AgentId",
    "AgentsSearchDeployedAgentsRequestSearchItem_Identity",
    "AgentsSearchDeployedAgentsRequestSearchItem_Name",
    "AgentsSearchDeployedAgentsRequestSearchItem_Tags",
    "AgentsSearchDeployedAgentsRequestSearchItem_TemplateName",
    "AgentsSearchDeployedAgentsRequestSearchItem_Version",
    "AgentsSearchDeployedAgentsRequestSortBy",
    "AgentsSearchDeployedAgentsResponse",
    "CreateAgentRequestModelSettings",
    "CreateAgentRequestModelSettings_Anthropic",
    "CreateAgentRequestModelSettings_Azure",
    "CreateAgentRequestModelSettings_Bedrock",
    "CreateAgentRequestModelSettings_ChatgptOauth",
    "CreateAgentRequestModelSettings_Deepseek",
    "CreateAgentRequestModelSettings_GoogleAi",
    "CreateAgentRequestModelSettings_GoogleVertex",
    "CreateAgentRequestModelSettings_Groq",
    "CreateAgentRequestModelSettings_Openai",
    "CreateAgentRequestModelSettings_Together",
    "CreateAgentRequestModelSettings_Xai",
    "CreateAgentRequestModelSettings_Zai",
    "CreateAgentRequestResponseFormat",
    "CreateAgentRequestResponseFormat_JsonObject",
    "CreateAgentRequestResponseFormat_JsonSchema",
    "CreateAgentRequestResponseFormat_Text",
    "CreateAgentRequestToolRulesItem",
    "CreateAgentRequestToolRulesItem_Conditional",
    "CreateAgentRequestToolRulesItem_ConstrainChildTools",
    "CreateAgentRequestToolRulesItem_ContinueLoop",
    "CreateAgentRequestToolRulesItem_ExitLoop",
    "CreateAgentRequestToolRulesItem_MaxCountPerStep",
    "CreateAgentRequestToolRulesItem_ParentLastTool",
    "CreateAgentRequestToolRulesItem_RequiredBeforeExit",
    "CreateAgentRequestToolRulesItem_RequiresApproval",
    "CreateAgentRequestToolRulesItem_RunFirst",
    "LettaAsyncRequestInput",
    "LettaAsyncRequestInputOneItem",
    "LettaAsyncRequestInputOneItem_Image",
    "LettaAsyncRequestInputOneItem_OmittedReasoning",
    "LettaAsyncRequestInputOneItem_Reasoning",
    "LettaAsyncRequestInputOneItem_RedactedReasoning",
    "LettaAsyncRequestInputOneItem_SummarizedReasoning",
    "LettaAsyncRequestInputOneItem_Text",
    "LettaAsyncRequestInputOneItem_ToolCall",
    "LettaAsyncRequestInputOneItem_ToolReturn",
    "LettaAsyncRequestMessagesItem",
    "ListAgentSourcesRequestOrder",
    "ListAgentSourcesRequestOrderBy",
    "ListAgentsRequestIncludeItem",
    "ListAgentsRequestOrder",
    "ListAgentsRequestOrderBy",
    "ListCoreMemoryBlocksRequestOrder",
    "ListCoreMemoryBlocksRequestOrderBy",
    "ListFilesForAgentRequestOrder",
    "ListFilesForAgentRequestOrderBy",
    "ListFoldersForAgentRequestOrder",
    "ListFoldersForAgentRequestOrderBy",
    "ListGroupsForAgentRequestOrder",
    "ListGroupsForAgentRequestOrderBy",
    "ListMessagesRequestOrder",
    "ListMessagesRequestOrderBy",
    "ListToolsForAgentRequestOrder",
    "ListToolsForAgentRequestOrderBy",
    "MessageSearchRequestSearchMode",
    "ModifyMessageRequestBody",
    "ModifyMessageRequestBody_AssistantMessage",
    "ModifyMessageRequestBody_ReasoningMessage",
    "ModifyMessageRequestBody_SystemMessage",
    "ModifyMessageRequestBody_UserMessage",
    "ModifyMessageResponse",
    "ModifyMessageResponse_ApprovalRequestMessage",
    "ModifyMessageResponse_ApprovalResponseMessage",
    "ModifyMessageResponse_AssistantMessage",
    "ModifyMessageResponse_Event",
    "ModifyMessageResponse_HiddenReasoningMessage",
    "ModifyMessageResponse_ReasoningMessage",
    "ModifyMessageResponse_Summary",
    "ModifyMessageResponse_SystemMessage",
    "ModifyMessageResponse_ToolCallMessage",
    "ModifyMessageResponse_ToolReturnMessage",
    "ModifyMessageResponse_UserMessage",
    "PreviewModelRequestRequestBody",
    "RetrieveAgentRequestIncludeItem",
    "SearchArchivalMemoryRequestTagMatchMode",
    "UpdateAgentModelSettings",
    "UpdateAgentModelSettings_Anthropic",
    "UpdateAgentModelSettings_Azure",
    "UpdateAgentModelSettings_Bedrock",
    "UpdateAgentModelSettings_ChatgptOauth",
    "UpdateAgentModelSettings_Deepseek",
    "UpdateAgentModelSettings_GoogleAi",
    "UpdateAgentModelSettings_GoogleVertex",
    "UpdateAgentModelSettings_Groq",
    "UpdateAgentModelSettings_Openai",
    "UpdateAgentModelSettings_Together",
    "UpdateAgentModelSettings_Xai",
    "UpdateAgentModelSettings_Zai",
    "UpdateAgentResponseFormat",
    "UpdateAgentResponseFormat_JsonObject",
    "UpdateAgentResponseFormat_JsonSchema",
    "UpdateAgentResponseFormat_Text",
    "UpdateAgentToolRulesItem",
    "UpdateAgentToolRulesItem_Conditional",
    "UpdateAgentToolRulesItem_ConstrainChildTools",
    "UpdateAgentToolRulesItem_ContinueLoop",
    "UpdateAgentToolRulesItem_ExitLoop",
    "UpdateAgentToolRulesItem_MaxCountPerStep",
    "UpdateAgentToolRulesItem_ParentLastTool",
    "UpdateAgentToolRulesItem_RequiredBeforeExit",
    "UpdateAgentToolRulesItem_RequiresApproval",
    "UpdateAgentToolRulesItem_RunFirst",
]

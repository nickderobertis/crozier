



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .group_create_manager_config import (
        GroupCreateManagerConfig,
        GroupCreateManagerConfig_Dynamic,
        GroupCreateManagerConfig_RoundRobin,
        GroupCreateManagerConfig_Sleeptime,
        GroupCreateManagerConfig_Supervisor,
        GroupCreateManagerConfig_VoiceSleeptime,
    )
    from .group_update_manager_config import (
        GroupUpdateManagerConfig,
        GroupUpdateManagerConfig_Dynamic,
        GroupUpdateManagerConfig_RoundRobin,
        GroupUpdateManagerConfig_Sleeptime,
        GroupUpdateManagerConfig_Supervisor,
        GroupUpdateManagerConfig_VoiceSleeptime,
    )
    from .list_group_messages_request_order import ListGroupMessagesRequestOrder
    from .list_group_messages_request_order_by import ListGroupMessagesRequestOrderBy
    from .list_groups_request_order import ListGroupsRequestOrder
    from .list_groups_request_order_by import ListGroupsRequestOrderBy
    from .modify_group_message_request_body import (
        ModifyGroupMessageRequestBody,
        ModifyGroupMessageRequestBody_AssistantMessage,
        ModifyGroupMessageRequestBody_ReasoningMessage,
        ModifyGroupMessageRequestBody_SystemMessage,
        ModifyGroupMessageRequestBody_UserMessage,
    )
    from .modify_group_message_response import (
        ModifyGroupMessageResponse,
        ModifyGroupMessageResponse_ApprovalRequestMessage,
        ModifyGroupMessageResponse_ApprovalResponseMessage,
        ModifyGroupMessageResponse_AssistantMessage,
        ModifyGroupMessageResponse_Event,
        ModifyGroupMessageResponse_HiddenReasoningMessage,
        ModifyGroupMessageResponse_ReasoningMessage,
        ModifyGroupMessageResponse_Summary,
        ModifyGroupMessageResponse_SystemMessage,
        ModifyGroupMessageResponse_ToolCallMessage,
        ModifyGroupMessageResponse_ToolReturnMessage,
        ModifyGroupMessageResponse_UserMessage,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GroupCreateManagerConfig": ".group_create_manager_config",
    "GroupCreateManagerConfig_Dynamic": ".group_create_manager_config",
    "GroupCreateManagerConfig_RoundRobin": ".group_create_manager_config",
    "GroupCreateManagerConfig_Sleeptime": ".group_create_manager_config",
    "GroupCreateManagerConfig_Supervisor": ".group_create_manager_config",
    "GroupCreateManagerConfig_VoiceSleeptime": ".group_create_manager_config",
    "GroupUpdateManagerConfig": ".group_update_manager_config",
    "GroupUpdateManagerConfig_Dynamic": ".group_update_manager_config",
    "GroupUpdateManagerConfig_RoundRobin": ".group_update_manager_config",
    "GroupUpdateManagerConfig_Sleeptime": ".group_update_manager_config",
    "GroupUpdateManagerConfig_Supervisor": ".group_update_manager_config",
    "GroupUpdateManagerConfig_VoiceSleeptime": ".group_update_manager_config",
    "ListGroupMessagesRequestOrder": ".list_group_messages_request_order",
    "ListGroupMessagesRequestOrderBy": ".list_group_messages_request_order_by",
    "ListGroupsRequestOrder": ".list_groups_request_order",
    "ListGroupsRequestOrderBy": ".list_groups_request_order_by",
    "ModifyGroupMessageRequestBody": ".modify_group_message_request_body",
    "ModifyGroupMessageRequestBody_AssistantMessage": ".modify_group_message_request_body",
    "ModifyGroupMessageRequestBody_ReasoningMessage": ".modify_group_message_request_body",
    "ModifyGroupMessageRequestBody_SystemMessage": ".modify_group_message_request_body",
    "ModifyGroupMessageRequestBody_UserMessage": ".modify_group_message_request_body",
    "ModifyGroupMessageResponse": ".modify_group_message_response",
    "ModifyGroupMessageResponse_ApprovalRequestMessage": ".modify_group_message_response",
    "ModifyGroupMessageResponse_ApprovalResponseMessage": ".modify_group_message_response",
    "ModifyGroupMessageResponse_AssistantMessage": ".modify_group_message_response",
    "ModifyGroupMessageResponse_Event": ".modify_group_message_response",
    "ModifyGroupMessageResponse_HiddenReasoningMessage": ".modify_group_message_response",
    "ModifyGroupMessageResponse_ReasoningMessage": ".modify_group_message_response",
    "ModifyGroupMessageResponse_Summary": ".modify_group_message_response",
    "ModifyGroupMessageResponse_SystemMessage": ".modify_group_message_response",
    "ModifyGroupMessageResponse_ToolCallMessage": ".modify_group_message_response",
    "ModifyGroupMessageResponse_ToolReturnMessage": ".modify_group_message_response",
    "ModifyGroupMessageResponse_UserMessage": ".modify_group_message_response",
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
    "GroupCreateManagerConfig",
    "GroupCreateManagerConfig_Dynamic",
    "GroupCreateManagerConfig_RoundRobin",
    "GroupCreateManagerConfig_Sleeptime",
    "GroupCreateManagerConfig_Supervisor",
    "GroupCreateManagerConfig_VoiceSleeptime",
    "GroupUpdateManagerConfig",
    "GroupUpdateManagerConfig_Dynamic",
    "GroupUpdateManagerConfig_RoundRobin",
    "GroupUpdateManagerConfig_Sleeptime",
    "GroupUpdateManagerConfig_Supervisor",
    "GroupUpdateManagerConfig_VoiceSleeptime",
    "ListGroupMessagesRequestOrder",
    "ListGroupMessagesRequestOrderBy",
    "ListGroupsRequestOrder",
    "ListGroupsRequestOrderBy",
    "ModifyGroupMessageRequestBody",
    "ModifyGroupMessageRequestBody_AssistantMessage",
    "ModifyGroupMessageRequestBody_ReasoningMessage",
    "ModifyGroupMessageRequestBody_SystemMessage",
    "ModifyGroupMessageRequestBody_UserMessage",
    "ModifyGroupMessageResponse",
    "ModifyGroupMessageResponse_ApprovalRequestMessage",
    "ModifyGroupMessageResponse_ApprovalResponseMessage",
    "ModifyGroupMessageResponse_AssistantMessage",
    "ModifyGroupMessageResponse_Event",
    "ModifyGroupMessageResponse_HiddenReasoningMessage",
    "ModifyGroupMessageResponse_ReasoningMessage",
    "ModifyGroupMessageResponse_Summary",
    "ModifyGroupMessageResponse_SystemMessage",
    "ModifyGroupMessageResponse_ToolCallMessage",
    "ModifyGroupMessageResponse_ToolReturnMessage",
    "ModifyGroupMessageResponse_UserMessage",
]

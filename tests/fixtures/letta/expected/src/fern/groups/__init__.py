



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GroupCreateManagerConfig,
        GroupCreateManagerConfig_Dynamic,
        GroupCreateManagerConfig_RoundRobin,
        GroupCreateManagerConfig_Sleeptime,
        GroupCreateManagerConfig_Supervisor,
        GroupCreateManagerConfig_VoiceSleeptime,
        GroupUpdateManagerConfig,
        GroupUpdateManagerConfig_Dynamic,
        GroupUpdateManagerConfig_RoundRobin,
        GroupUpdateManagerConfig_Sleeptime,
        GroupUpdateManagerConfig_Supervisor,
        GroupUpdateManagerConfig_VoiceSleeptime,
        ListGroupMessagesRequestOrder,
        ListGroupMessagesRequestOrderBy,
        ListGroupsRequestOrder,
        ListGroupsRequestOrderBy,
        ModifyGroupMessageRequestBody,
        ModifyGroupMessageRequestBody_AssistantMessage,
        ModifyGroupMessageRequestBody_ReasoningMessage,
        ModifyGroupMessageRequestBody_SystemMessage,
        ModifyGroupMessageRequestBody_UserMessage,
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
    "GroupCreateManagerConfig": ".types",
    "GroupCreateManagerConfig_Dynamic": ".types",
    "GroupCreateManagerConfig_RoundRobin": ".types",
    "GroupCreateManagerConfig_Sleeptime": ".types",
    "GroupCreateManagerConfig_Supervisor": ".types",
    "GroupCreateManagerConfig_VoiceSleeptime": ".types",
    "GroupUpdateManagerConfig": ".types",
    "GroupUpdateManagerConfig_Dynamic": ".types",
    "GroupUpdateManagerConfig_RoundRobin": ".types",
    "GroupUpdateManagerConfig_Sleeptime": ".types",
    "GroupUpdateManagerConfig_Supervisor": ".types",
    "GroupUpdateManagerConfig_VoiceSleeptime": ".types",
    "ListGroupMessagesRequestOrder": ".types",
    "ListGroupMessagesRequestOrderBy": ".types",
    "ListGroupsRequestOrder": ".types",
    "ListGroupsRequestOrderBy": ".types",
    "ModifyGroupMessageRequestBody": ".types",
    "ModifyGroupMessageRequestBody_AssistantMessage": ".types",
    "ModifyGroupMessageRequestBody_ReasoningMessage": ".types",
    "ModifyGroupMessageRequestBody_SystemMessage": ".types",
    "ModifyGroupMessageRequestBody_UserMessage": ".types",
    "ModifyGroupMessageResponse": ".types",
    "ModifyGroupMessageResponse_ApprovalRequestMessage": ".types",
    "ModifyGroupMessageResponse_ApprovalResponseMessage": ".types",
    "ModifyGroupMessageResponse_AssistantMessage": ".types",
    "ModifyGroupMessageResponse_Event": ".types",
    "ModifyGroupMessageResponse_HiddenReasoningMessage": ".types",
    "ModifyGroupMessageResponse_ReasoningMessage": ".types",
    "ModifyGroupMessageResponse_Summary": ".types",
    "ModifyGroupMessageResponse_SystemMessage": ".types",
    "ModifyGroupMessageResponse_ToolCallMessage": ".types",
    "ModifyGroupMessageResponse_ToolReturnMessage": ".types",
    "ModifyGroupMessageResponse_UserMessage": ".types",
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

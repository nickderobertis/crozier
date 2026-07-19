



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_messages_for_step_request_order import ListMessagesForStepRequestOrder
    from .list_messages_for_step_request_order_by import ListMessagesForStepRequestOrderBy
    from .list_messages_for_step_response_item import (
        ListMessagesForStepResponseItem,
        ListMessagesForStepResponseItem_ApprovalRequestMessage,
        ListMessagesForStepResponseItem_ApprovalResponseMessage,
        ListMessagesForStepResponseItem_AssistantMessage,
        ListMessagesForStepResponseItem_Event,
        ListMessagesForStepResponseItem_HiddenReasoningMessage,
        ListMessagesForStepResponseItem_ReasoningMessage,
        ListMessagesForStepResponseItem_Summary,
        ListMessagesForStepResponseItem_SystemMessage,
        ListMessagesForStepResponseItem_ToolCallMessage,
        ListMessagesForStepResponseItem_ToolReturnMessage,
        ListMessagesForStepResponseItem_UserMessage,
    )
    from .list_steps_request_feedback import ListStepsRequestFeedback
    from .list_steps_request_order import ListStepsRequestOrder
    from .list_steps_request_order_by import ListStepsRequestOrderBy
_dynamic_imports: typing.Dict[str, str] = {
    "ListMessagesForStepRequestOrder": ".list_messages_for_step_request_order",
    "ListMessagesForStepRequestOrderBy": ".list_messages_for_step_request_order_by",
    "ListMessagesForStepResponseItem": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_ApprovalRequestMessage": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_ApprovalResponseMessage": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_AssistantMessage": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_Event": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_HiddenReasoningMessage": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_ReasoningMessage": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_Summary": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_SystemMessage": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_ToolCallMessage": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_ToolReturnMessage": ".list_messages_for_step_response_item",
    "ListMessagesForStepResponseItem_UserMessage": ".list_messages_for_step_response_item",
    "ListStepsRequestFeedback": ".list_steps_request_feedback",
    "ListStepsRequestOrder": ".list_steps_request_order",
    "ListStepsRequestOrderBy": ".list_steps_request_order_by",
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
    "ListMessagesForStepRequestOrder",
    "ListMessagesForStepRequestOrderBy",
    "ListMessagesForStepResponseItem",
    "ListMessagesForStepResponseItem_ApprovalRequestMessage",
    "ListMessagesForStepResponseItem_ApprovalResponseMessage",
    "ListMessagesForStepResponseItem_AssistantMessage",
    "ListMessagesForStepResponseItem_Event",
    "ListMessagesForStepResponseItem_HiddenReasoningMessage",
    "ListMessagesForStepResponseItem_ReasoningMessage",
    "ListMessagesForStepResponseItem_Summary",
    "ListMessagesForStepResponseItem_SystemMessage",
    "ListMessagesForStepResponseItem_ToolCallMessage",
    "ListMessagesForStepResponseItem_ToolReturnMessage",
    "ListMessagesForStepResponseItem_UserMessage",
    "ListStepsRequestFeedback",
    "ListStepsRequestOrder",
    "ListStepsRequestOrderBy",
]

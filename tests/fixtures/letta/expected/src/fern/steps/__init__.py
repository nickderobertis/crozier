



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ListMessagesForStepRequestOrder,
        ListMessagesForStepRequestOrderBy,
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
        ListStepsRequestFeedback,
        ListStepsRequestOrder,
        ListStepsRequestOrderBy,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ListMessagesForStepRequestOrder": ".types",
    "ListMessagesForStepRequestOrderBy": ".types",
    "ListMessagesForStepResponseItem": ".types",
    "ListMessagesForStepResponseItem_ApprovalRequestMessage": ".types",
    "ListMessagesForStepResponseItem_ApprovalResponseMessage": ".types",
    "ListMessagesForStepResponseItem_AssistantMessage": ".types",
    "ListMessagesForStepResponseItem_Event": ".types",
    "ListMessagesForStepResponseItem_HiddenReasoningMessage": ".types",
    "ListMessagesForStepResponseItem_ReasoningMessage": ".types",
    "ListMessagesForStepResponseItem_Summary": ".types",
    "ListMessagesForStepResponseItem_SystemMessage": ".types",
    "ListMessagesForStepResponseItem_ToolCallMessage": ".types",
    "ListMessagesForStepResponseItem_ToolReturnMessage": ".types",
    "ListMessagesForStepResponseItem_UserMessage": ".types",
    "ListStepsRequestFeedback": ".types",
    "ListStepsRequestOrder": ".types",
    "ListStepsRequestOrderBy": ".types",
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

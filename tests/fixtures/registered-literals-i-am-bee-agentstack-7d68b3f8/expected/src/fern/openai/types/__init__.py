



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .chat_completion_request_function_call import ChatCompletionRequestFunctionCall
    from .chat_completion_request_function_call_zero import ChatCompletionRequestFunctionCallZero
    from .chat_completion_request_messages_item import (
        ChatCompletionRequestMessagesItem,
        ChatCompletionRequestMessagesItem_Assistant,
        ChatCompletionRequestMessagesItem_Developer,
        ChatCompletionRequestMessagesItem_Function,
        ChatCompletionRequestMessagesItem_System,
        ChatCompletionRequestMessagesItem_Tool,
        ChatCompletionRequestMessagesItem_User,
    )
    from .chat_completion_request_modalities_item import ChatCompletionRequestModalitiesItem
    from .chat_completion_request_model import ChatCompletionRequestModel
    from .chat_completion_request_model_one import ChatCompletionRequestModelOne
    from .chat_completion_request_reasoning_effort import ChatCompletionRequestReasoningEffort
    from .chat_completion_request_response_format import ChatCompletionRequestResponseFormat
    from .chat_completion_request_service_tier import ChatCompletionRequestServiceTier
    from .chat_completion_request_stop import ChatCompletionRequestStop
    from .chat_completion_request_tool_choice import ChatCompletionRequestToolChoice
    from .chat_completion_request_tool_choice_zero import ChatCompletionRequestToolChoiceZero
    from .embeddings_request_encoding_format import EmbeddingsRequestEncodingFormat
    from .embeddings_request_input import EmbeddingsRequestInput
_dynamic_imports: typing.Dict[str, str] = {
    "ChatCompletionRequestFunctionCall": ".chat_completion_request_function_call",
    "ChatCompletionRequestFunctionCallZero": ".chat_completion_request_function_call_zero",
    "ChatCompletionRequestMessagesItem": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_Assistant": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_Developer": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_Function": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_System": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_Tool": ".chat_completion_request_messages_item",
    "ChatCompletionRequestMessagesItem_User": ".chat_completion_request_messages_item",
    "ChatCompletionRequestModalitiesItem": ".chat_completion_request_modalities_item",
    "ChatCompletionRequestModel": ".chat_completion_request_model",
    "ChatCompletionRequestModelOne": ".chat_completion_request_model_one",
    "ChatCompletionRequestReasoningEffort": ".chat_completion_request_reasoning_effort",
    "ChatCompletionRequestResponseFormat": ".chat_completion_request_response_format",
    "ChatCompletionRequestServiceTier": ".chat_completion_request_service_tier",
    "ChatCompletionRequestStop": ".chat_completion_request_stop",
    "ChatCompletionRequestToolChoice": ".chat_completion_request_tool_choice",
    "ChatCompletionRequestToolChoiceZero": ".chat_completion_request_tool_choice_zero",
    "EmbeddingsRequestEncodingFormat": ".embeddings_request_encoding_format",
    "EmbeddingsRequestInput": ".embeddings_request_input",
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
    "ChatCompletionRequestFunctionCall",
    "ChatCompletionRequestFunctionCallZero",
    "ChatCompletionRequestMessagesItem",
    "ChatCompletionRequestMessagesItem_Assistant",
    "ChatCompletionRequestMessagesItem_Developer",
    "ChatCompletionRequestMessagesItem_Function",
    "ChatCompletionRequestMessagesItem_System",
    "ChatCompletionRequestMessagesItem_Tool",
    "ChatCompletionRequestMessagesItem_User",
    "ChatCompletionRequestModalitiesItem",
    "ChatCompletionRequestModel",
    "ChatCompletionRequestModelOne",
    "ChatCompletionRequestReasoningEffort",
    "ChatCompletionRequestResponseFormat",
    "ChatCompletionRequestServiceTier",
    "ChatCompletionRequestStop",
    "ChatCompletionRequestToolChoice",
    "ChatCompletionRequestToolChoiceZero",
    "EmbeddingsRequestEncodingFormat",
    "EmbeddingsRequestInput",
]

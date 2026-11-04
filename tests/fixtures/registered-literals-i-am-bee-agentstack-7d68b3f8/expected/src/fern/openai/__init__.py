



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ChatCompletionRequestFunctionCall,
        ChatCompletionRequestFunctionCallZero,
        ChatCompletionRequestMessagesItem,
        ChatCompletionRequestMessagesItem_Assistant,
        ChatCompletionRequestMessagesItem_Developer,
        ChatCompletionRequestMessagesItem_Function,
        ChatCompletionRequestMessagesItem_System,
        ChatCompletionRequestMessagesItem_Tool,
        ChatCompletionRequestMessagesItem_User,
        ChatCompletionRequestModalitiesItem,
        ChatCompletionRequestModel,
        ChatCompletionRequestModelOne,
        ChatCompletionRequestReasoningEffort,
        ChatCompletionRequestResponseFormat,
        ChatCompletionRequestServiceTier,
        ChatCompletionRequestStop,
        ChatCompletionRequestToolChoice,
        ChatCompletionRequestToolChoiceZero,
        EmbeddingsRequestEncodingFormat,
        EmbeddingsRequestInput,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ChatCompletionRequestFunctionCall": ".types",
    "ChatCompletionRequestFunctionCallZero": ".types",
    "ChatCompletionRequestMessagesItem": ".types",
    "ChatCompletionRequestMessagesItem_Assistant": ".types",
    "ChatCompletionRequestMessagesItem_Developer": ".types",
    "ChatCompletionRequestMessagesItem_Function": ".types",
    "ChatCompletionRequestMessagesItem_System": ".types",
    "ChatCompletionRequestMessagesItem_Tool": ".types",
    "ChatCompletionRequestMessagesItem_User": ".types",
    "ChatCompletionRequestModalitiesItem": ".types",
    "ChatCompletionRequestModel": ".types",
    "ChatCompletionRequestModelOne": ".types",
    "ChatCompletionRequestReasoningEffort": ".types",
    "ChatCompletionRequestResponseFormat": ".types",
    "ChatCompletionRequestServiceTier": ".types",
    "ChatCompletionRequestStop": ".types",
    "ChatCompletionRequestToolChoice": ".types",
    "ChatCompletionRequestToolChoiceZero": ".types",
    "EmbeddingsRequestEncodingFormat": ".types",
    "EmbeddingsRequestInput": ".types",
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

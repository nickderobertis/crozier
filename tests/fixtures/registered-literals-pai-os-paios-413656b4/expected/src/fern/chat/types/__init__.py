



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_chat_completion_request_function_call import CreateChatCompletionRequestFunctionCall
    from .create_chat_completion_request_function_call_zero import CreateChatCompletionRequestFunctionCallZero
    from .create_chat_completion_request_model import CreateChatCompletionRequestModel
    from .create_chat_completion_request_model_one import CreateChatCompletionRequestModelOne
    from .create_chat_completion_request_response_format import CreateChatCompletionRequestResponseFormat
    from .create_chat_completion_request_response_format_type import CreateChatCompletionRequestResponseFormatType
    from .create_chat_completion_request_stop import CreateChatCompletionRequestStop
_dynamic_imports: typing.Dict[str, str] = {
    "CreateChatCompletionRequestFunctionCall": ".create_chat_completion_request_function_call",
    "CreateChatCompletionRequestFunctionCallZero": ".create_chat_completion_request_function_call_zero",
    "CreateChatCompletionRequestModel": ".create_chat_completion_request_model",
    "CreateChatCompletionRequestModelOne": ".create_chat_completion_request_model_one",
    "CreateChatCompletionRequestResponseFormat": ".create_chat_completion_request_response_format",
    "CreateChatCompletionRequestResponseFormatType": ".create_chat_completion_request_response_format_type",
    "CreateChatCompletionRequestStop": ".create_chat_completion_request_stop",
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
    "CreateChatCompletionRequestFunctionCall",
    "CreateChatCompletionRequestFunctionCallZero",
    "CreateChatCompletionRequestModel",
    "CreateChatCompletionRequestModelOne",
    "CreateChatCompletionRequestResponseFormat",
    "CreateChatCompletionRequestResponseFormatType",
    "CreateChatCompletionRequestStop",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .chat_message import ChatMessage
    from .chat_message_role import ChatMessageRole
    from .chat_request_format import ChatRequestFormat
    from .chat_request_format_zero import ChatRequestFormatZero
    from .chat_request_keep_alive import ChatRequestKeepAlive
    from .chat_response import ChatResponse
    from .chat_response_message import ChatResponseMessage
    from .chat_response_message_role import ChatResponseMessageRole
    from .chat_stream_event import ChatStreamEvent
    from .chat_stream_event_message import ChatStreamEventMessage
    from .create_request_license import CreateRequestLicense
    from .embed_request_input import EmbedRequestInput
    from .embed_response import EmbedResponse
    from .error_response import ErrorResponse
    from .generate_request_format import GenerateRequestFormat
    from .generate_request_keep_alive import GenerateRequestKeepAlive
    from .generate_response import GenerateResponse
    from .generate_stream_event import GenerateStreamEvent
    from .list_response import ListResponse
    from .logprob import Logprob
    from .model_options import ModelOptions
    from .model_options_stop import ModelOptionsStop
    from .model_summary import ModelSummary
    from .model_summary_details import ModelSummaryDetails
    from .ps import Ps
    from .ps_response import PsResponse
    from .show_response import ShowResponse
    from .status_event import StatusEvent
    from .status_response import StatusResponse
    from .think_value import ThinkValue
    from .thinking import Thinking
    from .thinking_default import ThinkingDefault
    from .thinking_values_item import ThinkingValuesItem
    from .token_logprob import TokenLogprob
    from .tool_call import ToolCall
    from .tool_call_function import ToolCallFunction
    from .tool_definition import ToolDefinition
    from .tool_definition_function import ToolDefinitionFunction
    from .tool_definition_type import ToolDefinitionType
    from .version_response import VersionResponse
    from .web_fetch_request import WebFetchRequest
    from .web_fetch_response import WebFetchResponse
    from .web_search_request import WebSearchRequest
    from .web_search_response import WebSearchResponse
    from .web_search_result import WebSearchResult
_dynamic_imports: typing.Dict[str, str] = {
    "ChatMessage": ".chat_message",
    "ChatMessageRole": ".chat_message_role",
    "ChatRequestFormat": ".chat_request_format",
    "ChatRequestFormatZero": ".chat_request_format_zero",
    "ChatRequestKeepAlive": ".chat_request_keep_alive",
    "ChatResponse": ".chat_response",
    "ChatResponseMessage": ".chat_response_message",
    "ChatResponseMessageRole": ".chat_response_message_role",
    "ChatStreamEvent": ".chat_stream_event",
    "ChatStreamEventMessage": ".chat_stream_event_message",
    "CreateRequestLicense": ".create_request_license",
    "EmbedRequestInput": ".embed_request_input",
    "EmbedResponse": ".embed_response",
    "ErrorResponse": ".error_response",
    "GenerateRequestFormat": ".generate_request_format",
    "GenerateRequestKeepAlive": ".generate_request_keep_alive",
    "GenerateResponse": ".generate_response",
    "GenerateStreamEvent": ".generate_stream_event",
    "ListResponse": ".list_response",
    "Logprob": ".logprob",
    "ModelOptions": ".model_options",
    "ModelOptionsStop": ".model_options_stop",
    "ModelSummary": ".model_summary",
    "ModelSummaryDetails": ".model_summary_details",
    "Ps": ".ps",
    "PsResponse": ".ps_response",
    "ShowResponse": ".show_response",
    "StatusEvent": ".status_event",
    "StatusResponse": ".status_response",
    "ThinkValue": ".think_value",
    "Thinking": ".thinking",
    "ThinkingDefault": ".thinking_default",
    "ThinkingValuesItem": ".thinking_values_item",
    "TokenLogprob": ".token_logprob",
    "ToolCall": ".tool_call",
    "ToolCallFunction": ".tool_call_function",
    "ToolDefinition": ".tool_definition",
    "ToolDefinitionFunction": ".tool_definition_function",
    "ToolDefinitionType": ".tool_definition_type",
    "VersionResponse": ".version_response",
    "WebFetchRequest": ".web_fetch_request",
    "WebFetchResponse": ".web_fetch_response",
    "WebSearchRequest": ".web_search_request",
    "WebSearchResponse": ".web_search_response",
    "WebSearchResult": ".web_search_result",
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
    "ChatMessage",
    "ChatMessageRole",
    "ChatRequestFormat",
    "ChatRequestFormatZero",
    "ChatRequestKeepAlive",
    "ChatResponse",
    "ChatResponseMessage",
    "ChatResponseMessageRole",
    "ChatStreamEvent",
    "ChatStreamEventMessage",
    "CreateRequestLicense",
    "EmbedRequestInput",
    "EmbedResponse",
    "ErrorResponse",
    "GenerateRequestFormat",
    "GenerateRequestKeepAlive",
    "GenerateResponse",
    "GenerateStreamEvent",
    "ListResponse",
    "Logprob",
    "ModelOptions",
    "ModelOptionsStop",
    "ModelSummary",
    "ModelSummaryDetails",
    "Ps",
    "PsResponse",
    "ShowResponse",
    "StatusEvent",
    "StatusResponse",
    "ThinkValue",
    "Thinking",
    "ThinkingDefault",
    "ThinkingValuesItem",
    "TokenLogprob",
    "ToolCall",
    "ToolCallFunction",
    "ToolDefinition",
    "ToolDefinitionFunction",
    "ToolDefinitionType",
    "VersionResponse",
    "WebFetchRequest",
    "WebFetchResponse",
    "WebSearchRequest",
    "WebSearchResponse",
    "WebSearchResult",
]

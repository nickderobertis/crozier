



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ChatMessage,
        ChatMessageRole,
        ChatRequestFormat,
        ChatRequestFormatZero,
        ChatRequestKeepAlive,
        ChatResponse,
        ChatResponseMessage,
        ChatResponseMessageRole,
        ChatStreamEvent,
        ChatStreamEventMessage,
        CreateRequestLicense,
        EmbedRequestInput,
        EmbedResponse,
        ErrorResponse,
        GenerateRequestFormat,
        GenerateRequestKeepAlive,
        GenerateResponse,
        GenerateStreamEvent,
        ListResponse,
        Logprob,
        ModelOptions,
        ModelOptionsStop,
        ModelSummary,
        ModelSummaryDetails,
        Ps,
        PsResponse,
        ShowResponse,
        StatusEvent,
        StatusResponse,
        ThinkValue,
        Thinking,
        ThinkingDefault,
        ThinkingValuesItem,
        TokenLogprob,
        ToolCall,
        ToolCallFunction,
        ToolDefinition,
        ToolDefinitionFunction,
        ToolDefinitionType,
        VersionResponse,
        WebFetchRequest,
        WebFetchResponse,
        WebSearchRequest,
        WebSearchResponse,
        WebSearchResult,
    )
    from .errors import BadRequestError, InternalServerError, NotFoundError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ChatMessage": ".types",
    "ChatMessageRole": ".types",
    "ChatRequestFormat": ".types",
    "ChatRequestFormatZero": ".types",
    "ChatRequestKeepAlive": ".types",
    "ChatResponse": ".types",
    "ChatResponseMessage": ".types",
    "ChatResponseMessageRole": ".types",
    "ChatStreamEvent": ".types",
    "ChatStreamEventMessage": ".types",
    "CreateRequestLicense": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "EmbedRequestInput": ".types",
    "EmbedResponse": ".types",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GenerateRequestFormat": ".types",
    "GenerateRequestKeepAlive": ".types",
    "GenerateResponse": ".types",
    "GenerateStreamEvent": ".types",
    "InternalServerError": ".errors",
    "ListResponse": ".types",
    "Logprob": ".types",
    "ModelOptions": ".types",
    "ModelOptionsStop": ".types",
    "ModelSummary": ".types",
    "ModelSummaryDetails": ".types",
    "NotFoundError": ".errors",
    "Ps": ".types",
    "PsResponse": ".types",
    "ShowResponse": ".types",
    "StatusEvent": ".types",
    "StatusResponse": ".types",
    "ThinkValue": ".types",
    "Thinking": ".types",
    "ThinkingDefault": ".types",
    "ThinkingValuesItem": ".types",
    "TokenLogprob": ".types",
    "ToolCall": ".types",
    "ToolCallFunction": ".types",
    "ToolDefinition": ".types",
    "ToolDefinitionFunction": ".types",
    "ToolDefinitionType": ".types",
    "VersionResponse": ".types",
    "WebFetchRequest": ".types",
    "WebFetchResponse": ".types",
    "WebSearchRequest": ".types",
    "WebSearchResponse": ".types",
    "WebSearchResult": ".types",
    "__version__": ".version",
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
    "AsyncFernApi",
    "BadRequestError",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "EmbedRequestInput",
    "EmbedResponse",
    "ErrorResponse",
    "FernApi",
    "FernApiEnvironment",
    "GenerateRequestFormat",
    "GenerateRequestKeepAlive",
    "GenerateResponse",
    "GenerateStreamEvent",
    "InternalServerError",
    "ListResponse",
    "Logprob",
    "ModelOptions",
    "ModelOptionsStop",
    "ModelSummary",
    "ModelSummaryDetails",
    "NotFoundError",
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
    "__version__",
]

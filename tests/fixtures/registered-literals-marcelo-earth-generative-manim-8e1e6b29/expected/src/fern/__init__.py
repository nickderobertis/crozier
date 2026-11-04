



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ChatGenerationRequestEngine,
        ChatMessage,
        ChatMessageContent,
        ChatMessageContentOneItem,
        ChatMessageRole,
        CodeGenerationRequestEngine,
        CodeGenerationResponse,
        ErrorResponse,
        HealthResponse,
        HealthResponseProvidersValue,
        HealthResponseStatus,
        ModelsResponse,
        ModelsResponseEnginesItem,
        ModelsResponseEnginesItemEngine,
        ModelsResponseEnginesItemModelsItem,
        RenderComplete,
        RenderError,
        RenderProgress,
        VideoGenerationRequestAspectRatio,
        VideoGenerationRequestEngine,
        VideoRenderingRequestAspectRatio,
        VideoRenderingResponse,
    )
    from .errors import BadRequestError, InternalServerError, RequestTimeoutError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ChatGenerationRequestEngine": ".types",
    "ChatMessage": ".types",
    "ChatMessageContent": ".types",
    "ChatMessageContentOneItem": ".types",
    "ChatMessageRole": ".types",
    "CodeGenerationRequestEngine": ".types",
    "CodeGenerationResponse": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "HealthResponse": ".types",
    "HealthResponseProvidersValue": ".types",
    "HealthResponseStatus": ".types",
    "InternalServerError": ".errors",
    "ModelsResponse": ".types",
    "ModelsResponseEnginesItem": ".types",
    "ModelsResponseEnginesItemEngine": ".types",
    "ModelsResponseEnginesItemModelsItem": ".types",
    "RenderComplete": ".types",
    "RenderError": ".types",
    "RenderProgress": ".types",
    "RequestTimeoutError": ".errors",
    "VideoGenerationRequestAspectRatio": ".types",
    "VideoGenerationRequestEngine": ".types",
    "VideoRenderingRequestAspectRatio": ".types",
    "VideoRenderingResponse": ".types",
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
    "ChatGenerationRequestEngine",
    "ChatMessage",
    "ChatMessageContent",
    "ChatMessageContentOneItem",
    "ChatMessageRole",
    "CodeGenerationRequestEngine",
    "CodeGenerationResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "FernApi",
    "FernApiEnvironment",
    "HealthResponse",
    "HealthResponseProvidersValue",
    "HealthResponseStatus",
    "InternalServerError",
    "ModelsResponse",
    "ModelsResponseEnginesItem",
    "ModelsResponseEnginesItemEngine",
    "ModelsResponseEnginesItemModelsItem",
    "RenderComplete",
    "RenderError",
    "RenderProgress",
    "RequestTimeoutError",
    "VideoGenerationRequestAspectRatio",
    "VideoGenerationRequestEngine",
    "VideoRenderingRequestAspectRatio",
    "VideoRenderingResponse",
    "__version__",
]

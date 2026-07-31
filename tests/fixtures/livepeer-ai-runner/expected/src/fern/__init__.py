



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ApiError,
        AudioResponse,
        Chunk,
        GpuComputeInfo,
        GpuUtilizationInfo,
        HardwareInformation,
        HardwareStats,
        HealthCheck,
        HealthCheckStatus,
        HttpError,
        HttpValidationError,
        ImageResponse,
        ImageToTextResponse,
        LiveVideoToVideoResponse,
        LlmChoice,
        LlmMessage,
        LlmResponse,
        LlmTokenUsage,
        MasksResponse,
        Media,
        MediaUrl,
        TextResponse,
        ValidationError,
        ValidationErrorLocItem,
        VideoResponse,
    )
    from .errors import (
        BadRequestError,
        ContentTooLargeError,
        InternalServerError,
        UnauthorizedError,
        UnprocessableEntityError,
        UnsupportedMediaTypeError,
    )
    from . import generate
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ApiError": ".types",
    "AsyncFernApi": ".client",
    "AudioResponse": ".types",
    "BadRequestError": ".errors",
    "Chunk": ".types",
    "ContentTooLargeError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GpuComputeInfo": ".types",
    "GpuUtilizationInfo": ".types",
    "HardwareInformation": ".types",
    "HardwareStats": ".types",
    "HealthCheck": ".types",
    "HealthCheckStatus": ".types",
    "HttpError": ".types",
    "HttpValidationError": ".types",
    "ImageResponse": ".types",
    "ImageToTextResponse": ".types",
    "InternalServerError": ".errors",
    "LiveVideoToVideoResponse": ".types",
    "LlmChoice": ".types",
    "LlmMessage": ".types",
    "LlmResponse": ".types",
    "LlmTokenUsage": ".types",
    "MasksResponse": ".types",
    "Media": ".types",
    "MediaUrl": ".types",
    "TextResponse": ".types",
    "UnauthorizedError": ".errors",
    "UnprocessableEntityError": ".errors",
    "UnsupportedMediaTypeError": ".errors",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "VideoResponse": ".types",
    "__version__": ".version",
    "generate": ".generate",
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
    "ApiError",
    "AsyncFernApi",
    "AudioResponse",
    "BadRequestError",
    "Chunk",
    "ContentTooLargeError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GpuComputeInfo",
    "GpuUtilizationInfo",
    "HardwareInformation",
    "HardwareStats",
    "HealthCheck",
    "HealthCheckStatus",
    "HttpError",
    "HttpValidationError",
    "ImageResponse",
    "ImageToTextResponse",
    "InternalServerError",
    "LiveVideoToVideoResponse",
    "LlmChoice",
    "LlmMessage",
    "LlmResponse",
    "LlmTokenUsage",
    "MasksResponse",
    "Media",
    "MediaUrl",
    "TextResponse",
    "UnauthorizedError",
    "UnprocessableEntityError",
    "UnsupportedMediaTypeError",
    "ValidationError",
    "ValidationErrorLocItem",
    "VideoResponse",
    "__version__",
    "generate",
]

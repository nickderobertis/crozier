



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ChatBody,
        Chunk,
        ChunkObject,
        ChunksResponse,
        ChunksResponseModel,
        ChunksResponseObject,
        CompletionsBody,
        ContextFilter,
        Embedding,
        EmbeddingObject,
        EmbeddingsResponse,
        EmbeddingsResponseModel,
        EmbeddingsResponseObject,
        HealthResponse,
        HealthResponseStatus,
        HttpValidationError,
        IngestResponse,
        IngestResponseModel,
        IngestResponseObject,
        IngestedDoc,
        IngestedDocObject,
        OpenAiChoice,
        OpenAiCompletion,
        OpenAiCompletionModel,
        OpenAiCompletionObject,
        OpenAiDelta,
        OpenAiMessage,
        OpenAiMessageRole,
        SummarizeResponse,
        ValidationError,
        ValidationErrorLocItem,
    )
    from .errors import UnprocessableEntityError
    from . import context_chunks, contextual_completions, embeddings, health, ingestion, recipes
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .embeddings import EmbeddingsBodyInput
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "ChatBody": ".types",
    "Chunk": ".types",
    "ChunkObject": ".types",
    "ChunksResponse": ".types",
    "ChunksResponseModel": ".types",
    "ChunksResponseObject": ".types",
    "CompletionsBody": ".types",
    "ContextFilter": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Embedding": ".types",
    "EmbeddingObject": ".types",
    "EmbeddingsBodyInput": ".embeddings",
    "EmbeddingsResponse": ".types",
    "EmbeddingsResponseModel": ".types",
    "EmbeddingsResponseObject": ".types",
    "FernApi": ".client",
    "HealthResponse": ".types",
    "HealthResponseStatus": ".types",
    "HttpValidationError": ".types",
    "IngestResponse": ".types",
    "IngestResponseModel": ".types",
    "IngestResponseObject": ".types",
    "IngestedDoc": ".types",
    "IngestedDocObject": ".types",
    "OpenAiChoice": ".types",
    "OpenAiCompletion": ".types",
    "OpenAiCompletionModel": ".types",
    "OpenAiCompletionObject": ".types",
    "OpenAiDelta": ".types",
    "OpenAiMessage": ".types",
    "OpenAiMessageRole": ".types",
    "SummarizeResponse": ".types",
    "UnprocessableEntityError": ".errors",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "__version__": ".version",
    "context_chunks": ".context_chunks",
    "contextual_completions": ".contextual_completions",
    "embeddings": ".embeddings",
    "health": ".health",
    "ingestion": ".ingestion",
    "recipes": ".recipes",
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
    "ChatBody",
    "Chunk",
    "ChunkObject",
    "ChunksResponse",
    "ChunksResponseModel",
    "ChunksResponseObject",
    "CompletionsBody",
    "ContextFilter",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Embedding",
    "EmbeddingObject",
    "EmbeddingsBodyInput",
    "EmbeddingsResponse",
    "EmbeddingsResponseModel",
    "EmbeddingsResponseObject",
    "FernApi",
    "HealthResponse",
    "HealthResponseStatus",
    "HttpValidationError",
    "IngestResponse",
    "IngestResponseModel",
    "IngestResponseObject",
    "IngestedDoc",
    "IngestedDocObject",
    "OpenAiChoice",
    "OpenAiCompletion",
    "OpenAiCompletionModel",
    "OpenAiCompletionObject",
    "OpenAiDelta",
    "OpenAiMessage",
    "OpenAiMessageRole",
    "SummarizeResponse",
    "UnprocessableEntityError",
    "ValidationError",
    "ValidationErrorLocItem",
    "__version__",
    "context_chunks",
    "contextual_completions",
    "embeddings",
    "health",
    "ingestion",
    "recipes",
]

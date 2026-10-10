



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .chat_body import ChatBody
    from .chunk import Chunk
    from .chunk_object import ChunkObject
    from .chunks_response import ChunksResponse
    from .chunks_response_model import ChunksResponseModel
    from .chunks_response_object import ChunksResponseObject
    from .completions_body import CompletionsBody
    from .context_filter import ContextFilter
    from .embedding import Embedding
    from .embedding_object import EmbeddingObject
    from .embeddings_response import EmbeddingsResponse
    from .embeddings_response_model import EmbeddingsResponseModel
    from .embeddings_response_object import EmbeddingsResponseObject
    from .health_response import HealthResponse
    from .health_response_status import HealthResponseStatus
    from .http_validation_error import HttpValidationError
    from .ingest_response import IngestResponse
    from .ingest_response_model import IngestResponseModel
    from .ingest_response_object import IngestResponseObject
    from .ingested_doc import IngestedDoc
    from .ingested_doc_object import IngestedDocObject
    from .open_ai_choice import OpenAiChoice
    from .open_ai_completion import OpenAiCompletion
    from .open_ai_completion_model import OpenAiCompletionModel
    from .open_ai_completion_object import OpenAiCompletionObject
    from .open_ai_delta import OpenAiDelta
    from .open_ai_message import OpenAiMessage
    from .open_ai_message_role import OpenAiMessageRole
    from .summarize_response import SummarizeResponse
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "ChatBody": ".chat_body",
    "Chunk": ".chunk",
    "ChunkObject": ".chunk_object",
    "ChunksResponse": ".chunks_response",
    "ChunksResponseModel": ".chunks_response_model",
    "ChunksResponseObject": ".chunks_response_object",
    "CompletionsBody": ".completions_body",
    "ContextFilter": ".context_filter",
    "Embedding": ".embedding",
    "EmbeddingObject": ".embedding_object",
    "EmbeddingsResponse": ".embeddings_response",
    "EmbeddingsResponseModel": ".embeddings_response_model",
    "EmbeddingsResponseObject": ".embeddings_response_object",
    "HealthResponse": ".health_response",
    "HealthResponseStatus": ".health_response_status",
    "HttpValidationError": ".http_validation_error",
    "IngestResponse": ".ingest_response",
    "IngestResponseModel": ".ingest_response_model",
    "IngestResponseObject": ".ingest_response_object",
    "IngestedDoc": ".ingested_doc",
    "IngestedDocObject": ".ingested_doc_object",
    "OpenAiChoice": ".open_ai_choice",
    "OpenAiCompletion": ".open_ai_completion",
    "OpenAiCompletionModel": ".open_ai_completion_model",
    "OpenAiCompletionObject": ".open_ai_completion_object",
    "OpenAiDelta": ".open_ai_delta",
    "OpenAiMessage": ".open_ai_message",
    "OpenAiMessageRole": ".open_ai_message_role",
    "SummarizeResponse": ".summarize_response",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "ChatBody",
    "Chunk",
    "ChunkObject",
    "ChunksResponse",
    "ChunksResponseModel",
    "ChunksResponseObject",
    "CompletionsBody",
    "ContextFilter",
    "Embedding",
    "EmbeddingObject",
    "EmbeddingsResponse",
    "EmbeddingsResponseModel",
    "EmbeddingsResponseObject",
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
    "ValidationError",
    "ValidationErrorLocItem",
]

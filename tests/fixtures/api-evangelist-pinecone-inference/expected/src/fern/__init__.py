



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DenseEmbedding,
        Document,
        Embedding,
        Embedding_Dense,
        Embedding_Sparse,
        EmbeddingsList,
        EmbeddingsListUsage,
        ErrorResponse,
        ErrorResponseError,
        ModelInfo,
        ModelInfoList,
        ModelInfoMetric,
        ModelInfoSupportedMetrics,
        ModelInfoSupportedParameter,
        ModelInfoSupportedParameterAllowedValuesItem,
        ModelInfoSupportedParameterDefault,
        RankedDocument,
        RerankResult,
        RerankResultUsage,
        SparseEmbedding,
        VectorType,
    )
    from .errors import BadRequestError, InternalServerError, NotFoundError, UnauthorizedError
    from . import inference
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .inference import EmbedRequestInputsItem
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DenseEmbedding": ".types",
    "Document": ".types",
    "EmbedRequestInputsItem": ".inference",
    "Embedding": ".types",
    "Embedding_Dense": ".types",
    "Embedding_Sparse": ".types",
    "EmbeddingsList": ".types",
    "EmbeddingsListUsage": ".types",
    "ErrorResponse": ".types",
    "ErrorResponseError": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "InternalServerError": ".errors",
    "ModelInfo": ".types",
    "ModelInfoList": ".types",
    "ModelInfoMetric": ".types",
    "ModelInfoSupportedMetrics": ".types",
    "ModelInfoSupportedParameter": ".types",
    "ModelInfoSupportedParameterAllowedValuesItem": ".types",
    "ModelInfoSupportedParameterDefault": ".types",
    "NotFoundError": ".errors",
    "RankedDocument": ".types",
    "RerankResult": ".types",
    "RerankResultUsage": ".types",
    "SparseEmbedding": ".types",
    "UnauthorizedError": ".errors",
    "VectorType": ".types",
    "__version__": ".version",
    "inference": ".inference",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DenseEmbedding",
    "Document",
    "EmbedRequestInputsItem",
    "Embedding",
    "Embedding_Dense",
    "Embedding_Sparse",
    "EmbeddingsList",
    "EmbeddingsListUsage",
    "ErrorResponse",
    "ErrorResponseError",
    "FernApi",
    "FernApiEnvironment",
    "InternalServerError",
    "ModelInfo",
    "ModelInfoList",
    "ModelInfoMetric",
    "ModelInfoSupportedMetrics",
    "ModelInfoSupportedParameter",
    "ModelInfoSupportedParameterAllowedValuesItem",
    "ModelInfoSupportedParameterDefault",
    "NotFoundError",
    "RankedDocument",
    "RerankResult",
    "RerankResultUsage",
    "SparseEmbedding",
    "UnauthorizedError",
    "VectorType",
    "__version__",
    "inference",
]

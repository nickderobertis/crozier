



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .dense_embedding import DenseEmbedding
    from .document import Document
    from .embedding import Embedding, Embedding_Dense, Embedding_Sparse
    from .embeddings_list import EmbeddingsList
    from .embeddings_list_usage import EmbeddingsListUsage
    from .error_response import ErrorResponse
    from .error_response_error import ErrorResponseError
    from .model_info import ModelInfo
    from .model_info_list import ModelInfoList
    from .model_info_metric import ModelInfoMetric
    from .model_info_supported_metrics import ModelInfoSupportedMetrics
    from .model_info_supported_parameter import ModelInfoSupportedParameter
    from .model_info_supported_parameter_allowed_values_item import ModelInfoSupportedParameterAllowedValuesItem
    from .model_info_supported_parameter_default import ModelInfoSupportedParameterDefault
    from .ranked_document import RankedDocument
    from .rerank_result import RerankResult
    from .rerank_result_usage import RerankResultUsage
    from .sparse_embedding import SparseEmbedding
    from .vector_type import VectorType
_dynamic_imports: typing.Dict[str, str] = {
    "DenseEmbedding": ".dense_embedding",
    "Document": ".document",
    "Embedding": ".embedding",
    "Embedding_Dense": ".embedding",
    "Embedding_Sparse": ".embedding",
    "EmbeddingsList": ".embeddings_list",
    "EmbeddingsListUsage": ".embeddings_list_usage",
    "ErrorResponse": ".error_response",
    "ErrorResponseError": ".error_response_error",
    "ModelInfo": ".model_info",
    "ModelInfoList": ".model_info_list",
    "ModelInfoMetric": ".model_info_metric",
    "ModelInfoSupportedMetrics": ".model_info_supported_metrics",
    "ModelInfoSupportedParameter": ".model_info_supported_parameter",
    "ModelInfoSupportedParameterAllowedValuesItem": ".model_info_supported_parameter_allowed_values_item",
    "ModelInfoSupportedParameterDefault": ".model_info_supported_parameter_default",
    "RankedDocument": ".ranked_document",
    "RerankResult": ".rerank_result",
    "RerankResultUsage": ".rerank_result_usage",
    "SparseEmbedding": ".sparse_embedding",
    "VectorType": ".vector_type",
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
    "DenseEmbedding",
    "Document",
    "Embedding",
    "Embedding_Dense",
    "Embedding_Sparse",
    "EmbeddingsList",
    "EmbeddingsListUsage",
    "ErrorResponse",
    "ErrorResponseError",
    "ModelInfo",
    "ModelInfoList",
    "ModelInfoMetric",
    "ModelInfoSupportedMetrics",
    "ModelInfoSupportedParameter",
    "ModelInfoSupportedParameterAllowedValuesItem",
    "ModelInfoSupportedParameterDefault",
    "RankedDocument",
    "RerankResult",
    "RerankResultUsage",
    "SparseEmbedding",
    "VectorType",
]

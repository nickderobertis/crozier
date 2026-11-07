



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        SchemaResponsePatchRequestAttributes,
        SchemaResponsePatchRequestAttributesReviewsState,
        SchemaResponsePatchRequestLinks,
        SchemaResponsePatchRequestRelationships,
        SchemaResponsePatchResponse,
        SchemaResponsePatchResponseAttributes,
        SchemaResponsePatchResponseAttributesReviewsState,
        SchemaResponsePatchResponseLinks,
        SchemaResponsePatchResponseRelationships,
        SchemaResponsePpostRequestAttributes,
        SchemaResponsePpostRequestAttributesReviewsState,
        SchemaResponsePpostRequestLinks,
        SchemaResponsePpostRequestRelationships,
        SchemaResponsePpostResponse,
        SchemaResponsePpostResponseAttributes,
        SchemaResponsePpostResponseAttributesReviewsState,
        SchemaResponsePpostResponseLinks,
        SchemaResponsePpostResponseRelationships,
        SchemaResponsesListResponse,
        SchemaResponsesListResponseAttributes,
        SchemaResponsesListResponseAttributesReviewsState,
        SchemaResponsesListResponseLinks,
        SchemaResponsesListResponseRelationships,
        SchemaResponsesReadResponse,
        SchemaResponsesReadResponseAttributes,
        SchemaResponsesReadResponseAttributesReviewsState,
        SchemaResponsesReadResponseLinks,
        SchemaResponsesReadResponseRelationships,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "SchemaResponsePatchRequestAttributes": ".types",
    "SchemaResponsePatchRequestAttributesReviewsState": ".types",
    "SchemaResponsePatchRequestLinks": ".types",
    "SchemaResponsePatchRequestRelationships": ".types",
    "SchemaResponsePatchResponse": ".types",
    "SchemaResponsePatchResponseAttributes": ".types",
    "SchemaResponsePatchResponseAttributesReviewsState": ".types",
    "SchemaResponsePatchResponseLinks": ".types",
    "SchemaResponsePatchResponseRelationships": ".types",
    "SchemaResponsePpostRequestAttributes": ".types",
    "SchemaResponsePpostRequestAttributesReviewsState": ".types",
    "SchemaResponsePpostRequestLinks": ".types",
    "SchemaResponsePpostRequestRelationships": ".types",
    "SchemaResponsePpostResponse": ".types",
    "SchemaResponsePpostResponseAttributes": ".types",
    "SchemaResponsePpostResponseAttributesReviewsState": ".types",
    "SchemaResponsePpostResponseLinks": ".types",
    "SchemaResponsePpostResponseRelationships": ".types",
    "SchemaResponsesListResponse": ".types",
    "SchemaResponsesListResponseAttributes": ".types",
    "SchemaResponsesListResponseAttributesReviewsState": ".types",
    "SchemaResponsesListResponseLinks": ".types",
    "SchemaResponsesListResponseRelationships": ".types",
    "SchemaResponsesReadResponse": ".types",
    "SchemaResponsesReadResponseAttributes": ".types",
    "SchemaResponsesReadResponseAttributesReviewsState": ".types",
    "SchemaResponsesReadResponseLinks": ".types",
    "SchemaResponsesReadResponseRelationships": ".types",
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
    "SchemaResponsePatchRequestAttributes",
    "SchemaResponsePatchRequestAttributesReviewsState",
    "SchemaResponsePatchRequestLinks",
    "SchemaResponsePatchRequestRelationships",
    "SchemaResponsePatchResponse",
    "SchemaResponsePatchResponseAttributes",
    "SchemaResponsePatchResponseAttributesReviewsState",
    "SchemaResponsePatchResponseLinks",
    "SchemaResponsePatchResponseRelationships",
    "SchemaResponsePpostRequestAttributes",
    "SchemaResponsePpostRequestAttributesReviewsState",
    "SchemaResponsePpostRequestLinks",
    "SchemaResponsePpostRequestRelationships",
    "SchemaResponsePpostResponse",
    "SchemaResponsePpostResponseAttributes",
    "SchemaResponsePpostResponseAttributesReviewsState",
    "SchemaResponsePpostResponseLinks",
    "SchemaResponsePpostResponseRelationships",
    "SchemaResponsesListResponse",
    "SchemaResponsesListResponseAttributes",
    "SchemaResponsesListResponseAttributesReviewsState",
    "SchemaResponsesListResponseLinks",
    "SchemaResponsesListResponseRelationships",
    "SchemaResponsesReadResponse",
    "SchemaResponsesReadResponseAttributes",
    "SchemaResponsesReadResponseAttributesReviewsState",
    "SchemaResponsesReadResponseLinks",
    "SchemaResponsesReadResponseRelationships",
]

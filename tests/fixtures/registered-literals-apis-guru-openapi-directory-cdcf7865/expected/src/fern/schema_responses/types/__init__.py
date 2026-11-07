



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .schema_response_patch_request_attributes import SchemaResponsePatchRequestAttributes
    from .schema_response_patch_request_attributes_reviews_state import SchemaResponsePatchRequestAttributesReviewsState
    from .schema_response_patch_request_links import SchemaResponsePatchRequestLinks
    from .schema_response_patch_request_relationships import SchemaResponsePatchRequestRelationships
    from .schema_response_patch_response import SchemaResponsePatchResponse
    from .schema_response_patch_response_attributes import SchemaResponsePatchResponseAttributes
    from .schema_response_patch_response_attributes_reviews_state import (
        SchemaResponsePatchResponseAttributesReviewsState,
    )
    from .schema_response_patch_response_links import SchemaResponsePatchResponseLinks
    from .schema_response_patch_response_relationships import SchemaResponsePatchResponseRelationships
    from .schema_response_ppost_request_attributes import SchemaResponsePpostRequestAttributes
    from .schema_response_ppost_request_attributes_reviews_state import SchemaResponsePpostRequestAttributesReviewsState
    from .schema_response_ppost_request_links import SchemaResponsePpostRequestLinks
    from .schema_response_ppost_request_relationships import SchemaResponsePpostRequestRelationships
    from .schema_response_ppost_response import SchemaResponsePpostResponse
    from .schema_response_ppost_response_attributes import SchemaResponsePpostResponseAttributes
    from .schema_response_ppost_response_attributes_reviews_state import (
        SchemaResponsePpostResponseAttributesReviewsState,
    )
    from .schema_response_ppost_response_links import SchemaResponsePpostResponseLinks
    from .schema_response_ppost_response_relationships import SchemaResponsePpostResponseRelationships
    from .schema_responses_list_response import SchemaResponsesListResponse
    from .schema_responses_list_response_attributes import SchemaResponsesListResponseAttributes
    from .schema_responses_list_response_attributes_reviews_state import (
        SchemaResponsesListResponseAttributesReviewsState,
    )
    from .schema_responses_list_response_links import SchemaResponsesListResponseLinks
    from .schema_responses_list_response_relationships import SchemaResponsesListResponseRelationships
    from .schema_responses_read_response import SchemaResponsesReadResponse
    from .schema_responses_read_response_attributes import SchemaResponsesReadResponseAttributes
    from .schema_responses_read_response_attributes_reviews_state import (
        SchemaResponsesReadResponseAttributesReviewsState,
    )
    from .schema_responses_read_response_links import SchemaResponsesReadResponseLinks
    from .schema_responses_read_response_relationships import SchemaResponsesReadResponseRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "SchemaResponsePatchRequestAttributes": ".schema_response_patch_request_attributes",
    "SchemaResponsePatchRequestAttributesReviewsState": ".schema_response_patch_request_attributes_reviews_state",
    "SchemaResponsePatchRequestLinks": ".schema_response_patch_request_links",
    "SchemaResponsePatchRequestRelationships": ".schema_response_patch_request_relationships",
    "SchemaResponsePatchResponse": ".schema_response_patch_response",
    "SchemaResponsePatchResponseAttributes": ".schema_response_patch_response_attributes",
    "SchemaResponsePatchResponseAttributesReviewsState": ".schema_response_patch_response_attributes_reviews_state",
    "SchemaResponsePatchResponseLinks": ".schema_response_patch_response_links",
    "SchemaResponsePatchResponseRelationships": ".schema_response_patch_response_relationships",
    "SchemaResponsePpostRequestAttributes": ".schema_response_ppost_request_attributes",
    "SchemaResponsePpostRequestAttributesReviewsState": ".schema_response_ppost_request_attributes_reviews_state",
    "SchemaResponsePpostRequestLinks": ".schema_response_ppost_request_links",
    "SchemaResponsePpostRequestRelationships": ".schema_response_ppost_request_relationships",
    "SchemaResponsePpostResponse": ".schema_response_ppost_response",
    "SchemaResponsePpostResponseAttributes": ".schema_response_ppost_response_attributes",
    "SchemaResponsePpostResponseAttributesReviewsState": ".schema_response_ppost_response_attributes_reviews_state",
    "SchemaResponsePpostResponseLinks": ".schema_response_ppost_response_links",
    "SchemaResponsePpostResponseRelationships": ".schema_response_ppost_response_relationships",
    "SchemaResponsesListResponse": ".schema_responses_list_response",
    "SchemaResponsesListResponseAttributes": ".schema_responses_list_response_attributes",
    "SchemaResponsesListResponseAttributesReviewsState": ".schema_responses_list_response_attributes_reviews_state",
    "SchemaResponsesListResponseLinks": ".schema_responses_list_response_links",
    "SchemaResponsesListResponseRelationships": ".schema_responses_list_response_relationships",
    "SchemaResponsesReadResponse": ".schema_responses_read_response",
    "SchemaResponsesReadResponseAttributes": ".schema_responses_read_response_attributes",
    "SchemaResponsesReadResponseAttributesReviewsState": ".schema_responses_read_response_attributes_reviews_state",
    "SchemaResponsesReadResponseLinks": ".schema_responses_read_response_links",
    "SchemaResponsesReadResponseRelationships": ".schema_responses_read_response_relationships",
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

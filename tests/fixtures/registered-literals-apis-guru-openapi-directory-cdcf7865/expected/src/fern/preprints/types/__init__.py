



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .preprints_bibliographic_contributors_list_response_item import (
        PreprintsBibliographicContributorsListResponseItem,
    )
    from .preprints_bibliographic_contributors_list_response_item_attributes import (
        PreprintsBibliographicContributorsListResponseItemAttributes,
    )
    from .preprints_bibliographic_contributors_list_response_item_attributes_permission import (
        PreprintsBibliographicContributorsListResponseItemAttributesPermission,
    )
    from .preprints_bibliographic_contributors_list_response_item_links import (
        PreprintsBibliographicContributorsListResponseItemLinks,
    )
    from .preprints_bibliographic_contributors_list_response_item_relationships import (
        PreprintsBibliographicContributorsListResponseItemRelationships,
    )
    from .preprints_citation_list_response import PreprintsCitationListResponse
    from .preprints_citation_list_response_attributes import PreprintsCitationListResponseAttributes
    from .preprints_citation_list_response_links import PreprintsCitationListResponseLinks
    from .preprints_citation_read_response import PreprintsCitationReadResponse
    from .preprints_citation_read_response_attributes import PreprintsCitationReadResponseAttributes
    from .preprints_contributors_create_request_attributes import PreprintsContributorsCreateRequestAttributes
    from .preprints_contributors_create_request_attributes_permission import (
        PreprintsContributorsCreateRequestAttributesPermission,
    )
    from .preprints_contributors_list_response_item import PreprintsContributorsListResponseItem
    from .preprints_contributors_list_response_item_attributes import PreprintsContributorsListResponseItemAttributes
    from .preprints_contributors_list_response_item_attributes_permission import (
        PreprintsContributorsListResponseItemAttributesPermission,
    )
    from .preprints_contributors_list_response_item_links import PreprintsContributorsListResponseItemLinks
    from .preprints_contributors_list_response_item_relationships import (
        PreprintsContributorsListResponseItemRelationships,
    )
    from .preprints_create_request_attributes import PreprintsCreateRequestAttributes
    from .preprints_create_request_relationships import PreprintsCreateRequestRelationships
    from .preprints_list_response_item import PreprintsListResponseItem
    from .preprints_list_response_item_attributes import PreprintsListResponseItemAttributes
    from .preprints_list_response_item_links import PreprintsListResponseItemLinks
    from .preprints_list_response_item_relationships import PreprintsListResponseItemRelationships
    from .preprints_read_response import PreprintsReadResponse
    from .preprints_read_response_attributes import PreprintsReadResponseAttributes
    from .preprints_read_response_links import PreprintsReadResponseLinks
    from .preprints_read_response_relationships import PreprintsReadResponseRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "PreprintsBibliographicContributorsListResponseItem": ".preprints_bibliographic_contributors_list_response_item",
    "PreprintsBibliographicContributorsListResponseItemAttributes": ".preprints_bibliographic_contributors_list_response_item_attributes",
    "PreprintsBibliographicContributorsListResponseItemAttributesPermission": ".preprints_bibliographic_contributors_list_response_item_attributes_permission",
    "PreprintsBibliographicContributorsListResponseItemLinks": ".preprints_bibliographic_contributors_list_response_item_links",
    "PreprintsBibliographicContributorsListResponseItemRelationships": ".preprints_bibliographic_contributors_list_response_item_relationships",
    "PreprintsCitationListResponse": ".preprints_citation_list_response",
    "PreprintsCitationListResponseAttributes": ".preprints_citation_list_response_attributes",
    "PreprintsCitationListResponseLinks": ".preprints_citation_list_response_links",
    "PreprintsCitationReadResponse": ".preprints_citation_read_response",
    "PreprintsCitationReadResponseAttributes": ".preprints_citation_read_response_attributes",
    "PreprintsContributorsCreateRequestAttributes": ".preprints_contributors_create_request_attributes",
    "PreprintsContributorsCreateRequestAttributesPermission": ".preprints_contributors_create_request_attributes_permission",
    "PreprintsContributorsListResponseItem": ".preprints_contributors_list_response_item",
    "PreprintsContributorsListResponseItemAttributes": ".preprints_contributors_list_response_item_attributes",
    "PreprintsContributorsListResponseItemAttributesPermission": ".preprints_contributors_list_response_item_attributes_permission",
    "PreprintsContributorsListResponseItemLinks": ".preprints_contributors_list_response_item_links",
    "PreprintsContributorsListResponseItemRelationships": ".preprints_contributors_list_response_item_relationships",
    "PreprintsCreateRequestAttributes": ".preprints_create_request_attributes",
    "PreprintsCreateRequestRelationships": ".preprints_create_request_relationships",
    "PreprintsListResponseItem": ".preprints_list_response_item",
    "PreprintsListResponseItemAttributes": ".preprints_list_response_item_attributes",
    "PreprintsListResponseItemLinks": ".preprints_list_response_item_links",
    "PreprintsListResponseItemRelationships": ".preprints_list_response_item_relationships",
    "PreprintsReadResponse": ".preprints_read_response",
    "PreprintsReadResponseAttributes": ".preprints_read_response_attributes",
    "PreprintsReadResponseLinks": ".preprints_read_response_links",
    "PreprintsReadResponseRelationships": ".preprints_read_response_relationships",
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
    "PreprintsBibliographicContributorsListResponseItem",
    "PreprintsBibliographicContributorsListResponseItemAttributes",
    "PreprintsBibliographicContributorsListResponseItemAttributesPermission",
    "PreprintsBibliographicContributorsListResponseItemLinks",
    "PreprintsBibliographicContributorsListResponseItemRelationships",
    "PreprintsCitationListResponse",
    "PreprintsCitationListResponseAttributes",
    "PreprintsCitationListResponseLinks",
    "PreprintsCitationReadResponse",
    "PreprintsCitationReadResponseAttributes",
    "PreprintsContributorsCreateRequestAttributes",
    "PreprintsContributorsCreateRequestAttributesPermission",
    "PreprintsContributorsListResponseItem",
    "PreprintsContributorsListResponseItemAttributes",
    "PreprintsContributorsListResponseItemAttributesPermission",
    "PreprintsContributorsListResponseItemLinks",
    "PreprintsContributorsListResponseItemRelationships",
    "PreprintsCreateRequestAttributes",
    "PreprintsCreateRequestRelationships",
    "PreprintsListResponseItem",
    "PreprintsListResponseItemAttributes",
    "PreprintsListResponseItemLinks",
    "PreprintsListResponseItemRelationships",
    "PreprintsReadResponse",
    "PreprintsReadResponseAttributes",
    "PreprintsReadResponseLinks",
    "PreprintsReadResponseRelationships",
]

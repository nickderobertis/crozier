



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PreprintsBibliographicContributorsListResponseItem,
        PreprintsBibliographicContributorsListResponseItemAttributes,
        PreprintsBibliographicContributorsListResponseItemAttributesPermission,
        PreprintsBibliographicContributorsListResponseItemLinks,
        PreprintsBibliographicContributorsListResponseItemRelationships,
        PreprintsCitationListResponse,
        PreprintsCitationListResponseAttributes,
        PreprintsCitationListResponseLinks,
        PreprintsCitationReadResponse,
        PreprintsCitationReadResponseAttributes,
        PreprintsContributorsCreateRequestAttributes,
        PreprintsContributorsCreateRequestAttributesPermission,
        PreprintsContributorsListResponseItem,
        PreprintsContributorsListResponseItemAttributes,
        PreprintsContributorsListResponseItemAttributesPermission,
        PreprintsContributorsListResponseItemLinks,
        PreprintsContributorsListResponseItemRelationships,
        PreprintsCreateRequestAttributes,
        PreprintsCreateRequestRelationships,
        PreprintsListResponseItem,
        PreprintsListResponseItemAttributes,
        PreprintsListResponseItemLinks,
        PreprintsListResponseItemRelationships,
        PreprintsReadResponse,
        PreprintsReadResponseAttributes,
        PreprintsReadResponseLinks,
        PreprintsReadResponseRelationships,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PreprintsBibliographicContributorsListResponseItem": ".types",
    "PreprintsBibliographicContributorsListResponseItemAttributes": ".types",
    "PreprintsBibliographicContributorsListResponseItemAttributesPermission": ".types",
    "PreprintsBibliographicContributorsListResponseItemLinks": ".types",
    "PreprintsBibliographicContributorsListResponseItemRelationships": ".types",
    "PreprintsCitationListResponse": ".types",
    "PreprintsCitationListResponseAttributes": ".types",
    "PreprintsCitationListResponseLinks": ".types",
    "PreprintsCitationReadResponse": ".types",
    "PreprintsCitationReadResponseAttributes": ".types",
    "PreprintsContributorsCreateRequestAttributes": ".types",
    "PreprintsContributorsCreateRequestAttributesPermission": ".types",
    "PreprintsContributorsListResponseItem": ".types",
    "PreprintsContributorsListResponseItemAttributes": ".types",
    "PreprintsContributorsListResponseItemAttributesPermission": ".types",
    "PreprintsContributorsListResponseItemLinks": ".types",
    "PreprintsContributorsListResponseItemRelationships": ".types",
    "PreprintsCreateRequestAttributes": ".types",
    "PreprintsCreateRequestRelationships": ".types",
    "PreprintsListResponseItem": ".types",
    "PreprintsListResponseItemAttributes": ".types",
    "PreprintsListResponseItemLinks": ".types",
    "PreprintsListResponseItemRelationships": ".types",
    "PreprintsReadResponse": ".types",
    "PreprintsReadResponseAttributes": ".types",
    "PreprintsReadResponseLinks": ".types",
    "PreprintsReadResponseRelationships": ".types",
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

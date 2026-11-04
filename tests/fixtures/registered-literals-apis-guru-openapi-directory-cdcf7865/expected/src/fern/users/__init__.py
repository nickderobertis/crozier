



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        UsersAddonAccountsListResponseItem,
        UsersAddonAccountsListResponseItemAttributes,
        UsersAddonAccountsListResponseItemLinks,
        UsersAddonAccountsReadResponse,
        UsersAddonAccountsReadResponseAttributes,
        UsersAddonAccountsReadResponseLinks,
        UsersAddonsListResponseItem,
        UsersAddonsListResponseItemAttributes,
        UsersAddonsListResponseItemLinks,
        UsersAddonsReadResponse,
        UsersAddonsReadResponseAttributes,
        UsersAddonsReadResponseLinks,
        UsersInstitutionsListResponseItem,
        UsersInstitutionsListResponseItemAttributes,
        UsersInstitutionsListResponseItemLinks,
        UsersInstitutionsListResponseItemRelationships,
        UsersListResponseItem,
        UsersListResponseItemAttributes,
        UsersListResponseItemLinks,
        UsersListResponseItemRelationships,
        UsersNodesListResponseItem,
        UsersNodesListResponseItemAttributes,
        UsersNodesListResponseItemAttributesCategory,
        UsersNodesListResponseItemLinks,
        UsersNodesListResponseItemRelationships,
        UsersPartialUpdateRequestAttributes,
        UsersPreprintsListResponseItem,
        UsersPreprintsListResponseItemAttributes,
        UsersPreprintsListResponseItemLinks,
        UsersPreprintsListResponseItemRelationships,
        UsersReadResponse,
        UsersReadResponseAttributes,
        UsersReadResponseLinks,
        UsersReadResponseRelationships,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "UsersAddonAccountsListResponseItem": ".types",
    "UsersAddonAccountsListResponseItemAttributes": ".types",
    "UsersAddonAccountsListResponseItemLinks": ".types",
    "UsersAddonAccountsReadResponse": ".types",
    "UsersAddonAccountsReadResponseAttributes": ".types",
    "UsersAddonAccountsReadResponseLinks": ".types",
    "UsersAddonsListResponseItem": ".types",
    "UsersAddonsListResponseItemAttributes": ".types",
    "UsersAddonsListResponseItemLinks": ".types",
    "UsersAddonsReadResponse": ".types",
    "UsersAddonsReadResponseAttributes": ".types",
    "UsersAddonsReadResponseLinks": ".types",
    "UsersInstitutionsListResponseItem": ".types",
    "UsersInstitutionsListResponseItemAttributes": ".types",
    "UsersInstitutionsListResponseItemLinks": ".types",
    "UsersInstitutionsListResponseItemRelationships": ".types",
    "UsersListResponseItem": ".types",
    "UsersListResponseItemAttributes": ".types",
    "UsersListResponseItemLinks": ".types",
    "UsersListResponseItemRelationships": ".types",
    "UsersNodesListResponseItem": ".types",
    "UsersNodesListResponseItemAttributes": ".types",
    "UsersNodesListResponseItemAttributesCategory": ".types",
    "UsersNodesListResponseItemLinks": ".types",
    "UsersNodesListResponseItemRelationships": ".types",
    "UsersPartialUpdateRequestAttributes": ".types",
    "UsersPreprintsListResponseItem": ".types",
    "UsersPreprintsListResponseItemAttributes": ".types",
    "UsersPreprintsListResponseItemLinks": ".types",
    "UsersPreprintsListResponseItemRelationships": ".types",
    "UsersReadResponse": ".types",
    "UsersReadResponseAttributes": ".types",
    "UsersReadResponseLinks": ".types",
    "UsersReadResponseRelationships": ".types",
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
    "UsersAddonAccountsListResponseItem",
    "UsersAddonAccountsListResponseItemAttributes",
    "UsersAddonAccountsListResponseItemLinks",
    "UsersAddonAccountsReadResponse",
    "UsersAddonAccountsReadResponseAttributes",
    "UsersAddonAccountsReadResponseLinks",
    "UsersAddonsListResponseItem",
    "UsersAddonsListResponseItemAttributes",
    "UsersAddonsListResponseItemLinks",
    "UsersAddonsReadResponse",
    "UsersAddonsReadResponseAttributes",
    "UsersAddonsReadResponseLinks",
    "UsersInstitutionsListResponseItem",
    "UsersInstitutionsListResponseItemAttributes",
    "UsersInstitutionsListResponseItemLinks",
    "UsersInstitutionsListResponseItemRelationships",
    "UsersListResponseItem",
    "UsersListResponseItemAttributes",
    "UsersListResponseItemLinks",
    "UsersListResponseItemRelationships",
    "UsersNodesListResponseItem",
    "UsersNodesListResponseItemAttributes",
    "UsersNodesListResponseItemAttributesCategory",
    "UsersNodesListResponseItemLinks",
    "UsersNodesListResponseItemRelationships",
    "UsersPartialUpdateRequestAttributes",
    "UsersPreprintsListResponseItem",
    "UsersPreprintsListResponseItemAttributes",
    "UsersPreprintsListResponseItemLinks",
    "UsersPreprintsListResponseItemRelationships",
    "UsersReadResponse",
    "UsersReadResponseAttributes",
    "UsersReadResponseLinks",
    "UsersReadResponseRelationships",
]

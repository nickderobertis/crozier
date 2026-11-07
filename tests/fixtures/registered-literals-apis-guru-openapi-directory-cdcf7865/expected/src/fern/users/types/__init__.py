



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .users_addon_accounts_list_response_item import UsersAddonAccountsListResponseItem
    from .users_addon_accounts_list_response_item_attributes import UsersAddonAccountsListResponseItemAttributes
    from .users_addon_accounts_list_response_item_links import UsersAddonAccountsListResponseItemLinks
    from .users_addon_accounts_read_response import UsersAddonAccountsReadResponse
    from .users_addon_accounts_read_response_attributes import UsersAddonAccountsReadResponseAttributes
    from .users_addon_accounts_read_response_links import UsersAddonAccountsReadResponseLinks
    from .users_addons_list_response_item import UsersAddonsListResponseItem
    from .users_addons_list_response_item_attributes import UsersAddonsListResponseItemAttributes
    from .users_addons_list_response_item_links import UsersAddonsListResponseItemLinks
    from .users_addons_read_response import UsersAddonsReadResponse
    from .users_addons_read_response_attributes import UsersAddonsReadResponseAttributes
    from .users_addons_read_response_links import UsersAddonsReadResponseLinks
    from .users_institutions_list_response_item import UsersInstitutionsListResponseItem
    from .users_institutions_list_response_item_attributes import UsersInstitutionsListResponseItemAttributes
    from .users_institutions_list_response_item_links import UsersInstitutionsListResponseItemLinks
    from .users_institutions_list_response_item_relationships import UsersInstitutionsListResponseItemRelationships
    from .users_list_response_item import UsersListResponseItem
    from .users_list_response_item_attributes import UsersListResponseItemAttributes
    from .users_list_response_item_links import UsersListResponseItemLinks
    from .users_list_response_item_relationships import UsersListResponseItemRelationships
    from .users_nodes_list_response_item import UsersNodesListResponseItem
    from .users_nodes_list_response_item_attributes import UsersNodesListResponseItemAttributes
    from .users_nodes_list_response_item_attributes_category import UsersNodesListResponseItemAttributesCategory
    from .users_nodes_list_response_item_links import UsersNodesListResponseItemLinks
    from .users_nodes_list_response_item_relationships import UsersNodesListResponseItemRelationships
    from .users_partial_update_request_attributes import UsersPartialUpdateRequestAttributes
    from .users_preprints_list_response_item import UsersPreprintsListResponseItem
    from .users_preprints_list_response_item_attributes import UsersPreprintsListResponseItemAttributes
    from .users_preprints_list_response_item_links import UsersPreprintsListResponseItemLinks
    from .users_preprints_list_response_item_relationships import UsersPreprintsListResponseItemRelationships
    from .users_read_response import UsersReadResponse
    from .users_read_response_attributes import UsersReadResponseAttributes
    from .users_read_response_links import UsersReadResponseLinks
    from .users_read_response_relationships import UsersReadResponseRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "UsersAddonAccountsListResponseItem": ".users_addon_accounts_list_response_item",
    "UsersAddonAccountsListResponseItemAttributes": ".users_addon_accounts_list_response_item_attributes",
    "UsersAddonAccountsListResponseItemLinks": ".users_addon_accounts_list_response_item_links",
    "UsersAddonAccountsReadResponse": ".users_addon_accounts_read_response",
    "UsersAddonAccountsReadResponseAttributes": ".users_addon_accounts_read_response_attributes",
    "UsersAddonAccountsReadResponseLinks": ".users_addon_accounts_read_response_links",
    "UsersAddonsListResponseItem": ".users_addons_list_response_item",
    "UsersAddonsListResponseItemAttributes": ".users_addons_list_response_item_attributes",
    "UsersAddonsListResponseItemLinks": ".users_addons_list_response_item_links",
    "UsersAddonsReadResponse": ".users_addons_read_response",
    "UsersAddonsReadResponseAttributes": ".users_addons_read_response_attributes",
    "UsersAddonsReadResponseLinks": ".users_addons_read_response_links",
    "UsersInstitutionsListResponseItem": ".users_institutions_list_response_item",
    "UsersInstitutionsListResponseItemAttributes": ".users_institutions_list_response_item_attributes",
    "UsersInstitutionsListResponseItemLinks": ".users_institutions_list_response_item_links",
    "UsersInstitutionsListResponseItemRelationships": ".users_institutions_list_response_item_relationships",
    "UsersListResponseItem": ".users_list_response_item",
    "UsersListResponseItemAttributes": ".users_list_response_item_attributes",
    "UsersListResponseItemLinks": ".users_list_response_item_links",
    "UsersListResponseItemRelationships": ".users_list_response_item_relationships",
    "UsersNodesListResponseItem": ".users_nodes_list_response_item",
    "UsersNodesListResponseItemAttributes": ".users_nodes_list_response_item_attributes",
    "UsersNodesListResponseItemAttributesCategory": ".users_nodes_list_response_item_attributes_category",
    "UsersNodesListResponseItemLinks": ".users_nodes_list_response_item_links",
    "UsersNodesListResponseItemRelationships": ".users_nodes_list_response_item_relationships",
    "UsersPartialUpdateRequestAttributes": ".users_partial_update_request_attributes",
    "UsersPreprintsListResponseItem": ".users_preprints_list_response_item",
    "UsersPreprintsListResponseItemAttributes": ".users_preprints_list_response_item_attributes",
    "UsersPreprintsListResponseItemLinks": ".users_preprints_list_response_item_links",
    "UsersPreprintsListResponseItemRelationships": ".users_preprints_list_response_item_relationships",
    "UsersReadResponse": ".users_read_response",
    "UsersReadResponseAttributes": ".users_read_response_attributes",
    "UsersReadResponseLinks": ".users_read_response_links",
    "UsersReadResponseRelationships": ".users_read_response_relationships",
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





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .institutions_detail_response_item import InstitutionsDetailResponseItem
    from .institutions_detail_response_item_attributes import InstitutionsDetailResponseItemAttributes
    from .institutions_detail_response_item_links import InstitutionsDetailResponseItemLinks
    from .institutions_detail_response_item_relationships import InstitutionsDetailResponseItemRelationships
    from .institutions_list_response_item import InstitutionsListResponseItem
    from .institutions_list_response_item_attributes import InstitutionsListResponseItemAttributes
    from .institutions_list_response_item_links import InstitutionsListResponseItemLinks
    from .institutions_list_response_item_relationships import InstitutionsListResponseItemRelationships
    from .institutions_node_list_response_item import InstitutionsNodeListResponseItem
    from .institutions_node_list_response_item_attributes import InstitutionsNodeListResponseItemAttributes
    from .institutions_node_list_response_item_attributes_category import (
        InstitutionsNodeListResponseItemAttributesCategory,
    )
    from .institutions_node_list_response_item_links import InstitutionsNodeListResponseItemLinks
    from .institutions_node_list_response_item_relationships import InstitutionsNodeListResponseItemRelationships
    from .institutions_users_list_response_item import InstitutionsUsersListResponseItem
    from .institutions_users_list_response_item_attributes import InstitutionsUsersListResponseItemAttributes
    from .institutions_users_list_response_item_links import InstitutionsUsersListResponseItemLinks
    from .institutions_users_list_response_item_relationships import InstitutionsUsersListResponseItemRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "InstitutionsDetailResponseItem": ".institutions_detail_response_item",
    "InstitutionsDetailResponseItemAttributes": ".institutions_detail_response_item_attributes",
    "InstitutionsDetailResponseItemLinks": ".institutions_detail_response_item_links",
    "InstitutionsDetailResponseItemRelationships": ".institutions_detail_response_item_relationships",
    "InstitutionsListResponseItem": ".institutions_list_response_item",
    "InstitutionsListResponseItemAttributes": ".institutions_list_response_item_attributes",
    "InstitutionsListResponseItemLinks": ".institutions_list_response_item_links",
    "InstitutionsListResponseItemRelationships": ".institutions_list_response_item_relationships",
    "InstitutionsNodeListResponseItem": ".institutions_node_list_response_item",
    "InstitutionsNodeListResponseItemAttributes": ".institutions_node_list_response_item_attributes",
    "InstitutionsNodeListResponseItemAttributesCategory": ".institutions_node_list_response_item_attributes_category",
    "InstitutionsNodeListResponseItemLinks": ".institutions_node_list_response_item_links",
    "InstitutionsNodeListResponseItemRelationships": ".institutions_node_list_response_item_relationships",
    "InstitutionsUsersListResponseItem": ".institutions_users_list_response_item",
    "InstitutionsUsersListResponseItemAttributes": ".institutions_users_list_response_item_attributes",
    "InstitutionsUsersListResponseItemLinks": ".institutions_users_list_response_item_links",
    "InstitutionsUsersListResponseItemRelationships": ".institutions_users_list_response_item_relationships",
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
    "InstitutionsDetailResponseItem",
    "InstitutionsDetailResponseItemAttributes",
    "InstitutionsDetailResponseItemLinks",
    "InstitutionsDetailResponseItemRelationships",
    "InstitutionsListResponseItem",
    "InstitutionsListResponseItemAttributes",
    "InstitutionsListResponseItemLinks",
    "InstitutionsListResponseItemRelationships",
    "InstitutionsNodeListResponseItem",
    "InstitutionsNodeListResponseItemAttributes",
    "InstitutionsNodeListResponseItemAttributesCategory",
    "InstitutionsNodeListResponseItemLinks",
    "InstitutionsNodeListResponseItemRelationships",
    "InstitutionsUsersListResponseItem",
    "InstitutionsUsersListResponseItemAttributes",
    "InstitutionsUsersListResponseItemLinks",
    "InstitutionsUsersListResponseItemRelationships",
]

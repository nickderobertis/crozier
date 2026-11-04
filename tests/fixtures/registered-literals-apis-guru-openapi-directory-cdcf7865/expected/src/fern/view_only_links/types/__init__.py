



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .view_only_links_node_list_response_item import ViewOnlyLinksNodeListResponseItem
    from .view_only_links_node_list_response_item_attributes import ViewOnlyLinksNodeListResponseItemAttributes
    from .view_only_links_node_list_response_item_attributes_category import (
        ViewOnlyLinksNodeListResponseItemAttributesCategory,
    )
    from .view_only_links_node_list_response_item_links import ViewOnlyLinksNodeListResponseItemLinks
    from .view_only_links_node_list_response_item_relationships import ViewOnlyLinksNodeListResponseItemRelationships
    from .view_only_links_read_response import ViewOnlyLinksReadResponse
    from .view_only_links_read_response_attributes import ViewOnlyLinksReadResponseAttributes
    from .view_only_links_read_response_relationships import ViewOnlyLinksReadResponseRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "ViewOnlyLinksNodeListResponseItem": ".view_only_links_node_list_response_item",
    "ViewOnlyLinksNodeListResponseItemAttributes": ".view_only_links_node_list_response_item_attributes",
    "ViewOnlyLinksNodeListResponseItemAttributesCategory": ".view_only_links_node_list_response_item_attributes_category",
    "ViewOnlyLinksNodeListResponseItemLinks": ".view_only_links_node_list_response_item_links",
    "ViewOnlyLinksNodeListResponseItemRelationships": ".view_only_links_node_list_response_item_relationships",
    "ViewOnlyLinksReadResponse": ".view_only_links_read_response",
    "ViewOnlyLinksReadResponseAttributes": ".view_only_links_read_response_attributes",
    "ViewOnlyLinksReadResponseRelationships": ".view_only_links_read_response_relationships",
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
    "ViewOnlyLinksNodeListResponseItem",
    "ViewOnlyLinksNodeListResponseItemAttributes",
    "ViewOnlyLinksNodeListResponseItemAttributesCategory",
    "ViewOnlyLinksNodeListResponseItemLinks",
    "ViewOnlyLinksNodeListResponseItemRelationships",
    "ViewOnlyLinksReadResponse",
    "ViewOnlyLinksReadResponseAttributes",
    "ViewOnlyLinksReadResponseRelationships",
]

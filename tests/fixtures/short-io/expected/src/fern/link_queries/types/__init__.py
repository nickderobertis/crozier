



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_api_links_request_date_sort_order import GetApiLinksRequestDateSortOrder
    from .get_api_links_response import GetApiLinksResponse
    from .get_api_links_response_links_item import GetApiLinksResponseLinksItem
    from .get_api_links_response_links_item_expires_at import GetApiLinksResponseLinksItemExpiresAt
    from .get_api_links_response_links_item_redirect_type import GetApiLinksResponseLinksItemRedirectType
    from .get_api_links_response_links_item_source import GetApiLinksResponseLinksItemSource
    from .get_api_links_response_links_item_split_urlv2item import GetApiLinksResponseLinksItemSplitUrlv2Item
    from .get_api_links_response_links_item_ttl import GetApiLinksResponseLinksItemTtl
    from .get_api_links_response_links_item_user import GetApiLinksResponseLinksItemUser
    from .get_links_expand_response import GetLinksExpandResponse
    from .get_links_expand_response_expires_at import GetLinksExpandResponseExpiresAt
    from .get_links_expand_response_redirect_type import GetLinksExpandResponseRedirectType
    from .get_links_expand_response_source import GetLinksExpandResponseSource
    from .get_links_expand_response_split_urlv2item import GetLinksExpandResponseSplitUrlv2Item
    from .get_links_expand_response_ttl import GetLinksExpandResponseTtl
    from .get_links_expand_response_user import GetLinksExpandResponseUser
    from .get_links_link_id_response import GetLinksLinkIdResponse
    from .get_links_link_id_response_expires_at import GetLinksLinkIdResponseExpiresAt
    from .get_links_link_id_response_redirect_type import GetLinksLinkIdResponseRedirectType
    from .get_links_link_id_response_source import GetLinksLinkIdResponseSource
    from .get_links_link_id_response_split_urlv2item import GetLinksLinkIdResponseSplitUrlv2Item
    from .get_links_link_id_response_ttl import GetLinksLinkIdResponseTtl
    from .get_links_link_id_response_user import GetLinksLinkIdResponseUser
    from .post_links_opengraph_debug_response import PostLinksOpengraphDebugResponse
    from .post_links_opengraph_debug_response_og_tags_item import PostLinksOpengraphDebugResponseOgTagsItem
_dynamic_imports: typing.Dict[str, str] = {
    "GetApiLinksRequestDateSortOrder": ".get_api_links_request_date_sort_order",
    "GetApiLinksResponse": ".get_api_links_response",
    "GetApiLinksResponseLinksItem": ".get_api_links_response_links_item",
    "GetApiLinksResponseLinksItemExpiresAt": ".get_api_links_response_links_item_expires_at",
    "GetApiLinksResponseLinksItemRedirectType": ".get_api_links_response_links_item_redirect_type",
    "GetApiLinksResponseLinksItemSource": ".get_api_links_response_links_item_source",
    "GetApiLinksResponseLinksItemSplitUrlv2Item": ".get_api_links_response_links_item_split_urlv2item",
    "GetApiLinksResponseLinksItemTtl": ".get_api_links_response_links_item_ttl",
    "GetApiLinksResponseLinksItemUser": ".get_api_links_response_links_item_user",
    "GetLinksExpandResponse": ".get_links_expand_response",
    "GetLinksExpandResponseExpiresAt": ".get_links_expand_response_expires_at",
    "GetLinksExpandResponseRedirectType": ".get_links_expand_response_redirect_type",
    "GetLinksExpandResponseSource": ".get_links_expand_response_source",
    "GetLinksExpandResponseSplitUrlv2Item": ".get_links_expand_response_split_urlv2item",
    "GetLinksExpandResponseTtl": ".get_links_expand_response_ttl",
    "GetLinksExpandResponseUser": ".get_links_expand_response_user",
    "GetLinksLinkIdResponse": ".get_links_link_id_response",
    "GetLinksLinkIdResponseExpiresAt": ".get_links_link_id_response_expires_at",
    "GetLinksLinkIdResponseRedirectType": ".get_links_link_id_response_redirect_type",
    "GetLinksLinkIdResponseSource": ".get_links_link_id_response_source",
    "GetLinksLinkIdResponseSplitUrlv2Item": ".get_links_link_id_response_split_urlv2item",
    "GetLinksLinkIdResponseTtl": ".get_links_link_id_response_ttl",
    "GetLinksLinkIdResponseUser": ".get_links_link_id_response_user",
    "PostLinksOpengraphDebugResponse": ".post_links_opengraph_debug_response",
    "PostLinksOpengraphDebugResponseOgTagsItem": ".post_links_opengraph_debug_response_og_tags_item",
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
    "GetApiLinksRequestDateSortOrder",
    "GetApiLinksResponse",
    "GetApiLinksResponseLinksItem",
    "GetApiLinksResponseLinksItemExpiresAt",
    "GetApiLinksResponseLinksItemRedirectType",
    "GetApiLinksResponseLinksItemSource",
    "GetApiLinksResponseLinksItemSplitUrlv2Item",
    "GetApiLinksResponseLinksItemTtl",
    "GetApiLinksResponseLinksItemUser",
    "GetLinksExpandResponse",
    "GetLinksExpandResponseExpiresAt",
    "GetLinksExpandResponseRedirectType",
    "GetLinksExpandResponseSource",
    "GetLinksExpandResponseSplitUrlv2Item",
    "GetLinksExpandResponseTtl",
    "GetLinksExpandResponseUser",
    "GetLinksLinkIdResponse",
    "GetLinksLinkIdResponseExpiresAt",
    "GetLinksLinkIdResponseRedirectType",
    "GetLinksLinkIdResponseSource",
    "GetLinksLinkIdResponseSplitUrlv2Item",
    "GetLinksLinkIdResponseTtl",
    "GetLinksLinkIdResponseUser",
    "PostLinksOpengraphDebugResponse",
    "PostLinksOpengraphDebugResponseOgTagsItem",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetApiLinksRequestDateSortOrder,
        GetApiLinksResponse,
        GetApiLinksResponseLinksItem,
        GetApiLinksResponseLinksItemExpiresAt,
        GetApiLinksResponseLinksItemRedirectType,
        GetApiLinksResponseLinksItemSource,
        GetApiLinksResponseLinksItemSplitUrlv2Item,
        GetApiLinksResponseLinksItemTtl,
        GetApiLinksResponseLinksItemUser,
        GetLinksExpandResponse,
        GetLinksExpandResponseExpiresAt,
        GetLinksExpandResponseRedirectType,
        GetLinksExpandResponseSource,
        GetLinksExpandResponseSplitUrlv2Item,
        GetLinksExpandResponseTtl,
        GetLinksExpandResponseUser,
        GetLinksLinkIdResponse,
        GetLinksLinkIdResponseExpiresAt,
        GetLinksLinkIdResponseRedirectType,
        GetLinksLinkIdResponseSource,
        GetLinksLinkIdResponseSplitUrlv2Item,
        GetLinksLinkIdResponseTtl,
        GetLinksLinkIdResponseUser,
        PostLinksOpengraphDebugResponse,
        PostLinksOpengraphDebugResponseOgTagsItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetApiLinksRequestDateSortOrder": ".types",
    "GetApiLinksResponse": ".types",
    "GetApiLinksResponseLinksItem": ".types",
    "GetApiLinksResponseLinksItemExpiresAt": ".types",
    "GetApiLinksResponseLinksItemRedirectType": ".types",
    "GetApiLinksResponseLinksItemSource": ".types",
    "GetApiLinksResponseLinksItemSplitUrlv2Item": ".types",
    "GetApiLinksResponseLinksItemTtl": ".types",
    "GetApiLinksResponseLinksItemUser": ".types",
    "GetLinksExpandResponse": ".types",
    "GetLinksExpandResponseExpiresAt": ".types",
    "GetLinksExpandResponseRedirectType": ".types",
    "GetLinksExpandResponseSource": ".types",
    "GetLinksExpandResponseSplitUrlv2Item": ".types",
    "GetLinksExpandResponseTtl": ".types",
    "GetLinksExpandResponseUser": ".types",
    "GetLinksLinkIdResponse": ".types",
    "GetLinksLinkIdResponseExpiresAt": ".types",
    "GetLinksLinkIdResponseRedirectType": ".types",
    "GetLinksLinkIdResponseSource": ".types",
    "GetLinksLinkIdResponseSplitUrlv2Item": ".types",
    "GetLinksLinkIdResponseTtl": ".types",
    "GetLinksLinkIdResponseUser": ".types",
    "PostLinksOpengraphDebugResponse": ".types",
    "PostLinksOpengraphDebugResponseOgTagsItem": ".types",
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





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_legs_response import ListLegsResponse
    from .list_legs_response_embedded import ListLegsResponseEmbedded
    from .list_legs_response_embedded_legs_item import ListLegsResponseEmbeddedLegsItem
    from .list_legs_response_links import ListLegsResponseLinks
    from .list_legs_response_links_self import ListLegsResponseLinksSelf
_dynamic_imports: typing.Dict[str, str] = {
    "ListLegsResponse": ".list_legs_response",
    "ListLegsResponseEmbedded": ".list_legs_response_embedded",
    "ListLegsResponseEmbeddedLegsItem": ".list_legs_response_embedded_legs_item",
    "ListLegsResponseLinks": ".list_legs_response_links",
    "ListLegsResponseLinksSelf": ".list_legs_response_links_self",
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
    "ListLegsResponse",
    "ListLegsResponseEmbedded",
    "ListLegsResponseEmbeddedLegsItem",
    "ListLegsResponseLinks",
    "ListLegsResponseLinksSelf",
]

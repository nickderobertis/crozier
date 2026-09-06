



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_redirects_response import CreateRedirectsResponse
    from .delete_redirects_response import DeleteRedirectsResponse
    from .delete_redirects_response_pagination import DeleteRedirectsResponsePagination
    from .delete_redirects_response_redirects_item import DeleteRedirectsResponseRedirectsItem
    from .list_redirects_response import ListRedirectsResponse
    from .list_redirects_response_pagination import ListRedirectsResponsePagination
    from .list_redirects_response_redirects_item import ListRedirectsResponseRedirectsItem
    from .update_redirects_response import UpdateRedirectsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateRedirectsResponse": ".create_redirects_response",
    "DeleteRedirectsResponse": ".delete_redirects_response",
    "DeleteRedirectsResponsePagination": ".delete_redirects_response_pagination",
    "DeleteRedirectsResponseRedirectsItem": ".delete_redirects_response_redirects_item",
    "ListRedirectsResponse": ".list_redirects_response",
    "ListRedirectsResponsePagination": ".list_redirects_response_pagination",
    "ListRedirectsResponseRedirectsItem": ".list_redirects_response_redirects_item",
    "UpdateRedirectsResponse": ".update_redirects_response",
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
    "CreateRedirectsResponse",
    "DeleteRedirectsResponse",
    "DeleteRedirectsResponsePagination",
    "DeleteRedirectsResponseRedirectsItem",
    "ListRedirectsResponse",
    "ListRedirectsResponsePagination",
    "ListRedirectsResponseRedirectsItem",
    "UpdateRedirectsResponse",
]

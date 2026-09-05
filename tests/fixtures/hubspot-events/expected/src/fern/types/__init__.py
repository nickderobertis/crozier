



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .collection_response_external_unified_event import CollectionResponseExternalUnifiedEvent
    from .error import Error
    from .error_detail import ErrorDetail
    from .external_unified_event import ExternalUnifiedEvent
    from .next_page import NextPage
    from .oauth_scope import OauthScope
    from .paging import Paging
    from .previous_page import PreviousPage
_dynamic_imports: typing.Dict[str, str] = {
    "CollectionResponseExternalUnifiedEvent": ".collection_response_external_unified_event",
    "Error": ".error",
    "ErrorDetail": ".error_detail",
    "ExternalUnifiedEvent": ".external_unified_event",
    "NextPage": ".next_page",
    "OauthScope": ".oauth_scope",
    "Paging": ".paging",
    "PreviousPage": ".previous_page",
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
    "CollectionResponseExternalUnifiedEvent",
    "Error",
    "ErrorDetail",
    "ExternalUnifiedEvent",
    "NextPage",
    "OauthScope",
    "Paging",
    "PreviousPage",
]

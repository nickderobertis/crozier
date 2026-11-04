



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetAffectedAgentsResponse,
        GetAffectedAgentsResponseData,
        GetSessionDetailsResponse,
        GetSessionDetailsResponseData,
        ListThirdPartySessionsResponse,
        RefreshThirdPartySessionResponse,
        TerminateSessionResponse,
        TerminateSessionResponseData,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetAffectedAgentsResponse": ".types",
    "GetAffectedAgentsResponseData": ".types",
    "GetSessionDetailsResponse": ".types",
    "GetSessionDetailsResponseData": ".types",
    "ListThirdPartySessionsResponse": ".types",
    "RefreshThirdPartySessionResponse": ".types",
    "TerminateSessionResponse": ".types",
    "TerminateSessionResponseData": ".types",
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
    "GetAffectedAgentsResponse",
    "GetAffectedAgentsResponseData",
    "GetSessionDetailsResponse",
    "GetSessionDetailsResponseData",
    "ListThirdPartySessionsResponse",
    "RefreshThirdPartySessionResponse",
    "TerminateSessionResponse",
    "TerminateSessionResponseData",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .config_update_response import ConfigUpdateResponse
    from .config_update_response_reload_type import ConfigUpdateResponseReloadType
    from .log_search_match import LogSearchMatch
    from .log_search_response import LogSearchResponse
    from .log_tail_payload import LogTailPayload
    from .unauthorized_error_body import UnauthorizedErrorBody
_dynamic_imports: typing.Dict[str, str] = {
    "ConfigUpdateResponse": ".config_update_response",
    "ConfigUpdateResponseReloadType": ".config_update_response_reload_type",
    "LogSearchMatch": ".log_search_match",
    "LogSearchResponse": ".log_search_response",
    "LogTailPayload": ".log_tail_payload",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
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
    "ConfigUpdateResponse",
    "ConfigUpdateResponseReloadType",
    "LogSearchMatch",
    "LogSearchResponse",
    "LogTailPayload",
    "UnauthorizedErrorBody",
]

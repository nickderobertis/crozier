



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .logs_read_response import LogsReadResponse
    from .logs_read_response_attributes import LogsReadResponseAttributes
    from .logs_read_response_attributes_params import LogsReadResponseAttributesParams
    from .logs_read_response_links import LogsReadResponseLinks
    from .logs_read_response_relationships import LogsReadResponseRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "LogsReadResponse": ".logs_read_response",
    "LogsReadResponseAttributes": ".logs_read_response_attributes",
    "LogsReadResponseAttributesParams": ".logs_read_response_attributes_params",
    "LogsReadResponseLinks": ".logs_read_response_links",
    "LogsReadResponseRelationships": ".logs_read_response_relationships",
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
    "LogsReadResponse",
    "LogsReadResponseAttributes",
    "LogsReadResponseAttributesParams",
    "LogsReadResponseLinks",
    "LogsReadResponseRelationships",
]

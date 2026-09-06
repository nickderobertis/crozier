



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_scripts_response import ListScriptsResponse
    from .list_scripts_response_pagination import ListScriptsResponsePagination
    from .list_scripts_response_registered_scripts_item import ListScriptsResponseRegisteredScriptsItem
    from .register_hosted_scripts_response import RegisterHostedScriptsResponse
    from .register_inline_scripts_response import RegisterInlineScriptsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ListScriptsResponse": ".list_scripts_response",
    "ListScriptsResponsePagination": ".list_scripts_response_pagination",
    "ListScriptsResponseRegisteredScriptsItem": ".list_scripts_response_registered_scripts_item",
    "RegisterHostedScriptsResponse": ".register_hosted_scripts_response",
    "RegisterInlineScriptsResponse": ".register_inline_scripts_response",
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
    "ListScriptsResponse",
    "ListScriptsResponsePagination",
    "ListScriptsResponseRegisteredScriptsItem",
    "RegisterHostedScriptsResponse",
    "RegisterInlineScriptsResponse",
]

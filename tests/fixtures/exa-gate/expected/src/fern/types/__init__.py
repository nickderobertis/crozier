



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .key_batch_action import KeyBatchAction
    from .key_create import KeyCreate
    from .proxy_error import ProxyError
    from .proxy_error_error import ProxyErrorError
    from .proxy_error_error_type import ProxyErrorErrorType
_dynamic_imports: typing.Dict[str, str] = {
    "KeyBatchAction": ".key_batch_action",
    "KeyCreate": ".key_create",
    "ProxyError": ".proxy_error",
    "ProxyErrorError": ".proxy_error_error",
    "ProxyErrorErrorType": ".proxy_error_error_type",
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


__all__ = ["KeyBatchAction", "KeyCreate", "ProxyError", "ProxyErrorError", "ProxyErrorErrorType"]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .global_config_response import GlobalConfigResponse
    from .global_config_response_ai import GlobalConfigResponseAi
    from .global_config_response_observability import GlobalConfigResponseObservability
    from .global_config_response_observability_tianji import GlobalConfigResponseObservabilityTianji
_dynamic_imports: typing.Dict[str, str] = {
    "GlobalConfigResponse": ".global_config_response",
    "GlobalConfigResponseAi": ".global_config_response_ai",
    "GlobalConfigResponseObservability": ".global_config_response_observability",
    "GlobalConfigResponseObservabilityTianji": ".global_config_response_observability_tianji",
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
    "GlobalConfigResponse",
    "GlobalConfigResponseAi",
    "GlobalConfigResponseObservability",
    "GlobalConfigResponseObservabilityTianji",
]

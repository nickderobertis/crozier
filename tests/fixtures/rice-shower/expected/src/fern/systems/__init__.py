



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateSystemRequestHeatersItem,
        CreateSystemRequestThermosItem,
        CreateSystemResponse,
        CreateSystemResponseHeatersItem,
        CreateSystemResponseThermosItem,
        DeleteSystemResponse,
        GetSystemResponse,
        GetSystemResponseHeatersItem,
        GetSystemResponseThermosItem,
        ListSystemsResponseItem,
        ListSystemsResponseItemHeatersItem,
        ListSystemsResponseItemThermosItem,
        UpdateSystemRequestHeatersItem,
        UpdateSystemRequestThermosItem,
        UpdateSystemResponse,
        UpdateSystemResponseHeatersItem,
        UpdateSystemResponseThermosItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateSystemRequestHeatersItem": ".types",
    "CreateSystemRequestThermosItem": ".types",
    "CreateSystemResponse": ".types",
    "CreateSystemResponseHeatersItem": ".types",
    "CreateSystemResponseThermosItem": ".types",
    "DeleteSystemResponse": ".types",
    "GetSystemResponse": ".types",
    "GetSystemResponseHeatersItem": ".types",
    "GetSystemResponseThermosItem": ".types",
    "ListSystemsResponseItem": ".types",
    "ListSystemsResponseItemHeatersItem": ".types",
    "ListSystemsResponseItemThermosItem": ".types",
    "UpdateSystemRequestHeatersItem": ".types",
    "UpdateSystemRequestThermosItem": ".types",
    "UpdateSystemResponse": ".types",
    "UpdateSystemResponseHeatersItem": ".types",
    "UpdateSystemResponseThermosItem": ".types",
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
    "CreateSystemRequestHeatersItem",
    "CreateSystemRequestThermosItem",
    "CreateSystemResponse",
    "CreateSystemResponseHeatersItem",
    "CreateSystemResponseThermosItem",
    "DeleteSystemResponse",
    "GetSystemResponse",
    "GetSystemResponseHeatersItem",
    "GetSystemResponseThermosItem",
    "ListSystemsResponseItem",
    "ListSystemsResponseItemHeatersItem",
    "ListSystemsResponseItemThermosItem",
    "UpdateSystemRequestHeatersItem",
    "UpdateSystemRequestThermosItem",
    "UpdateSystemResponse",
    "UpdateSystemResponseHeatersItem",
    "UpdateSystemResponseThermosItem",
]

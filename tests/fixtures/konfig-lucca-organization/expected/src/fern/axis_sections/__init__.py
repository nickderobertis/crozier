



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Axis,
        AxisSection,
        GetApiV3AxesResponse,
        GetApiV3AxesResponseData,
        GetApiV3AxisSectionsAxisSectionIdResponse,
        GetApiV3AxissectionsResponse,
        GetApiV3AxissectionsResponseData,
        PostApiV3AxisSectionsResponse,
        PutApiV3AxisSectionsAxisSectionIdResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "Axis": ".types",
    "AxisSection": ".types",
    "GetApiV3AxesResponse": ".types",
    "GetApiV3AxesResponseData": ".types",
    "GetApiV3AxisSectionsAxisSectionIdResponse": ".types",
    "GetApiV3AxissectionsResponse": ".types",
    "GetApiV3AxissectionsResponseData": ".types",
    "PostApiV3AxisSectionsResponse": ".types",
    "PutApiV3AxisSectionsAxisSectionIdResponse": ".types",
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
    "Axis",
    "AxisSection",
    "GetApiV3AxesResponse",
    "GetApiV3AxesResponseData",
    "GetApiV3AxisSectionsAxisSectionIdResponse",
    "GetApiV3AxissectionsResponse",
    "GetApiV3AxissectionsResponseData",
    "PostApiV3AxisSectionsResponse",
    "PutApiV3AxisSectionsAxisSectionIdResponse",
]

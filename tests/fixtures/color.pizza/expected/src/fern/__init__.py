



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Color,
        ColorBase,
        ColorBaseHsl,
        ColorBaseLab,
        ColorBaseRgb,
        ColorBaseSwatchImg,
        ColorHsl,
        ColorLab,
        ColorRgb,
        Error,
        GetListsResponse,
        GetListsResponseListDescriptions,
        GetNamesResponse,
        GetResponse,
        ListDescription,
        PossibleLists,
    )
    from .errors import NotFoundError
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Color": ".types",
    "ColorBase": ".types",
    "ColorBaseHsl": ".types",
    "ColorBaseLab": ".types",
    "ColorBaseRgb": ".types",
    "ColorBaseSwatchImg": ".types",
    "ColorHsl": ".types",
    "ColorLab": ".types",
    "ColorRgb": ".types",
    "Error": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetListsResponse": ".types",
    "GetListsResponseListDescriptions": ".types",
    "GetNamesResponse": ".types",
    "GetResponse": ".types",
    "ListDescription": ".types",
    "NotFoundError": ".errors",
    "PossibleLists": ".types",
    "__version__": ".version",
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
    "AsyncFernApi",
    "Color",
    "ColorBase",
    "ColorBaseHsl",
    "ColorBaseLab",
    "ColorBaseRgb",
    "ColorBaseSwatchImg",
    "ColorHsl",
    "ColorLab",
    "ColorRgb",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "GetListsResponse",
    "GetListsResponseListDescriptions",
    "GetNamesResponse",
    "GetResponse",
    "ListDescription",
    "NotFoundError",
    "PossibleLists",
    "__version__",
]

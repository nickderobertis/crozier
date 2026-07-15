



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .color import Color
    from .color_base import ColorBase
    from .color_base_hsl import ColorBaseHsl
    from .color_base_lab import ColorBaseLab
    from .color_base_rgb import ColorBaseRgb
    from .color_base_swatch_img import ColorBaseSwatchImg
    from .color_hsl import ColorHsl
    from .color_lab import ColorLab
    from .color_rgb import ColorRgb
    from .error import Error
    from .get_lists_response import GetListsResponse
    from .get_lists_response_list_descriptions import GetListsResponseListDescriptions
    from .get_names_response import GetNamesResponse
    from .get_response import GetResponse
    from .list_description import ListDescription
    from .possible_lists import PossibleLists
_dynamic_imports: typing.Dict[str, str] = {
    "Color": ".color",
    "ColorBase": ".color_base",
    "ColorBaseHsl": ".color_base_hsl",
    "ColorBaseLab": ".color_base_lab",
    "ColorBaseRgb": ".color_base_rgb",
    "ColorBaseSwatchImg": ".color_base_swatch_img",
    "ColorHsl": ".color_hsl",
    "ColorLab": ".color_lab",
    "ColorRgb": ".color_rgb",
    "Error": ".error",
    "GetListsResponse": ".get_lists_response",
    "GetListsResponseListDescriptions": ".get_lists_response_list_descriptions",
    "GetNamesResponse": ".get_names_response",
    "GetResponse": ".get_response",
    "ListDescription": ".list_description",
    "PossibleLists": ".possible_lists",
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
    "GetListsResponse",
    "GetListsResponseListDescriptions",
    "GetNamesResponse",
    "GetResponse",
    "ListDescription",
    "PossibleLists",
]

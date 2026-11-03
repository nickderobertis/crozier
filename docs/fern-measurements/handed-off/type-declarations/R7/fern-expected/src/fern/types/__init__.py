



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_tile_v2tiles_coastal_zxy_pbf_get_request_shading import GetTileV2TilesCoastalZxyPbfGetRequestShading
    from .get_tile_v2tiles_coastal_zxy_pbf_get_response import GetTileV2TilesCoastalZxyPbfGetResponse
    from .read_abcd_tile_request_palette import ReadAbcdTileRequestPalette
    from .read_abcd_tile_response import ReadAbcdTileResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetTileV2TilesCoastalZxyPbfGetRequestShading": ".get_tile_v2tiles_coastal_zxy_pbf_get_request_shading",
    "GetTileV2TilesCoastalZxyPbfGetResponse": ".get_tile_v2tiles_coastal_zxy_pbf_get_response",
    "ReadAbcdTileRequestPalette": ".read_abcd_tile_request_palette",
    "ReadAbcdTileResponse": ".read_abcd_tile_response",
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
    "GetTileV2TilesCoastalZxyPbfGetRequestShading",
    "GetTileV2TilesCoastalZxyPbfGetResponse",
    "ReadAbcdTileRequestPalette",
    "ReadAbcdTileResponse",
]

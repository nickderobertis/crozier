



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .buoy import Buoy
    from .buoys_by_station import BuoysByStation
    from .depth import Depth
    from .depths_by_station import DepthsByStation
    from .soundings_by_station import SoundingsByStation
    from .soundings_by_station_value import SoundingsByStationValue
    from .station_board import StationBoard
    from .tide_grid import TideGrid
    from .tide_grid_item_item_value import TideGridItemItemValue
    from .tide_grid_item_item_value_trend import TideGridItemItemValueTrend
_dynamic_imports: typing.Dict[str, str] = {
    "Buoy": ".buoy",
    "BuoysByStation": ".buoys_by_station",
    "Depth": ".depth",
    "DepthsByStation": ".depths_by_station",
    "SoundingsByStation": ".soundings_by_station",
    "SoundingsByStationValue": ".soundings_by_station_value",
    "StationBoard": ".station_board",
    "TideGrid": ".tide_grid",
    "TideGridItemItemValue": ".tide_grid_item_item_value",
    "TideGridItemItemValueTrend": ".tide_grid_item_item_value_trend",
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
    "Buoy",
    "BuoysByStation",
    "Depth",
    "DepthsByStation",
    "SoundingsByStation",
    "SoundingsByStationValue",
    "StationBoard",
    "TideGrid",
    "TideGridItemItemValue",
    "TideGridItemItemValueTrend",
]

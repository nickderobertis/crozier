



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .creature_sighting import CreatureSighting
    from .depth_centimetres import DepthCentimetres
    from .gauge_reading import GaugeReading
    from .survey_entry import SurveyEntry, SurveyEntry_Level, SurveyEntry_Sighting
    from .water_level import WaterLevel
_dynamic_imports: typing.Dict[str, str] = {
    "CreatureSighting": ".creature_sighting",
    "DepthCentimetres": ".depth_centimetres",
    "GaugeReading": ".gauge_reading",
    "SurveyEntry": ".survey_entry",
    "SurveyEntry_Level": ".survey_entry",
    "SurveyEntry_Sighting": ".survey_entry",
    "WaterLevel": ".water_level",
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
    "CreatureSighting",
    "DepthCentimetres",
    "GaugeReading",
    "SurveyEntry",
    "SurveyEntry_Level",
    "SurveyEntry_Sighting",
    "WaterLevel",
]

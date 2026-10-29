



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .camera import Camera
    from .comet_reading import CometReading
    from .instrument import Instrument, Instrument_Camera, Instrument_Telescope
    from .logbook import Logbook
    from .meteor_reading import MeteorReading
    from .meteor_reading_kind import MeteorReadingKind
    from .reading import Reading, Reading_Comet, Reading_Meteor, Reading_Star
    from .star_reading import StarReading
    from .star_reading_kind import StarReadingKind
    from .telescope import Telescope
    from .trail import Trail
_dynamic_imports: typing.Dict[str, str] = {
    "Camera": ".camera",
    "CometReading": ".comet_reading",
    "Instrument": ".instrument",
    "Instrument_Camera": ".instrument",
    "Instrument_Telescope": ".instrument",
    "Logbook": ".logbook",
    "MeteorReading": ".meteor_reading",
    "MeteorReadingKind": ".meteor_reading_kind",
    "Reading": ".reading",
    "Reading_Comet": ".reading",
    "Reading_Meteor": ".reading",
    "Reading_Star": ".reading",
    "StarReading": ".star_reading",
    "StarReadingKind": ".star_reading_kind",
    "Telescope": ".telescope",
    "Trail": ".trail",
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
    "Camera",
    "CometReading",
    "Instrument",
    "Instrument_Camera",
    "Instrument_Telescope",
    "Logbook",
    "MeteorReading",
    "MeteorReadingKind",
    "Reading",
    "Reading_Comet",
    "Reading_Meteor",
    "Reading_Star",
    "StarReading",
    "StarReadingKind",
    "Telescope",
    "Trail",
]

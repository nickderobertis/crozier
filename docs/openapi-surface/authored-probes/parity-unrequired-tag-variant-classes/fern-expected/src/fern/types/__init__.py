



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .imager import Imager
    from .observatory import Observatory
    from .observatory_instruments_item import (
        ObservatoryInstrumentsItem,
        ObservatoryInstrumentsItem_Imaging,
        ObservatoryInstrumentsItem_Spectroscopy,
    )
    from .reflector import Reflector
    from .refractor import Refractor
    from .spectrograph import Spectrograph
    from .telescope import Telescope, Telescope_Reflector, Telescope_Refractor
_dynamic_imports: typing.Dict[str, str] = {
    "Imager": ".imager",
    "Observatory": ".observatory",
    "ObservatoryInstrumentsItem": ".observatory_instruments_item",
    "ObservatoryInstrumentsItem_Imaging": ".observatory_instruments_item",
    "ObservatoryInstrumentsItem_Spectroscopy": ".observatory_instruments_item",
    "Reflector": ".reflector",
    "Refractor": ".refractor",
    "Spectrograph": ".spectrograph",
    "Telescope": ".telescope",
    "Telescope_Reflector": ".telescope",
    "Telescope_Refractor": ".telescope",
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
    "Imager",
    "Observatory",
    "ObservatoryInstrumentsItem",
    "ObservatoryInstrumentsItem_Imaging",
    "ObservatoryInstrumentsItem_Spectroscopy",
    "Reflector",
    "Refractor",
    "Spectrograph",
    "Telescope",
    "Telescope_Reflector",
    "Telescope_Refractor",
]

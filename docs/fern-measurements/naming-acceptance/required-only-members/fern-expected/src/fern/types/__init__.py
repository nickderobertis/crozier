



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .harvest import Harvest
    from .harvest_base import HarvestBase
    from .harvest_target import HarvestTarget
    from .packet_base import PacketBase
    from .packet_create import PacketCreate
    from .packet_for_create import PacketForCreate
    from .sample_base import SampleBase
    from .shelf import Shelf
    from .shelf_samples_item import ShelfSamplesItem
    from .storage_target import StorageTarget
    from .trial_create import TrialCreate
_dynamic_imports: typing.Dict[str, str] = {
    "Harvest": ".harvest",
    "HarvestBase": ".harvest_base",
    "HarvestTarget": ".harvest_target",
    "PacketBase": ".packet_base",
    "PacketCreate": ".packet_create",
    "PacketForCreate": ".packet_for_create",
    "SampleBase": ".sample_base",
    "Shelf": ".shelf",
    "ShelfSamplesItem": ".shelf_samples_item",
    "StorageTarget": ".storage_target",
    "TrialCreate": ".trial_create",
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
    "Harvest",
    "HarvestBase",
    "HarvestTarget",
    "PacketBase",
    "PacketCreate",
    "PacketForCreate",
    "SampleBase",
    "Shelf",
    "ShelfSamplesItem",
    "StorageTarget",
    "TrialCreate",
]

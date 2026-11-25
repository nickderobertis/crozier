



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        FlowSensor,
        LevelSensor,
        Lock,
        LockCrew,
        LockCrew_Lockkeeper,
        LockCrew_Volunteer,
        LockGate,
        LockGate_Slide,
        LockGate_Swing,
        LockPaddle,
        LockRelief,
        LockRelief_Volunteer,
        LockSensor,
        LockSensor_Flow,
        LockSensor_LevelDownstream,
        LockSensor_LevelUpstream,
        Lockkeeper,
        LockkeeperRole,
        ManualPaddle,
        ManualPaddleDrive,
        PoweredPaddle,
        PoweredPaddleDrive,
        SlideGate,
        SwingGate,
        Volunteer,
    )
    from . import locks
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FlowSensor": ".types",
    "LevelSensor": ".types",
    "Lock": ".types",
    "LockCrew": ".types",
    "LockCrew_Lockkeeper": ".types",
    "LockCrew_Volunteer": ".types",
    "LockGate": ".types",
    "LockGate_Slide": ".types",
    "LockGate_Swing": ".types",
    "LockPaddle": ".types",
    "LockRelief": ".types",
    "LockRelief_Volunteer": ".types",
    "LockSensor": ".types",
    "LockSensor_Flow": ".types",
    "LockSensor_LevelDownstream": ".types",
    "LockSensor_LevelUpstream": ".types",
    "Lockkeeper": ".types",
    "LockkeeperRole": ".types",
    "ManualPaddle": ".types",
    "ManualPaddleDrive": ".types",
    "PoweredPaddle": ".types",
    "PoweredPaddleDrive": ".types",
    "SlideGate": ".types",
    "SwingGate": ".types",
    "Volunteer": ".types",
    "__version__": ".version",
    "locks": ".locks",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FlowSensor",
    "LevelSensor",
    "Lock",
    "LockCrew",
    "LockCrew_Lockkeeper",
    "LockCrew_Volunteer",
    "LockGate",
    "LockGate_Slide",
    "LockGate_Swing",
    "LockPaddle",
    "LockRelief",
    "LockRelief_Volunteer",
    "LockSensor",
    "LockSensor_Flow",
    "LockSensor_LevelDownstream",
    "LockSensor_LevelUpstream",
    "Lockkeeper",
    "LockkeeperRole",
    "ManualPaddle",
    "ManualPaddleDrive",
    "PoweredPaddle",
    "PoweredPaddleDrive",
    "SlideGate",
    "SwingGate",
    "Volunteer",
    "__version__",
    "locks",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .flow_sensor import FlowSensor
    from .level_sensor import LevelSensor
    from .lock import Lock
    from .lock_crew import LockCrew, LockCrew_Lockkeeper, LockCrew_Volunteer
    from .lock_gate import LockGate, LockGate_Slide, LockGate_Swing
    from .lock_paddle import LockPaddle
    from .lock_relief import LockRelief, LockRelief_Volunteer
    from .lock_sensor import LockSensor, LockSensor_Flow, LockSensor_LevelDownstream, LockSensor_LevelUpstream
    from .lockkeeper import Lockkeeper
    from .lockkeeper_role import LockkeeperRole
    from .manual_paddle import ManualPaddle
    from .manual_paddle_drive import ManualPaddleDrive
    from .powered_paddle import PoweredPaddle
    from .powered_paddle_drive import PoweredPaddleDrive
    from .slide_gate import SlideGate
    from .swing_gate import SwingGate
    from .volunteer import Volunteer
_dynamic_imports: typing.Dict[str, str] = {
    "FlowSensor": ".flow_sensor",
    "LevelSensor": ".level_sensor",
    "Lock": ".lock",
    "LockCrew": ".lock_crew",
    "LockCrew_Lockkeeper": ".lock_crew",
    "LockCrew_Volunteer": ".lock_crew",
    "LockGate": ".lock_gate",
    "LockGate_Slide": ".lock_gate",
    "LockGate_Swing": ".lock_gate",
    "LockPaddle": ".lock_paddle",
    "LockRelief": ".lock_relief",
    "LockRelief_Volunteer": ".lock_relief",
    "LockSensor": ".lock_sensor",
    "LockSensor_Flow": ".lock_sensor",
    "LockSensor_LevelDownstream": ".lock_sensor",
    "LockSensor_LevelUpstream": ".lock_sensor",
    "Lockkeeper": ".lockkeeper",
    "LockkeeperRole": ".lockkeeper_role",
    "ManualPaddle": ".manual_paddle",
    "ManualPaddleDrive": ".manual_paddle_drive",
    "PoweredPaddle": ".powered_paddle",
    "PoweredPaddleDrive": ".powered_paddle_drive",
    "SlideGate": ".slide_gate",
    "SwingGate": ".swing_gate",
    "Volunteer": ".volunteer",
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
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .alarm import Alarm
    from .alarm_base import AlarmBase
    from .manual_trigger import ManualTrigger
    from .receipt import Receipt
    from .surge_alarm import SurgeAlarm
    from .tide_trigger import TideTrigger
    from .trigger import Trigger
    from .wind_trigger import WindTrigger
_dynamic_imports: typing.Dict[str, str] = {
    "Alarm": ".alarm",
    "AlarmBase": ".alarm_base",
    "ManualTrigger": ".manual_trigger",
    "Receipt": ".receipt",
    "SurgeAlarm": ".surge_alarm",
    "TideTrigger": ".tide_trigger",
    "Trigger": ".trigger",
    "WindTrigger": ".wind_trigger",
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


__all__ = ["Alarm", "AlarmBase", "ManualTrigger", "Receipt", "SurgeAlarm", "TideTrigger", "Trigger", "WindTrigger"]

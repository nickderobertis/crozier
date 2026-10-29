



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .calibrated import Calibrated
    from .gauge import Gauge
    from .humidity_sensor import HumiditySensor
    from .named import Named
    from .plain_gauge import PlainGauge
    from .rain_sensor import RainSensor
    from .sensor import Sensor, Sensor_Humidity, Sensor_Rain, Sensor_Thermo, Sensor_Wind
    from .thermo_sensor import ThermoSensor
    from .vane_gauge import VaneGauge
    from .wind_sensor import WindSensor
_dynamic_imports: typing.Dict[str, str] = {
    "Calibrated": ".calibrated",
    "Gauge": ".gauge",
    "HumiditySensor": ".humidity_sensor",
    "Named": ".named",
    "PlainGauge": ".plain_gauge",
    "RainSensor": ".rain_sensor",
    "Sensor": ".sensor",
    "Sensor_Humidity": ".sensor",
    "Sensor_Rain": ".sensor",
    "Sensor_Thermo": ".sensor",
    "Sensor_Wind": ".sensor",
    "ThermoSensor": ".thermo_sensor",
    "VaneGauge": ".vane_gauge",
    "WindSensor": ".wind_sensor",
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
    "Calibrated",
    "Gauge",
    "HumiditySensor",
    "Named",
    "PlainGauge",
    "RainSensor",
    "Sensor",
    "Sensor_Humidity",
    "Sensor_Rain",
    "Sensor_Thermo",
    "Sensor_Wind",
    "ThermoSensor",
    "VaneGauge",
    "WindSensor",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .board import Board
    from .forecast_reading import ForecastReading
    from .panel import Panel
    from .panel_reading import PanelReading, PanelReading_Forecast, PanelReading_Sensors
    from .sensor_reading import SensorReading
    from .sensor_reading_bench import SensorReadingBench
    from .sensor_reading_channels_item import SensorReadingChannelsItem
    from .sensor_reading_checks_item import (
        SensorReadingChecksItem,
        SensorReadingChecksItem_Threshold,
        SensorReadingChecksItem_Trend,
    )
    from .threshold_check import ThresholdCheck
    from .trend_check import TrendCheck
    from .window import Window
_dynamic_imports: typing.Dict[str, str] = {
    "Board": ".board",
    "ForecastReading": ".forecast_reading",
    "Panel": ".panel",
    "PanelReading": ".panel_reading",
    "PanelReading_Forecast": ".panel_reading",
    "PanelReading_Sensors": ".panel_reading",
    "SensorReading": ".sensor_reading",
    "SensorReadingBench": ".sensor_reading_bench",
    "SensorReadingChannelsItem": ".sensor_reading_channels_item",
    "SensorReadingChecksItem": ".sensor_reading_checks_item",
    "SensorReadingChecksItem_Threshold": ".sensor_reading_checks_item",
    "SensorReadingChecksItem_Trend": ".sensor_reading_checks_item",
    "ThresholdCheck": ".threshold_check",
    "TrendCheck": ".trend_check",
    "Window": ".window",
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
    "Board",
    "ForecastReading",
    "Panel",
    "PanelReading",
    "PanelReading_Forecast",
    "PanelReading_Sensors",
    "SensorReading",
    "SensorReadingBench",
    "SensorReadingChannelsItem",
    "SensorReadingChecksItem",
    "SensorReadingChecksItem_Threshold",
    "SensorReadingChecksItem_Trend",
    "ThresholdCheck",
    "TrendCheck",
    "Window",
]

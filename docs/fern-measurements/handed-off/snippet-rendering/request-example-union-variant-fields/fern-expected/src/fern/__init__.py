



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Board,
        ForecastReading,
        Panel,
        PanelReading,
        PanelReading_Forecast,
        PanelReading_Sensors,
        SensorReading,
        SensorReadingBench,
        SensorReadingChannelsItem,
        SensorReadingChecksItem,
        SensorReadingChecksItem_Threshold,
        SensorReadingChecksItem_Trend,
        ThresholdCheck,
        TrendCheck,
        Window,
    )
    from . import boards
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Board": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForecastReading": ".types",
    "Panel": ".types",
    "PanelReading": ".types",
    "PanelReading_Forecast": ".types",
    "PanelReading_Sensors": ".types",
    "SensorReading": ".types",
    "SensorReadingBench": ".types",
    "SensorReadingChannelsItem": ".types",
    "SensorReadingChecksItem": ".types",
    "SensorReadingChecksItem_Threshold": ".types",
    "SensorReadingChecksItem_Trend": ".types",
    "ThresholdCheck": ".types",
    "TrendCheck": ".types",
    "Window": ".types",
    "__version__": ".version",
    "boards": ".boards",
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
    "Board",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
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
    "__version__",
    "boards",
]

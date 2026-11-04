



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AlertOperator,
        AutumnSeason,
        AutumnSeasonPhase,
        BenchAlert,
        BenchAlertLevels,
        BenchAlertLevelsTarget,
        BenchAlertOne,
        BenchAlertOneTarget,
        Board,
        ForecastReading,
        Panel,
        PanelReading,
        PanelReading_Forecast,
        PanelReading_Sensors,
        SensorReading,
        SensorReadingAlertsItem,
        SensorReadingAlertsItemBench,
        SensorReadingAlertsItemVent,
        SensorReadingAlertsItem_Bench,
        SensorReadingAlertsItem_Vent,
        SensorReadingBench,
        SensorReadingChannelsItem,
        SensorReadingChecksItem,
        SensorReadingChecksItem_Threshold,
        SensorReadingChecksItem_Trend,
        SensorReadingSeason,
        SensorReadingSeason_Autumn,
        SensorReadingSeason_Spring,
        SpringSeason,
        SpringSeasonPhase,
        ThresholdCheck,
        TrendCheck,
        VentAlert,
        VentAlertLevels,
        VentAlertLevelsTarget,
        VentAlertOne,
        VentAlertOneTarget,
        Window,
    )
    from . import boards
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AlertOperator": ".types",
    "AsyncFernApi": ".client",
    "AutumnSeason": ".types",
    "AutumnSeasonPhase": ".types",
    "BenchAlert": ".types",
    "BenchAlertLevels": ".types",
    "BenchAlertLevelsTarget": ".types",
    "BenchAlertOne": ".types",
    "BenchAlertOneTarget": ".types",
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
    "SensorReadingAlertsItem": ".types",
    "SensorReadingAlertsItemBench": ".types",
    "SensorReadingAlertsItemVent": ".types",
    "SensorReadingAlertsItem_Bench": ".types",
    "SensorReadingAlertsItem_Vent": ".types",
    "SensorReadingBench": ".types",
    "SensorReadingChannelsItem": ".types",
    "SensorReadingChecksItem": ".types",
    "SensorReadingChecksItem_Threshold": ".types",
    "SensorReadingChecksItem_Trend": ".types",
    "SensorReadingSeason": ".types",
    "SensorReadingSeason_Autumn": ".types",
    "SensorReadingSeason_Spring": ".types",
    "SpringSeason": ".types",
    "SpringSeasonPhase": ".types",
    "ThresholdCheck": ".types",
    "TrendCheck": ".types",
    "VentAlert": ".types",
    "VentAlertLevels": ".types",
    "VentAlertLevelsTarget": ".types",
    "VentAlertOne": ".types",
    "VentAlertOneTarget": ".types",
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
    "AlertOperator",
    "AsyncFernApi",
    "AutumnSeason",
    "AutumnSeasonPhase",
    "BenchAlert",
    "BenchAlertLevels",
    "BenchAlertLevelsTarget",
    "BenchAlertOne",
    "BenchAlertOneTarget",
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
    "SensorReadingAlertsItem",
    "SensorReadingAlertsItemBench",
    "SensorReadingAlertsItemVent",
    "SensorReadingAlertsItem_Bench",
    "SensorReadingAlertsItem_Vent",
    "SensorReadingBench",
    "SensorReadingChannelsItem",
    "SensorReadingChecksItem",
    "SensorReadingChecksItem_Threshold",
    "SensorReadingChecksItem_Trend",
    "SensorReadingSeason",
    "SensorReadingSeason_Autumn",
    "SensorReadingSeason_Spring",
    "SpringSeason",
    "SpringSeasonPhase",
    "ThresholdCheck",
    "TrendCheck",
    "VentAlert",
    "VentAlertLevels",
    "VentAlertLevelsTarget",
    "VentAlertOne",
    "VentAlertOneTarget",
    "Window",
    "__version__",
    "boards",
]

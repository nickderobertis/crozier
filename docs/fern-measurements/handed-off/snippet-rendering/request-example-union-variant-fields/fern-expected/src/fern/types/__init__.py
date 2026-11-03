



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .alert_operator import AlertOperator
    from .autumn_season import AutumnSeason
    from .autumn_season_phase import AutumnSeasonPhase
    from .bench_alert import BenchAlert
    from .bench_alert_levels import BenchAlertLevels
    from .bench_alert_levels_target import BenchAlertLevelsTarget
    from .bench_alert_one import BenchAlertOne
    from .bench_alert_one_target import BenchAlertOneTarget
    from .board import Board
    from .forecast_reading import ForecastReading
    from .panel import Panel
    from .panel_reading import PanelReading, PanelReading_Forecast, PanelReading_Sensors
    from .sensor_reading import SensorReading
    from .sensor_reading_alerts_item import (
        SensorReadingAlertsItem,
        SensorReadingAlertsItem_Bench,
        SensorReadingAlertsItem_Vent,
    )
    from .sensor_reading_alerts_item_bench import SensorReadingAlertsItemBench
    from .sensor_reading_alerts_item_vent import SensorReadingAlertsItemVent
    from .sensor_reading_bench import SensorReadingBench
    from .sensor_reading_channels_item import SensorReadingChannelsItem
    from .sensor_reading_checks_item import (
        SensorReadingChecksItem,
        SensorReadingChecksItem_Threshold,
        SensorReadingChecksItem_Trend,
    )
    from .sensor_reading_season import SensorReadingSeason, SensorReadingSeason_Autumn, SensorReadingSeason_Spring
    from .spring_season import SpringSeason
    from .spring_season_phase import SpringSeasonPhase
    from .threshold_check import ThresholdCheck
    from .trend_check import TrendCheck
    from .vent_alert import VentAlert
    from .vent_alert_levels import VentAlertLevels
    from .vent_alert_levels_target import VentAlertLevelsTarget
    from .vent_alert_one import VentAlertOne
    from .vent_alert_one_target import VentAlertOneTarget
    from .window import Window
_dynamic_imports: typing.Dict[str, str] = {
    "AlertOperator": ".alert_operator",
    "AutumnSeason": ".autumn_season",
    "AutumnSeasonPhase": ".autumn_season_phase",
    "BenchAlert": ".bench_alert",
    "BenchAlertLevels": ".bench_alert_levels",
    "BenchAlertLevelsTarget": ".bench_alert_levels_target",
    "BenchAlertOne": ".bench_alert_one",
    "BenchAlertOneTarget": ".bench_alert_one_target",
    "Board": ".board",
    "ForecastReading": ".forecast_reading",
    "Panel": ".panel",
    "PanelReading": ".panel_reading",
    "PanelReading_Forecast": ".panel_reading",
    "PanelReading_Sensors": ".panel_reading",
    "SensorReading": ".sensor_reading",
    "SensorReadingAlertsItem": ".sensor_reading_alerts_item",
    "SensorReadingAlertsItemBench": ".sensor_reading_alerts_item_bench",
    "SensorReadingAlertsItemVent": ".sensor_reading_alerts_item_vent",
    "SensorReadingAlertsItem_Bench": ".sensor_reading_alerts_item",
    "SensorReadingAlertsItem_Vent": ".sensor_reading_alerts_item",
    "SensorReadingBench": ".sensor_reading_bench",
    "SensorReadingChannelsItem": ".sensor_reading_channels_item",
    "SensorReadingChecksItem": ".sensor_reading_checks_item",
    "SensorReadingChecksItem_Threshold": ".sensor_reading_checks_item",
    "SensorReadingChecksItem_Trend": ".sensor_reading_checks_item",
    "SensorReadingSeason": ".sensor_reading_season",
    "SensorReadingSeason_Autumn": ".sensor_reading_season",
    "SensorReadingSeason_Spring": ".sensor_reading_season",
    "SpringSeason": ".spring_season",
    "SpringSeasonPhase": ".spring_season_phase",
    "ThresholdCheck": ".threshold_check",
    "TrendCheck": ".trend_check",
    "VentAlert": ".vent_alert",
    "VentAlertLevels": ".vent_alert_levels",
    "VentAlertLevelsTarget": ".vent_alert_levels_target",
    "VentAlertOne": ".vent_alert_one",
    "VentAlertOneTarget": ".vent_alert_one_target",
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
    "AlertOperator",
    "AutumnSeason",
    "AutumnSeasonPhase",
    "BenchAlert",
    "BenchAlertLevels",
    "BenchAlertLevelsTarget",
    "BenchAlertOne",
    "BenchAlertOneTarget",
    "Board",
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
]

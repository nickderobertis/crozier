



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_heater_metrics_request_time_end import GetHeaterMetricsRequestTimeEnd
    from .get_heater_metrics_request_time_start import GetHeaterMetricsRequestTimeStart
    from .get_heater_metrics_response import GetHeaterMetricsResponse
    from .get_heater_metrics_response_metrics_item import GetHeaterMetricsResponseMetricsItem
    from .get_heater_metrics_response_metrics_item_channels_item import GetHeaterMetricsResponseMetricsItemChannelsItem
    from .get_thermo_metrics_request_time_end import GetThermoMetricsRequestTimeEnd
    from .get_thermo_metrics_request_time_start import GetThermoMetricsRequestTimeStart
    from .get_thermo_metrics_response import GetThermoMetricsResponse
    from .get_thermo_metrics_response_metrics_item import GetThermoMetricsResponseMetricsItem
    from .get_thermo_metrics_response_metrics_item_channels_item import GetThermoMetricsResponseMetricsItemChannelsItem
_dynamic_imports: typing.Dict[str, str] = {
    "GetHeaterMetricsRequestTimeEnd": ".get_heater_metrics_request_time_end",
    "GetHeaterMetricsRequestTimeStart": ".get_heater_metrics_request_time_start",
    "GetHeaterMetricsResponse": ".get_heater_metrics_response",
    "GetHeaterMetricsResponseMetricsItem": ".get_heater_metrics_response_metrics_item",
    "GetHeaterMetricsResponseMetricsItemChannelsItem": ".get_heater_metrics_response_metrics_item_channels_item",
    "GetThermoMetricsRequestTimeEnd": ".get_thermo_metrics_request_time_end",
    "GetThermoMetricsRequestTimeStart": ".get_thermo_metrics_request_time_start",
    "GetThermoMetricsResponse": ".get_thermo_metrics_response",
    "GetThermoMetricsResponseMetricsItem": ".get_thermo_metrics_response_metrics_item",
    "GetThermoMetricsResponseMetricsItemChannelsItem": ".get_thermo_metrics_response_metrics_item_channels_item",
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
    "GetHeaterMetricsRequestTimeEnd",
    "GetHeaterMetricsRequestTimeStart",
    "GetHeaterMetricsResponse",
    "GetHeaterMetricsResponseMetricsItem",
    "GetHeaterMetricsResponseMetricsItemChannelsItem",
    "GetThermoMetricsRequestTimeEnd",
    "GetThermoMetricsRequestTimeStart",
    "GetThermoMetricsResponse",
    "GetThermoMetricsResponseMetricsItem",
    "GetThermoMetricsResponseMetricsItemChannelsItem",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_all_scrape_metrics_response_item import GetAllScrapeMetricsResponseItem
    from .get_all_scrape_metrics_response_item_heater import GetAllScrapeMetricsResponseItemHeater
    from .get_all_scrape_metrics_response_item_heater_error_count_item import (
        GetAllScrapeMetricsResponseItemHeaterErrorCountItem,
    )
    from .get_all_scrape_metrics_response_item_thermo import GetAllScrapeMetricsResponseItemThermo
    from .get_all_scrape_metrics_response_item_thermo_error_count_item import (
        GetAllScrapeMetricsResponseItemThermoErrorCountItem,
    )
    from .get_all_scrape_status_response_item import GetAllScrapeStatusResponseItem
    from .get_all_scrape_status_response_item_heater import GetAllScrapeStatusResponseItemHeater
    from .get_all_scrape_status_response_item_thermo import GetAllScrapeStatusResponseItemThermo
    from .get_system_scrape_metrics_response import GetSystemScrapeMetricsResponse
    from .get_system_scrape_metrics_response_heater import GetSystemScrapeMetricsResponseHeater
    from .get_system_scrape_metrics_response_heater_error_count_item import (
        GetSystemScrapeMetricsResponseHeaterErrorCountItem,
    )
    from .get_system_scrape_metrics_response_thermo import GetSystemScrapeMetricsResponseThermo
    from .get_system_scrape_metrics_response_thermo_error_count_item import (
        GetSystemScrapeMetricsResponseThermoErrorCountItem,
    )
    from .get_system_scrape_status_response import GetSystemScrapeStatusResponse
    from .get_system_scrape_status_response_heater import GetSystemScrapeStatusResponseHeater
    from .get_system_scrape_status_response_thermo import GetSystemScrapeStatusResponseThermo
_dynamic_imports: typing.Dict[str, str] = {
    "GetAllScrapeMetricsResponseItem": ".get_all_scrape_metrics_response_item",
    "GetAllScrapeMetricsResponseItemHeater": ".get_all_scrape_metrics_response_item_heater",
    "GetAllScrapeMetricsResponseItemHeaterErrorCountItem": ".get_all_scrape_metrics_response_item_heater_error_count_item",
    "GetAllScrapeMetricsResponseItemThermo": ".get_all_scrape_metrics_response_item_thermo",
    "GetAllScrapeMetricsResponseItemThermoErrorCountItem": ".get_all_scrape_metrics_response_item_thermo_error_count_item",
    "GetAllScrapeStatusResponseItem": ".get_all_scrape_status_response_item",
    "GetAllScrapeStatusResponseItemHeater": ".get_all_scrape_status_response_item_heater",
    "GetAllScrapeStatusResponseItemThermo": ".get_all_scrape_status_response_item_thermo",
    "GetSystemScrapeMetricsResponse": ".get_system_scrape_metrics_response",
    "GetSystemScrapeMetricsResponseHeater": ".get_system_scrape_metrics_response_heater",
    "GetSystemScrapeMetricsResponseHeaterErrorCountItem": ".get_system_scrape_metrics_response_heater_error_count_item",
    "GetSystemScrapeMetricsResponseThermo": ".get_system_scrape_metrics_response_thermo",
    "GetSystemScrapeMetricsResponseThermoErrorCountItem": ".get_system_scrape_metrics_response_thermo_error_count_item",
    "GetSystemScrapeStatusResponse": ".get_system_scrape_status_response",
    "GetSystemScrapeStatusResponseHeater": ".get_system_scrape_status_response_heater",
    "GetSystemScrapeStatusResponseThermo": ".get_system_scrape_status_response_thermo",
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
    "GetAllScrapeMetricsResponseItem",
    "GetAllScrapeMetricsResponseItemHeater",
    "GetAllScrapeMetricsResponseItemHeaterErrorCountItem",
    "GetAllScrapeMetricsResponseItemThermo",
    "GetAllScrapeMetricsResponseItemThermoErrorCountItem",
    "GetAllScrapeStatusResponseItem",
    "GetAllScrapeStatusResponseItemHeater",
    "GetAllScrapeStatusResponseItemThermo",
    "GetSystemScrapeMetricsResponse",
    "GetSystemScrapeMetricsResponseHeater",
    "GetSystemScrapeMetricsResponseHeaterErrorCountItem",
    "GetSystemScrapeMetricsResponseThermo",
    "GetSystemScrapeMetricsResponseThermoErrorCountItem",
    "GetSystemScrapeStatusResponse",
    "GetSystemScrapeStatusResponseHeater",
    "GetSystemScrapeStatusResponseThermo",
]

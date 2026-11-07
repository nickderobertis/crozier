



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .telemetry_all_response_item import TelemetryAllResponseItem
    from .telemetry_delete_response import TelemetryDeleteResponse
    from .telemetry_info_response import TelemetryInfoResponse
    from .telemetry_metrics_request_type import TelemetryMetricsRequestType
    from .telemetry_metrics_response_item import TelemetryMetricsResponseItem
    from .telemetry_pageviews_response import TelemetryPageviewsResponse
    from .telemetry_stats_response import TelemetryStatsResponse
    from .telemetry_stats_response_pageviews import TelemetryStatsResponsePageviews
    from .telemetry_stats_response_uniques import TelemetryStatsResponseUniques
    from .telemetry_upsert_response import TelemetryUpsertResponse
_dynamic_imports: typing.Dict[str, str] = {
    "TelemetryAllResponseItem": ".telemetry_all_response_item",
    "TelemetryDeleteResponse": ".telemetry_delete_response",
    "TelemetryInfoResponse": ".telemetry_info_response",
    "TelemetryMetricsRequestType": ".telemetry_metrics_request_type",
    "TelemetryMetricsResponseItem": ".telemetry_metrics_response_item",
    "TelemetryPageviewsResponse": ".telemetry_pageviews_response",
    "TelemetryStatsResponse": ".telemetry_stats_response",
    "TelemetryStatsResponsePageviews": ".telemetry_stats_response_pageviews",
    "TelemetryStatsResponseUniques": ".telemetry_stats_response_uniques",
    "TelemetryUpsertResponse": ".telemetry_upsert_response",
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
    "TelemetryAllResponseItem",
    "TelemetryDeleteResponse",
    "TelemetryInfoResponse",
    "TelemetryMetricsRequestType",
    "TelemetryMetricsResponseItem",
    "TelemetryPageviewsResponse",
    "TelemetryStatsResponse",
    "TelemetryStatsResponsePageviews",
    "TelemetryStatsResponseUniques",
    "TelemetryUpsertResponse",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .monitor_all_response_item import MonitorAllResponseItem
    from .monitor_all_response_item_notifications_item import MonitorAllResponseItemNotificationsItem
    from .monitor_change_active_response import MonitorChangeActiveResponse
    from .monitor_data_metrics_response import MonitorDataMetricsResponse
    from .monitor_data_response_item import MonitorDataResponseItem
    from .monitor_delete_response import MonitorDeleteResponse
    from .monitor_events_response_item import MonitorEventsResponseItem
    from .monitor_get_public_info_response_item import MonitorGetPublicInfoResponseItem
    from .monitor_get_response import MonitorGetResponse
    from .monitor_get_response_notifications_item import MonitorGetResponseNotificationsItem
    from .monitor_get_status_response import MonitorGetStatusResponse
    from .monitor_get_status_response_payload import MonitorGetStatusResponsePayload
    from .monitor_public_data_response_item import MonitorPublicDataResponseItem
    from .monitor_public_summary_response_item import MonitorPublicSummaryResponseItem
    from .monitor_recent_data_response_item import MonitorRecentDataResponseItem
    from .monitor_upsert_response import MonitorUpsertResponse
    from .server_status_public_info_response_value import ServerStatusPublicInfoResponseValue
_dynamic_imports: typing.Dict[str, str] = {
    "MonitorAllResponseItem": ".monitor_all_response_item",
    "MonitorAllResponseItemNotificationsItem": ".monitor_all_response_item_notifications_item",
    "MonitorChangeActiveResponse": ".monitor_change_active_response",
    "MonitorDataMetricsResponse": ".monitor_data_metrics_response",
    "MonitorDataResponseItem": ".monitor_data_response_item",
    "MonitorDeleteResponse": ".monitor_delete_response",
    "MonitorEventsResponseItem": ".monitor_events_response_item",
    "MonitorGetPublicInfoResponseItem": ".monitor_get_public_info_response_item",
    "MonitorGetResponse": ".monitor_get_response",
    "MonitorGetResponseNotificationsItem": ".monitor_get_response_notifications_item",
    "MonitorGetStatusResponse": ".monitor_get_status_response",
    "MonitorGetStatusResponsePayload": ".monitor_get_status_response_payload",
    "MonitorPublicDataResponseItem": ".monitor_public_data_response_item",
    "MonitorPublicSummaryResponseItem": ".monitor_public_summary_response_item",
    "MonitorRecentDataResponseItem": ".monitor_recent_data_response_item",
    "MonitorUpsertResponse": ".monitor_upsert_response",
    "ServerStatusPublicInfoResponseValue": ".server_status_public_info_response_value",
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
    "MonitorAllResponseItem",
    "MonitorAllResponseItemNotificationsItem",
    "MonitorChangeActiveResponse",
    "MonitorDataMetricsResponse",
    "MonitorDataResponseItem",
    "MonitorDeleteResponse",
    "MonitorEventsResponseItem",
    "MonitorGetPublicInfoResponseItem",
    "MonitorGetResponse",
    "MonitorGetResponseNotificationsItem",
    "MonitorGetStatusResponse",
    "MonitorGetStatusResponsePayload",
    "MonitorPublicDataResponseItem",
    "MonitorPublicSummaryResponseItem",
    "MonitorRecentDataResponseItem",
    "MonitorUpsertResponse",
    "ServerStatusPublicInfoResponseValue",
]

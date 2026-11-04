



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        MonitorAllResponseItem,
        MonitorAllResponseItemNotificationsItem,
        MonitorChangeActiveResponse,
        MonitorDataMetricsResponse,
        MonitorDataResponseItem,
        MonitorDeleteResponse,
        MonitorEventsResponseItem,
        MonitorGetPublicInfoResponseItem,
        MonitorGetResponse,
        MonitorGetResponseNotificationsItem,
        MonitorGetStatusResponse,
        MonitorGetStatusResponsePayload,
        MonitorPublicDataResponseItem,
        MonitorPublicSummaryResponseItem,
        MonitorRecentDataResponseItem,
        MonitorUpsertResponse,
        ServerStatusPublicInfoResponseValue,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "MonitorAllResponseItem": ".types",
    "MonitorAllResponseItemNotificationsItem": ".types",
    "MonitorChangeActiveResponse": ".types",
    "MonitorDataMetricsResponse": ".types",
    "MonitorDataResponseItem": ".types",
    "MonitorDeleteResponse": ".types",
    "MonitorEventsResponseItem": ".types",
    "MonitorGetPublicInfoResponseItem": ".types",
    "MonitorGetResponse": ".types",
    "MonitorGetResponseNotificationsItem": ".types",
    "MonitorGetStatusResponse": ".types",
    "MonitorGetStatusResponsePayload": ".types",
    "MonitorPublicDataResponseItem": ".types",
    "MonitorPublicSummaryResponseItem": ".types",
    "MonitorRecentDataResponseItem": ".types",
    "MonitorUpsertResponse": ".types",
    "ServerStatusPublicInfoResponseValue": ".types",
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

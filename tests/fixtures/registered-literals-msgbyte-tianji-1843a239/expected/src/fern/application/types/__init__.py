



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ai_gateway_create_response import AiGatewayCreateResponse
    from .application_all_response_item import ApplicationAllResponseItem
    from .application_create_response import ApplicationCreateResponse
    from .application_delete_response import ApplicationDeleteResponse
    from .application_event_stats_request_unit import ApplicationEventStatsRequestUnit
    from .application_event_stats_response import ApplicationEventStatsResponse
    from .application_event_stats_response_current_item import ApplicationEventStatsResponseCurrentItem
    from .application_event_stats_response_previous_item import ApplicationEventStatsResponsePreviousItem
    from .application_info_response import ApplicationInfoResponse
    from .application_info_response_application_store_infos_item import ApplicationInfoResponseApplicationStoreInfosItem
    from .application_store_app_search_request_store_type import ApplicationStoreAppSearchRequestStoreType
    from .application_store_app_search_response_item import ApplicationStoreAppSearchResponseItem
    from .application_store_info_history_request_store_type import ApplicationStoreInfoHistoryRequestStoreType
    from .application_store_info_history_response_item import ApplicationStoreInfoHistoryResponseItem
    from .application_update_response import ApplicationUpdateResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AiGatewayCreateResponse": ".ai_gateway_create_response",
    "ApplicationAllResponseItem": ".application_all_response_item",
    "ApplicationCreateResponse": ".application_create_response",
    "ApplicationDeleteResponse": ".application_delete_response",
    "ApplicationEventStatsRequestUnit": ".application_event_stats_request_unit",
    "ApplicationEventStatsResponse": ".application_event_stats_response",
    "ApplicationEventStatsResponseCurrentItem": ".application_event_stats_response_current_item",
    "ApplicationEventStatsResponsePreviousItem": ".application_event_stats_response_previous_item",
    "ApplicationInfoResponse": ".application_info_response",
    "ApplicationInfoResponseApplicationStoreInfosItem": ".application_info_response_application_store_infos_item",
    "ApplicationStoreAppSearchRequestStoreType": ".application_store_app_search_request_store_type",
    "ApplicationStoreAppSearchResponseItem": ".application_store_app_search_response_item",
    "ApplicationStoreInfoHistoryRequestStoreType": ".application_store_info_history_request_store_type",
    "ApplicationStoreInfoHistoryResponseItem": ".application_store_info_history_response_item",
    "ApplicationUpdateResponse": ".application_update_response",
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
    "AiGatewayCreateResponse",
    "ApplicationAllResponseItem",
    "ApplicationCreateResponse",
    "ApplicationDeleteResponse",
    "ApplicationEventStatsRequestUnit",
    "ApplicationEventStatsResponse",
    "ApplicationEventStatsResponseCurrentItem",
    "ApplicationEventStatsResponsePreviousItem",
    "ApplicationInfoResponse",
    "ApplicationInfoResponseApplicationStoreInfosItem",
    "ApplicationStoreAppSearchRequestStoreType",
    "ApplicationStoreAppSearchResponseItem",
    "ApplicationStoreInfoHistoryRequestStoreType",
    "ApplicationStoreInfoHistoryResponseItem",
    "ApplicationUpdateResponse",
]

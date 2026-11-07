



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .bad_request_error_body_extra import BadRequestErrorBodyExtra
    from .delete_request_event import DeleteRequestEvent
    from .delete_request_start import DeleteRequestStart
    from .download_request_event import DownloadRequestEvent
    from .download_request_start import DownloadRequestStart
    from .event_type import EventType
    from .head_download_request_event import HeadDownloadRequestEvent
    from .head_download_request_start import HeadDownloadRequestStart
    from .list_order import ListOrder
    from .list_request_after import ListRequestAfter
    from .list_request_before import ListRequestBefore
    from .list_request_event import ListRequestEvent
    from .list_request_limit import ListRequestLimit
    from .list_request_offset import ListRequestOffset
    from .list_request_order import ListRequestOrder
    from .list_response_results import ListResponseResults
    from .naive_datetime import NaiveDatetime
    from .not_found_error_body import NotFoundErrorBody
    from .not_found_error_body_extra import NotFoundErrorBodyExtra
    from .parameters import Parameters
    from .recording import Recording
    from .subscribe_request_types import SubscribeRequestTypes
    from .test_request_parameters import TestRequestParameters
    from .test_response_result import TestResponseResult
    from .upload_request_event import UploadRequestEvent
    from .upload_request_start import UploadRequestStart
    from .upload_request_type import UploadRequestType
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "BadRequestErrorBodyExtra": ".bad_request_error_body_extra",
    "DeleteRequestEvent": ".delete_request_event",
    "DeleteRequestStart": ".delete_request_start",
    "DownloadRequestEvent": ".download_request_event",
    "DownloadRequestStart": ".download_request_start",
    "EventType": ".event_type",
    "HeadDownloadRequestEvent": ".head_download_request_event",
    "HeadDownloadRequestStart": ".head_download_request_start",
    "ListOrder": ".list_order",
    "ListRequestAfter": ".list_request_after",
    "ListRequestBefore": ".list_request_before",
    "ListRequestEvent": ".list_request_event",
    "ListRequestLimit": ".list_request_limit",
    "ListRequestOffset": ".list_request_offset",
    "ListRequestOrder": ".list_request_order",
    "ListResponseResults": ".list_response_results",
    "NaiveDatetime": ".naive_datetime",
    "NotFoundErrorBody": ".not_found_error_body",
    "NotFoundErrorBodyExtra": ".not_found_error_body_extra",
    "Parameters": ".parameters",
    "Recording": ".recording",
    "SubscribeRequestTypes": ".subscribe_request_types",
    "TestRequestParameters": ".test_request_parameters",
    "TestResponseResult": ".test_response_result",
    "UploadRequestEvent": ".upload_request_event",
    "UploadRequestStart": ".upload_request_start",
    "UploadRequestType": ".upload_request_type",
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
    "BadRequestErrorBody",
    "BadRequestErrorBodyExtra",
    "DeleteRequestEvent",
    "DeleteRequestStart",
    "DownloadRequestEvent",
    "DownloadRequestStart",
    "EventType",
    "HeadDownloadRequestEvent",
    "HeadDownloadRequestStart",
    "ListOrder",
    "ListRequestAfter",
    "ListRequestBefore",
    "ListRequestEvent",
    "ListRequestLimit",
    "ListRequestOffset",
    "ListRequestOrder",
    "ListResponseResults",
    "NaiveDatetime",
    "NotFoundErrorBody",
    "NotFoundErrorBodyExtra",
    "Parameters",
    "Recording",
    "SubscribeRequestTypes",
    "TestRequestParameters",
    "TestResponseResult",
    "UploadRequestEvent",
    "UploadRequestStart",
    "UploadRequestType",
]

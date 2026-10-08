



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .base_request import BaseRequest
    from .base_response import BaseResponse
    from .cancel_error_response import CancelErrorResponse
    from .cancel_response import CancelResponse
    from .error_response import ErrorResponse
    from .msg_header_error_response import MsgHeaderErrorResponse
    from .msg_header_request import MsgHeaderRequest
    from .msg_header_response import MsgHeaderResponse
    from .report_response import ReportResponse
    from .report_response_jobs_item import ReportResponseJobsItem
    from .rest_response import RestResponse
    from .sms_inbox_response import SmsInboxResponse
    from .sms_inbox_response_messages_item import SmsInboxResponseMessagesItem
_dynamic_imports: typing.Dict[str, str] = {
    "BaseRequest": ".base_request",
    "BaseResponse": ".base_response",
    "CancelErrorResponse": ".cancel_error_response",
    "CancelResponse": ".cancel_response",
    "ErrorResponse": ".error_response",
    "MsgHeaderErrorResponse": ".msg_header_error_response",
    "MsgHeaderRequest": ".msg_header_request",
    "MsgHeaderResponse": ".msg_header_response",
    "ReportResponse": ".report_response",
    "ReportResponseJobsItem": ".report_response_jobs_item",
    "RestResponse": ".rest_response",
    "SmsInboxResponse": ".sms_inbox_response",
    "SmsInboxResponseMessagesItem": ".sms_inbox_response_messages_item",
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
    "BaseRequest",
    "BaseResponse",
    "CancelErrorResponse",
    "CancelResponse",
    "ErrorResponse",
    "MsgHeaderErrorResponse",
    "MsgHeaderRequest",
    "MsgHeaderResponse",
    "ReportResponse",
    "ReportResponseJobsItem",
    "RestResponse",
    "SmsInboxResponse",
    "SmsInboxResponseMessagesItem",
]

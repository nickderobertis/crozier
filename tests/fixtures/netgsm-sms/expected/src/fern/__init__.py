



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BaseRequest,
        BaseResponse,
        CancelErrorResponse,
        CancelResponse,
        ErrorResponse,
        MsgHeaderErrorResponse,
        MsgHeaderRequest,
        MsgHeaderResponse,
        ReportResponse,
        ReportResponseJobsItem,
        RestResponse,
        SmsInboxResponse,
        SmsInboxResponseMessagesItem,
    )
    from .errors import NotAcceptableError
    from . import bulk_sms, queries
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .bulk_sms import RestSendRequestMessagesItem
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BaseRequest": ".types",
    "BaseResponse": ".types",
    "CancelErrorResponse": ".types",
    "CancelResponse": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "MsgHeaderErrorResponse": ".types",
    "MsgHeaderRequest": ".types",
    "MsgHeaderResponse": ".types",
    "NotAcceptableError": ".errors",
    "ReportResponse": ".types",
    "ReportResponseJobsItem": ".types",
    "RestResponse": ".types",
    "RestSendRequestMessagesItem": ".bulk_sms",
    "SmsInboxResponse": ".types",
    "SmsInboxResponseMessagesItem": ".types",
    "__version__": ".version",
    "bulk_sms": ".bulk_sms",
    "queries": ".queries",
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
    "AsyncFernApi",
    "BaseRequest",
    "BaseResponse",
    "CancelErrorResponse",
    "CancelResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "FernApi",
    "FernApiEnvironment",
    "MsgHeaderErrorResponse",
    "MsgHeaderRequest",
    "MsgHeaderResponse",
    "NotAcceptableError",
    "ReportResponse",
    "ReportResponseJobsItem",
    "RestResponse",
    "RestSendRequestMessagesItem",
    "SmsInboxResponse",
    "SmsInboxResponseMessagesItem",
    "__version__",
    "bulk_sms",
    "queries",
]

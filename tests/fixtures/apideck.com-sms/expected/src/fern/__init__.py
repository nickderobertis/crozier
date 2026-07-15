



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BadRequestResponse,
        BadRequestResponseDetail,
        CreateMessageResponse,
        Currency,
        CustomField,
        CustomFieldValue,
        DeleteMessageResponse,
        Email,
        EmailType,
        GetMessageResponse,
        GetMessagesResponse,
        Links,
        Message,
        MessageDirection,
        MessageError,
        MessagePrice,
        MessageStatus,
        MessageType,
        Meta,
        MetaCursors,
        NotFoundResponse,
        NotFoundResponseDetail,
        NotImplementedResponse,
        NotImplementedResponseDetail,
        PaymentRequiredResponse,
        Tags,
        TooManyRequestsResponse,
        TooManyRequestsResponseDetail,
        UnauthorizedResponse,
        UnexpectedErrorResponse,
        UnexpectedErrorResponseDetail,
        UnifiedId,
        UnprocessableResponse,
        UpdateMessageResponse,
    )
    from .errors import (
        BadRequestError,
        NotFoundError,
        PaymentRequiredError,
        UnauthorizedError,
        UnprocessableEntityError,
    )
    from . import messages
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestResponse": ".types",
    "BadRequestResponseDetail": ".types",
    "CreateMessageResponse": ".types",
    "Currency": ".types",
    "CustomField": ".types",
    "CustomFieldValue": ".types",
    "DeleteMessageResponse": ".types",
    "Email": ".types",
    "EmailType": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetMessageResponse": ".types",
    "GetMessagesResponse": ".types",
    "Links": ".types",
    "Message": ".types",
    "MessageDirection": ".types",
    "MessageError": ".types",
    "MessagePrice": ".types",
    "MessageStatus": ".types",
    "MessageType": ".types",
    "Meta": ".types",
    "MetaCursors": ".types",
    "NotFoundError": ".errors",
    "NotFoundResponse": ".types",
    "NotFoundResponseDetail": ".types",
    "NotImplementedResponse": ".types",
    "NotImplementedResponseDetail": ".types",
    "PaymentRequiredError": ".errors",
    "PaymentRequiredResponse": ".types",
    "Tags": ".types",
    "TooManyRequestsResponse": ".types",
    "TooManyRequestsResponseDetail": ".types",
    "UnauthorizedError": ".errors",
    "UnauthorizedResponse": ".types",
    "UnexpectedErrorResponse": ".types",
    "UnexpectedErrorResponseDetail": ".types",
    "UnifiedId": ".types",
    "UnprocessableEntityError": ".errors",
    "UnprocessableResponse": ".types",
    "UpdateMessageResponse": ".types",
    "__version__": ".version",
    "messages": ".messages",
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
    "BadRequestError",
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "CreateMessageResponse",
    "Currency",
    "CustomField",
    "CustomFieldValue",
    "DeleteMessageResponse",
    "Email",
    "EmailType",
    "FernApi",
    "FernApiEnvironment",
    "GetMessageResponse",
    "GetMessagesResponse",
    "Links",
    "Message",
    "MessageDirection",
    "MessageError",
    "MessagePrice",
    "MessageStatus",
    "MessageType",
    "Meta",
    "MetaCursors",
    "NotFoundError",
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PaymentRequiredError",
    "PaymentRequiredResponse",
    "Tags",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedError",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableEntityError",
    "UnprocessableResponse",
    "UpdateMessageResponse",
    "__version__",
    "messages",
]

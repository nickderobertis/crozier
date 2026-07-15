



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_response import BadRequestResponse
    from .bad_request_response_detail import BadRequestResponseDetail
    from .create_message_response import CreateMessageResponse
    from .currency import Currency
    from .custom_field import CustomField
    from .custom_field_value import CustomFieldValue
    from .delete_message_response import DeleteMessageResponse
    from .email import Email
    from .email_type import EmailType
    from .get_message_response import GetMessageResponse
    from .get_messages_response import GetMessagesResponse
    from .links import Links
    from .message import Message
    from .message_direction import MessageDirection
    from .message_error import MessageError
    from .message_price import MessagePrice
    from .message_status import MessageStatus
    from .message_type import MessageType
    from .meta import Meta
    from .meta_cursors import MetaCursors
    from .not_found_response import NotFoundResponse
    from .not_found_response_detail import NotFoundResponseDetail
    from .not_implemented_response import NotImplementedResponse
    from .not_implemented_response_detail import NotImplementedResponseDetail
    from .payment_required_response import PaymentRequiredResponse
    from .tags import Tags
    from .too_many_requests_response import TooManyRequestsResponse
    from .too_many_requests_response_detail import TooManyRequestsResponseDetail
    from .unauthorized_response import UnauthorizedResponse
    from .unexpected_error_response import UnexpectedErrorResponse
    from .unexpected_error_response_detail import UnexpectedErrorResponseDetail
    from .unified_id import UnifiedId
    from .unprocessable_response import UnprocessableResponse
    from .update_message_response import UpdateMessageResponse
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestResponse": ".bad_request_response",
    "BadRequestResponseDetail": ".bad_request_response_detail",
    "CreateMessageResponse": ".create_message_response",
    "Currency": ".currency",
    "CustomField": ".custom_field",
    "CustomFieldValue": ".custom_field_value",
    "DeleteMessageResponse": ".delete_message_response",
    "Email": ".email",
    "EmailType": ".email_type",
    "GetMessageResponse": ".get_message_response",
    "GetMessagesResponse": ".get_messages_response",
    "Links": ".links",
    "Message": ".message",
    "MessageDirection": ".message_direction",
    "MessageError": ".message_error",
    "MessagePrice": ".message_price",
    "MessageStatus": ".message_status",
    "MessageType": ".message_type",
    "Meta": ".meta",
    "MetaCursors": ".meta_cursors",
    "NotFoundResponse": ".not_found_response",
    "NotFoundResponseDetail": ".not_found_response_detail",
    "NotImplementedResponse": ".not_implemented_response",
    "NotImplementedResponseDetail": ".not_implemented_response_detail",
    "PaymentRequiredResponse": ".payment_required_response",
    "Tags": ".tags",
    "TooManyRequestsResponse": ".too_many_requests_response",
    "TooManyRequestsResponseDetail": ".too_many_requests_response_detail",
    "UnauthorizedResponse": ".unauthorized_response",
    "UnexpectedErrorResponse": ".unexpected_error_response",
    "UnexpectedErrorResponseDetail": ".unexpected_error_response_detail",
    "UnifiedId": ".unified_id",
    "UnprocessableResponse": ".unprocessable_response",
    "UpdateMessageResponse": ".update_message_response",
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
    "BadRequestResponse",
    "BadRequestResponseDetail",
    "CreateMessageResponse",
    "Currency",
    "CustomField",
    "CustomFieldValue",
    "DeleteMessageResponse",
    "Email",
    "EmailType",
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
    "NotFoundResponse",
    "NotFoundResponseDetail",
    "NotImplementedResponse",
    "NotImplementedResponseDetail",
    "PaymentRequiredResponse",
    "Tags",
    "TooManyRequestsResponse",
    "TooManyRequestsResponseDetail",
    "UnauthorizedResponse",
    "UnexpectedErrorResponse",
    "UnexpectedErrorResponseDetail",
    "UnifiedId",
    "UnprocessableResponse",
    "UpdateMessageResponse",
]

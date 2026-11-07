



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .emails_send_request_attachments_item import EmailsSendRequestAttachmentsItem
    from .emails_send_request_bcc import EmailsSendRequestBcc
    from .emails_send_request_bcc_one_item import EmailsSendRequestBccOneItem
    from .emails_send_request_bcc_one_item_email import EmailsSendRequestBccOneItemEmail
    from .emails_send_request_bcc_zero import EmailsSendRequestBccZero
    from .emails_send_request_bcc_zero_email import EmailsSendRequestBccZeroEmail
    from .emails_send_request_cc import EmailsSendRequestCc
    from .emails_send_request_cc_one_item import EmailsSendRequestCcOneItem
    from .emails_send_request_cc_one_item_email import EmailsSendRequestCcOneItemEmail
    from .emails_send_request_cc_zero import EmailsSendRequestCcZero
    from .emails_send_request_cc_zero_email import EmailsSendRequestCcZeroEmail
    from .emails_send_request_from import EmailsSendRequestFrom
    from .emails_send_request_from_email import EmailsSendRequestFromEmail
    from .emails_send_request_reply_to_list import EmailsSendRequestReplyToList
    from .emails_send_request_reply_to_list_email import EmailsSendRequestReplyToListEmail
    from .emails_send_request_reply_to_list_one_item import EmailsSendRequestReplyToListOneItem
    from .emails_send_request_to import EmailsSendRequestTo
    from .emails_send_request_to_one_item import EmailsSendRequestToOneItem
    from .emails_send_request_to_one_item_email import EmailsSendRequestToOneItemEmail
    from .emails_send_request_to_zero import EmailsSendRequestToZero
    from .emails_send_request_to_zero_email import EmailsSendRequestToZeroEmail
    from .emails_send_response import EmailsSendResponse
_dynamic_imports: typing.Dict[str, str] = {
    "EmailsSendRequestAttachmentsItem": ".emails_send_request_attachments_item",
    "EmailsSendRequestBcc": ".emails_send_request_bcc",
    "EmailsSendRequestBccOneItem": ".emails_send_request_bcc_one_item",
    "EmailsSendRequestBccOneItemEmail": ".emails_send_request_bcc_one_item_email",
    "EmailsSendRequestBccZero": ".emails_send_request_bcc_zero",
    "EmailsSendRequestBccZeroEmail": ".emails_send_request_bcc_zero_email",
    "EmailsSendRequestCc": ".emails_send_request_cc",
    "EmailsSendRequestCcOneItem": ".emails_send_request_cc_one_item",
    "EmailsSendRequestCcOneItemEmail": ".emails_send_request_cc_one_item_email",
    "EmailsSendRequestCcZero": ".emails_send_request_cc_zero",
    "EmailsSendRequestCcZeroEmail": ".emails_send_request_cc_zero_email",
    "EmailsSendRequestFrom": ".emails_send_request_from",
    "EmailsSendRequestFromEmail": ".emails_send_request_from_email",
    "EmailsSendRequestReplyToList": ".emails_send_request_reply_to_list",
    "EmailsSendRequestReplyToListEmail": ".emails_send_request_reply_to_list_email",
    "EmailsSendRequestReplyToListOneItem": ".emails_send_request_reply_to_list_one_item",
    "EmailsSendRequestTo": ".emails_send_request_to",
    "EmailsSendRequestToOneItem": ".emails_send_request_to_one_item",
    "EmailsSendRequestToOneItemEmail": ".emails_send_request_to_one_item_email",
    "EmailsSendRequestToZero": ".emails_send_request_to_zero",
    "EmailsSendRequestToZeroEmail": ".emails_send_request_to_zero_email",
    "EmailsSendResponse": ".emails_send_response",
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
    "EmailsSendRequestAttachmentsItem",
    "EmailsSendRequestBcc",
    "EmailsSendRequestBccOneItem",
    "EmailsSendRequestBccOneItemEmail",
    "EmailsSendRequestBccZero",
    "EmailsSendRequestBccZeroEmail",
    "EmailsSendRequestCc",
    "EmailsSendRequestCcOneItem",
    "EmailsSendRequestCcOneItemEmail",
    "EmailsSendRequestCcZero",
    "EmailsSendRequestCcZeroEmail",
    "EmailsSendRequestFrom",
    "EmailsSendRequestFromEmail",
    "EmailsSendRequestReplyToList",
    "EmailsSendRequestReplyToListEmail",
    "EmailsSendRequestReplyToListOneItem",
    "EmailsSendRequestTo",
    "EmailsSendRequestToOneItem",
    "EmailsSendRequestToOneItemEmail",
    "EmailsSendRequestToZero",
    "EmailsSendRequestToZeroEmail",
    "EmailsSendResponse",
]

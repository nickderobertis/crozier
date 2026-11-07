



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        EmailsSendRequestAttachmentsItem,
        EmailsSendRequestBcc,
        EmailsSendRequestBccOneItem,
        EmailsSendRequestBccOneItemEmail,
        EmailsSendRequestBccZero,
        EmailsSendRequestBccZeroEmail,
        EmailsSendRequestCc,
        EmailsSendRequestCcOneItem,
        EmailsSendRequestCcOneItemEmail,
        EmailsSendRequestCcZero,
        EmailsSendRequestCcZeroEmail,
        EmailsSendRequestFrom,
        EmailsSendRequestFromEmail,
        EmailsSendRequestReplyToList,
        EmailsSendRequestReplyToListEmail,
        EmailsSendRequestReplyToListOneItem,
        EmailsSendRequestTo,
        EmailsSendRequestToOneItem,
        EmailsSendRequestToOneItemEmail,
        EmailsSendRequestToZero,
        EmailsSendRequestToZeroEmail,
        EmailsSendResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "EmailsSendRequestAttachmentsItem": ".types",
    "EmailsSendRequestBcc": ".types",
    "EmailsSendRequestBccOneItem": ".types",
    "EmailsSendRequestBccOneItemEmail": ".types",
    "EmailsSendRequestBccZero": ".types",
    "EmailsSendRequestBccZeroEmail": ".types",
    "EmailsSendRequestCc": ".types",
    "EmailsSendRequestCcOneItem": ".types",
    "EmailsSendRequestCcOneItemEmail": ".types",
    "EmailsSendRequestCcZero": ".types",
    "EmailsSendRequestCcZeroEmail": ".types",
    "EmailsSendRequestFrom": ".types",
    "EmailsSendRequestFromEmail": ".types",
    "EmailsSendRequestReplyToList": ".types",
    "EmailsSendRequestReplyToListEmail": ".types",
    "EmailsSendRequestReplyToListOneItem": ".types",
    "EmailsSendRequestTo": ".types",
    "EmailsSendRequestToOneItem": ".types",
    "EmailsSendRequestToOneItemEmail": ".types",
    "EmailsSendRequestToZero": ".types",
    "EmailsSendRequestToZeroEmail": ".types",
    "EmailsSendResponse": ".types",
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

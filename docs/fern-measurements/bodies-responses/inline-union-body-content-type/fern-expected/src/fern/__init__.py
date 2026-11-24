



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import EmailVerification, SmsVerification
    from . import verifications
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .verifications import (
        AddContactRequest,
        AddContactRequestEmail,
        AddContactRequestSms,
        AddContactRequest_Email,
        AddContactRequest_Sms,
        AddTaggedContactRequest,
        AddTaggedContactRequestEmail,
        AddTaggedContactRequestSms,
        AddTaggedContactRequest_Email,
        AddTaggedContactRequest_Sms,
        AddVerificationRequest,
        AddVerificationRequest_Email,
        AddVerificationRequest_Sms,
        RecheckVerificationRequest,
        RecheckVerificationRequest_Email,
        RecheckVerificationRequest_Sms,
        SendNoticeRequest,
        SendNoticeRequest_Email,
        SendNoticeRequest_Sms,
        SendReminderRequest,
        SendReminderRequest_Email,
        SendReminderRequest_Sms,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AddContactRequest": ".verifications",
    "AddContactRequestEmail": ".verifications",
    "AddContactRequestSms": ".verifications",
    "AddContactRequest_Email": ".verifications",
    "AddContactRequest_Sms": ".verifications",
    "AddTaggedContactRequest": ".verifications",
    "AddTaggedContactRequestEmail": ".verifications",
    "AddTaggedContactRequestSms": ".verifications",
    "AddTaggedContactRequest_Email": ".verifications",
    "AddTaggedContactRequest_Sms": ".verifications",
    "AddVerificationRequest": ".verifications",
    "AddVerificationRequest_Email": ".verifications",
    "AddVerificationRequest_Sms": ".verifications",
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "EmailVerification": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "RecheckVerificationRequest": ".verifications",
    "RecheckVerificationRequest_Email": ".verifications",
    "RecheckVerificationRequest_Sms": ".verifications",
    "SendNoticeRequest": ".verifications",
    "SendNoticeRequest_Email": ".verifications",
    "SendNoticeRequest_Sms": ".verifications",
    "SendReminderRequest": ".verifications",
    "SendReminderRequest_Email": ".verifications",
    "SendReminderRequest_Sms": ".verifications",
    "SmsVerification": ".types",
    "__version__": ".version",
    "verifications": ".verifications",
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
    "AddContactRequest",
    "AddContactRequestEmail",
    "AddContactRequestSms",
    "AddContactRequest_Email",
    "AddContactRequest_Sms",
    "AddTaggedContactRequest",
    "AddTaggedContactRequestEmail",
    "AddTaggedContactRequestSms",
    "AddTaggedContactRequest_Email",
    "AddTaggedContactRequest_Sms",
    "AddVerificationRequest",
    "AddVerificationRequest_Email",
    "AddVerificationRequest_Sms",
    "AsyncFernApi",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "EmailVerification",
    "FernApi",
    "FernApiEnvironment",
    "RecheckVerificationRequest",
    "RecheckVerificationRequest_Email",
    "RecheckVerificationRequest_Sms",
    "SendNoticeRequest",
    "SendNoticeRequest_Email",
    "SendNoticeRequest_Sms",
    "SendReminderRequest",
    "SendReminderRequest_Email",
    "SendReminderRequest_Sms",
    "SmsVerification",
    "__version__",
    "verifications",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
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
_dynamic_imports: typing.Dict[str, str] = {
    "AddContactRequest": ".types",
    "AddContactRequestEmail": ".types",
    "AddContactRequestSms": ".types",
    "AddContactRequest_Email": ".types",
    "AddContactRequest_Sms": ".types",
    "AddTaggedContactRequest": ".types",
    "AddTaggedContactRequestEmail": ".types",
    "AddTaggedContactRequestSms": ".types",
    "AddTaggedContactRequest_Email": ".types",
    "AddTaggedContactRequest_Sms": ".types",
    "AddVerificationRequest": ".types",
    "AddVerificationRequest_Email": ".types",
    "AddVerificationRequest_Sms": ".types",
    "RecheckVerificationRequest": ".types",
    "RecheckVerificationRequest_Email": ".types",
    "RecheckVerificationRequest_Sms": ".types",
    "SendNoticeRequest": ".types",
    "SendNoticeRequest_Email": ".types",
    "SendNoticeRequest_Sms": ".types",
    "SendReminderRequest": ".types",
    "SendReminderRequest_Email": ".types",
    "SendReminderRequest_Sms": ".types",
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
    "RecheckVerificationRequest",
    "RecheckVerificationRequest_Email",
    "RecheckVerificationRequest_Sms",
    "SendNoticeRequest",
    "SendNoticeRequest_Email",
    "SendNoticeRequest_Sms",
    "SendReminderRequest",
    "SendReminderRequest_Email",
    "SendReminderRequest_Sms",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_verification_request import (
        AddVerificationRequest,
        AddVerificationRequest_Email,
        AddVerificationRequest_Sms,
    )
    from .recheck_verification_request import (
        RecheckVerificationRequest,
        RecheckVerificationRequest_Email,
        RecheckVerificationRequest_Sms,
    )
    from .send_reminder_request import SendReminderRequest, SendReminderRequest_Email, SendReminderRequest_Sms
_dynamic_imports: typing.Dict[str, str] = {
    "AddVerificationRequest": ".add_verification_request",
    "AddVerificationRequest_Email": ".add_verification_request",
    "AddVerificationRequest_Sms": ".add_verification_request",
    "RecheckVerificationRequest": ".recheck_verification_request",
    "RecheckVerificationRequest_Email": ".recheck_verification_request",
    "RecheckVerificationRequest_Sms": ".recheck_verification_request",
    "SendReminderRequest": ".send_reminder_request",
    "SendReminderRequest_Email": ".send_reminder_request",
    "SendReminderRequest_Sms": ".send_reminder_request",
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
    "AddVerificationRequest",
    "AddVerificationRequest_Email",
    "AddVerificationRequest_Sms",
    "RecheckVerificationRequest",
    "RecheckVerificationRequest_Email",
    "RecheckVerificationRequest_Sms",
    "SendReminderRequest",
    "SendReminderRequest_Email",
    "SendReminderRequest_Sms",
]

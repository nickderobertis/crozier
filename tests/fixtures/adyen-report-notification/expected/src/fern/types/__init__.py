



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .balance_platform_notification_response import BalancePlatformNotificationResponse
    from .report_notification_data import ReportNotificationData
    from .report_notification_request import ReportNotificationRequest
    from .report_notification_request_type import ReportNotificationRequestType
    from .resource import Resource
    from .resource_reference import ResourceReference
_dynamic_imports: typing.Dict[str, str] = {
    "BalancePlatformNotificationResponse": ".balance_platform_notification_response",
    "ReportNotificationData": ".report_notification_data",
    "ReportNotificationRequest": ".report_notification_request",
    "ReportNotificationRequestType": ".report_notification_request_type",
    "Resource": ".resource",
    "ResourceReference": ".resource_reference",
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
    "BalancePlatformNotificationResponse",
    "ReportNotificationData",
    "ReportNotificationRequest",
    "ReportNotificationRequestType",
    "Resource",
    "ResourceReference",
]





import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_notification_response import CreateNotificationResponse
    from .delete_notification_response import DeleteNotificationResponse
    from .get_notification_event_data_response import GetNotificationEventDataResponse
    from .get_notifications_response import GetNotificationsResponse
    from .get_notifications_response_data import GetNotificationsResponseData
    from .update_notification_response import UpdateNotificationResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateNotificationResponse": ".create_notification_response",
    "DeleteNotificationResponse": ".delete_notification_response",
    "GetNotificationEventDataResponse": ".get_notification_event_data_response",
    "GetNotificationsResponse": ".get_notifications_response",
    "GetNotificationsResponseData": ".get_notifications_response_data",
    "UpdateNotificationResponse": ".update_notification_response",
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
    "CreateNotificationResponse",
    "DeleteNotificationResponse",
    "GetNotificationEventDataResponse",
    "GetNotificationsResponse",
    "GetNotificationsResponseData",
    "UpdateNotificationResponse",
]

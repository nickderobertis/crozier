



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_users_accounts_request_review_status import ListUsersAccountsRequestReviewStatus
    from .user_notification_create_product import UserNotificationCreateProduct
    from .user_notification_create_product_zero import UserNotificationCreateProductZero
    from .user_notification_create_resource_id import UserNotificationCreateResourceId
    from .user_notification_create_resource_id_zero import UserNotificationCreateResourceIdZero
_dynamic_imports: typing.Dict[str, str] = {
    "ListUsersAccountsRequestReviewStatus": ".list_users_accounts_request_review_status",
    "UserNotificationCreateProduct": ".user_notification_create_product",
    "UserNotificationCreateProductZero": ".user_notification_create_product_zero",
    "UserNotificationCreateResourceId": ".user_notification_create_resource_id",
    "UserNotificationCreateResourceIdZero": ".user_notification_create_resource_id_zero",
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
    "ListUsersAccountsRequestReviewStatus",
    "UserNotificationCreateProduct",
    "UserNotificationCreateProductZero",
    "UserNotificationCreateResourceId",
    "UserNotificationCreateResourceIdZero",
]

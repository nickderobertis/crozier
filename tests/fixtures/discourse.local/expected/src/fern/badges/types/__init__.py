



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .admin_list_badges_response import AdminListBadgesResponse
    from .admin_list_badges_response_admin_badges import AdminListBadgesResponseAdminBadges
    from .admin_list_badges_response_admin_badges_triggers import AdminListBadgesResponseAdminBadgesTriggers
    from .admin_list_badges_response_badge_groupings_item import AdminListBadgesResponseBadgeGroupingsItem
    from .admin_list_badges_response_badge_types_item import AdminListBadgesResponseBadgeTypesItem
    from .admin_list_badges_response_badges_item import AdminListBadgesResponseBadgesItem
    from .create_badge_response import CreateBadgeResponse
    from .create_badge_response_badge import CreateBadgeResponseBadge
    from .create_badge_response_badge_types_item import CreateBadgeResponseBadgeTypesItem
    from .list_user_badges_response import ListUserBadgesResponse
    from .list_user_badges_response_badge_types_item import ListUserBadgesResponseBadgeTypesItem
    from .list_user_badges_response_badges_item import ListUserBadgesResponseBadgesItem
    from .list_user_badges_response_granted_bies_item import ListUserBadgesResponseGrantedBiesItem
    from .list_user_badges_response_user_badges_item import ListUserBadgesResponseUserBadgesItem
    from .update_badge_response import UpdateBadgeResponse
    from .update_badge_response_badge import UpdateBadgeResponseBadge
    from .update_badge_response_badge_types_item import UpdateBadgeResponseBadgeTypesItem
_dynamic_imports: typing.Dict[str, str] = {
    "AdminListBadgesResponse": ".admin_list_badges_response",
    "AdminListBadgesResponseAdminBadges": ".admin_list_badges_response_admin_badges",
    "AdminListBadgesResponseAdminBadgesTriggers": ".admin_list_badges_response_admin_badges_triggers",
    "AdminListBadgesResponseBadgeGroupingsItem": ".admin_list_badges_response_badge_groupings_item",
    "AdminListBadgesResponseBadgeTypesItem": ".admin_list_badges_response_badge_types_item",
    "AdminListBadgesResponseBadgesItem": ".admin_list_badges_response_badges_item",
    "CreateBadgeResponse": ".create_badge_response",
    "CreateBadgeResponseBadge": ".create_badge_response_badge",
    "CreateBadgeResponseBadgeTypesItem": ".create_badge_response_badge_types_item",
    "ListUserBadgesResponse": ".list_user_badges_response",
    "ListUserBadgesResponseBadgeTypesItem": ".list_user_badges_response_badge_types_item",
    "ListUserBadgesResponseBadgesItem": ".list_user_badges_response_badges_item",
    "ListUserBadgesResponseGrantedBiesItem": ".list_user_badges_response_granted_bies_item",
    "ListUserBadgesResponseUserBadgesItem": ".list_user_badges_response_user_badges_item",
    "UpdateBadgeResponse": ".update_badge_response",
    "UpdateBadgeResponseBadge": ".update_badge_response_badge",
    "UpdateBadgeResponseBadgeTypesItem": ".update_badge_response_badge_types_item",
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
    "AdminListBadgesResponse",
    "AdminListBadgesResponseAdminBadges",
    "AdminListBadgesResponseAdminBadgesTriggers",
    "AdminListBadgesResponseBadgeGroupingsItem",
    "AdminListBadgesResponseBadgeTypesItem",
    "AdminListBadgesResponseBadgesItem",
    "CreateBadgeResponse",
    "CreateBadgeResponseBadge",
    "CreateBadgeResponseBadgeTypesItem",
    "ListUserBadgesResponse",
    "ListUserBadgesResponseBadgeTypesItem",
    "ListUserBadgesResponseBadgesItem",
    "ListUserBadgesResponseGrantedBiesItem",
    "ListUserBadgesResponseUserBadgesItem",
    "UpdateBadgeResponse",
    "UpdateBadgeResponseBadge",
    "UpdateBadgeResponseBadgeTypesItem",
]

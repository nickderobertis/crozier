



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_site_response import GetSiteResponse
    from .get_site_response_archetypes_item import GetSiteResponseArchetypesItem
    from .get_site_response_categories_item import GetSiteResponseCategoriesItem
    from .get_site_response_categories_item_required_tag_groups_item import (
        GetSiteResponseCategoriesItemRequiredTagGroupsItem,
    )
    from .get_site_response_custom_emoji_translation import GetSiteResponseCustomEmojiTranslation
    from .get_site_response_groups_item import GetSiteResponseGroupsItem
    from .get_site_response_notification_types import GetSiteResponseNotificationTypes
    from .get_site_response_post_action_types_item import GetSiteResponsePostActionTypesItem
    from .get_site_response_post_types import GetSiteResponsePostTypes
    from .get_site_response_topic_flag_types_item import GetSiteResponseTopicFlagTypesItem
    from .get_site_response_trust_levels import GetSiteResponseTrustLevels
    from .get_site_response_user_color_schemes_item import GetSiteResponseUserColorSchemesItem
    from .get_site_response_user_themes_item import GetSiteResponseUserThemesItem
_dynamic_imports: typing.Dict[str, str] = {
    "GetSiteResponse": ".get_site_response",
    "GetSiteResponseArchetypesItem": ".get_site_response_archetypes_item",
    "GetSiteResponseCategoriesItem": ".get_site_response_categories_item",
    "GetSiteResponseCategoriesItemRequiredTagGroupsItem": ".get_site_response_categories_item_required_tag_groups_item",
    "GetSiteResponseCustomEmojiTranslation": ".get_site_response_custom_emoji_translation",
    "GetSiteResponseGroupsItem": ".get_site_response_groups_item",
    "GetSiteResponseNotificationTypes": ".get_site_response_notification_types",
    "GetSiteResponsePostActionTypesItem": ".get_site_response_post_action_types_item",
    "GetSiteResponsePostTypes": ".get_site_response_post_types",
    "GetSiteResponseTopicFlagTypesItem": ".get_site_response_topic_flag_types_item",
    "GetSiteResponseTrustLevels": ".get_site_response_trust_levels",
    "GetSiteResponseUserColorSchemesItem": ".get_site_response_user_color_schemes_item",
    "GetSiteResponseUserThemesItem": ".get_site_response_user_themes_item",
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
    "GetSiteResponse",
    "GetSiteResponseArchetypesItem",
    "GetSiteResponseCategoriesItem",
    "GetSiteResponseCategoriesItemRequiredTagGroupsItem",
    "GetSiteResponseCustomEmojiTranslation",
    "GetSiteResponseGroupsItem",
    "GetSiteResponseNotificationTypes",
    "GetSiteResponsePostActionTypesItem",
    "GetSiteResponsePostTypes",
    "GetSiteResponseTopicFlagTypesItem",
    "GetSiteResponseTrustLevels",
    "GetSiteResponseUserColorSchemesItem",
    "GetSiteResponseUserThemesItem",
]

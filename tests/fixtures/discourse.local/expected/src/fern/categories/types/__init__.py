



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_category_request_permissions import CreateCategoryRequestPermissions
    from .create_category_response import CreateCategoryResponse
    from .create_category_response_category import CreateCategoryResponseCategory
    from .create_category_response_category_custom_fields import CreateCategoryResponseCategoryCustomFields
    from .create_category_response_category_group_permissions_item import (
        CreateCategoryResponseCategoryGroupPermissionsItem,
    )
    from .create_category_response_category_required_tag_groups_item import (
        CreateCategoryResponseCategoryRequiredTagGroupsItem,
    )
    from .get_category_response import GetCategoryResponse
    from .get_category_response_category import GetCategoryResponseCategory
    from .get_category_response_category_custom_fields import GetCategoryResponseCategoryCustomFields
    from .get_category_response_category_group_permissions_item import GetCategoryResponseCategoryGroupPermissionsItem
    from .get_category_response_category_required_tag_groups_item import (
        GetCategoryResponseCategoryRequiredTagGroupsItem,
    )
    from .list_categories_response import ListCategoriesResponse
    from .list_categories_response_category_list import ListCategoriesResponseCategoryList
    from .list_categories_response_category_list_categories_item import ListCategoriesResponseCategoryListCategoriesItem
    from .list_category_topics_response import ListCategoryTopicsResponse
    from .list_category_topics_response_topic_list import ListCategoryTopicsResponseTopicList
    from .list_category_topics_response_topic_list_topics_item import ListCategoryTopicsResponseTopicListTopicsItem
    from .list_category_topics_response_topic_list_topics_item_posters_item import (
        ListCategoryTopicsResponseTopicListTopicsItemPostersItem,
    )
    from .list_category_topics_response_users_item import ListCategoryTopicsResponseUsersItem
    from .update_category_request_permissions import UpdateCategoryRequestPermissions
    from .update_category_response import UpdateCategoryResponse
    from .update_category_response_category import UpdateCategoryResponseCategory
    from .update_category_response_category_custom_fields import UpdateCategoryResponseCategoryCustomFields
    from .update_category_response_category_group_permissions_item import (
        UpdateCategoryResponseCategoryGroupPermissionsItem,
    )
    from .update_category_response_category_required_tag_groups_item import (
        UpdateCategoryResponseCategoryRequiredTagGroupsItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateCategoryRequestPermissions": ".create_category_request_permissions",
    "CreateCategoryResponse": ".create_category_response",
    "CreateCategoryResponseCategory": ".create_category_response_category",
    "CreateCategoryResponseCategoryCustomFields": ".create_category_response_category_custom_fields",
    "CreateCategoryResponseCategoryGroupPermissionsItem": ".create_category_response_category_group_permissions_item",
    "CreateCategoryResponseCategoryRequiredTagGroupsItem": ".create_category_response_category_required_tag_groups_item",
    "GetCategoryResponse": ".get_category_response",
    "GetCategoryResponseCategory": ".get_category_response_category",
    "GetCategoryResponseCategoryCustomFields": ".get_category_response_category_custom_fields",
    "GetCategoryResponseCategoryGroupPermissionsItem": ".get_category_response_category_group_permissions_item",
    "GetCategoryResponseCategoryRequiredTagGroupsItem": ".get_category_response_category_required_tag_groups_item",
    "ListCategoriesResponse": ".list_categories_response",
    "ListCategoriesResponseCategoryList": ".list_categories_response_category_list",
    "ListCategoriesResponseCategoryListCategoriesItem": ".list_categories_response_category_list_categories_item",
    "ListCategoryTopicsResponse": ".list_category_topics_response",
    "ListCategoryTopicsResponseTopicList": ".list_category_topics_response_topic_list",
    "ListCategoryTopicsResponseTopicListTopicsItem": ".list_category_topics_response_topic_list_topics_item",
    "ListCategoryTopicsResponseTopicListTopicsItemPostersItem": ".list_category_topics_response_topic_list_topics_item_posters_item",
    "ListCategoryTopicsResponseUsersItem": ".list_category_topics_response_users_item",
    "UpdateCategoryRequestPermissions": ".update_category_request_permissions",
    "UpdateCategoryResponse": ".update_category_response",
    "UpdateCategoryResponseCategory": ".update_category_response_category",
    "UpdateCategoryResponseCategoryCustomFields": ".update_category_response_category_custom_fields",
    "UpdateCategoryResponseCategoryGroupPermissionsItem": ".update_category_response_category_group_permissions_item",
    "UpdateCategoryResponseCategoryRequiredTagGroupsItem": ".update_category_response_category_required_tag_groups_item",
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
    "CreateCategoryRequestPermissions",
    "CreateCategoryResponse",
    "CreateCategoryResponseCategory",
    "CreateCategoryResponseCategoryCustomFields",
    "CreateCategoryResponseCategoryGroupPermissionsItem",
    "CreateCategoryResponseCategoryRequiredTagGroupsItem",
    "GetCategoryResponse",
    "GetCategoryResponseCategory",
    "GetCategoryResponseCategoryCustomFields",
    "GetCategoryResponseCategoryGroupPermissionsItem",
    "GetCategoryResponseCategoryRequiredTagGroupsItem",
    "ListCategoriesResponse",
    "ListCategoriesResponseCategoryList",
    "ListCategoriesResponseCategoryListCategoriesItem",
    "ListCategoryTopicsResponse",
    "ListCategoryTopicsResponseTopicList",
    "ListCategoryTopicsResponseTopicListTopicsItem",
    "ListCategoryTopicsResponseTopicListTopicsItemPostersItem",
    "ListCategoryTopicsResponseUsersItem",
    "UpdateCategoryRequestPermissions",
    "UpdateCategoryResponse",
    "UpdateCategoryResponseCategory",
    "UpdateCategoryResponseCategoryCustomFields",
    "UpdateCategoryResponseCategoryGroupPermissionsItem",
    "UpdateCategoryResponseCategoryRequiredTagGroupsItem",
]

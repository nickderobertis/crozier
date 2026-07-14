



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_tag_group_response import CreateTagGroupResponse
    from .create_tag_group_response_tag_group import CreateTagGroupResponseTagGroup
    from .get_tag_group_response import GetTagGroupResponse
    from .get_tag_group_response_tag_group import GetTagGroupResponseTagGroup
    from .get_tag_group_response_tag_group_permissions import GetTagGroupResponseTagGroupPermissions
    from .get_tag_response import GetTagResponse
    from .get_tag_response_topic_list import GetTagResponseTopicList
    from .get_tag_response_topic_list_tags_item import GetTagResponseTopicListTagsItem
    from .get_tag_response_topic_list_topics_item import GetTagResponseTopicListTopicsItem
    from .get_tag_response_topic_list_topics_item_posters_item import GetTagResponseTopicListTopicsItemPostersItem
    from .get_tag_response_users_item import GetTagResponseUsersItem
    from .list_tag_groups_response import ListTagGroupsResponse
    from .list_tag_groups_response_tag_groups_item import ListTagGroupsResponseTagGroupsItem
    from .list_tag_groups_response_tag_groups_item_permissions import ListTagGroupsResponseTagGroupsItemPermissions
    from .list_tags_response import ListTagsResponse
    from .list_tags_response_extras import ListTagsResponseExtras
    from .list_tags_response_tags_item import ListTagsResponseTagsItem
    from .update_tag_group_response import UpdateTagGroupResponse
    from .update_tag_group_response_tag_group import UpdateTagGroupResponseTagGroup
    from .update_tag_group_response_tag_group_permissions import UpdateTagGroupResponseTagGroupPermissions
_dynamic_imports: typing.Dict[str, str] = {
    "CreateTagGroupResponse": ".create_tag_group_response",
    "CreateTagGroupResponseTagGroup": ".create_tag_group_response_tag_group",
    "GetTagGroupResponse": ".get_tag_group_response",
    "GetTagGroupResponseTagGroup": ".get_tag_group_response_tag_group",
    "GetTagGroupResponseTagGroupPermissions": ".get_tag_group_response_tag_group_permissions",
    "GetTagResponse": ".get_tag_response",
    "GetTagResponseTopicList": ".get_tag_response_topic_list",
    "GetTagResponseTopicListTagsItem": ".get_tag_response_topic_list_tags_item",
    "GetTagResponseTopicListTopicsItem": ".get_tag_response_topic_list_topics_item",
    "GetTagResponseTopicListTopicsItemPostersItem": ".get_tag_response_topic_list_topics_item_posters_item",
    "GetTagResponseUsersItem": ".get_tag_response_users_item",
    "ListTagGroupsResponse": ".list_tag_groups_response",
    "ListTagGroupsResponseTagGroupsItem": ".list_tag_groups_response_tag_groups_item",
    "ListTagGroupsResponseTagGroupsItemPermissions": ".list_tag_groups_response_tag_groups_item_permissions",
    "ListTagsResponse": ".list_tags_response",
    "ListTagsResponseExtras": ".list_tags_response_extras",
    "ListTagsResponseTagsItem": ".list_tags_response_tags_item",
    "UpdateTagGroupResponse": ".update_tag_group_response",
    "UpdateTagGroupResponseTagGroup": ".update_tag_group_response_tag_group",
    "UpdateTagGroupResponseTagGroupPermissions": ".update_tag_group_response_tag_group_permissions",
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
    "CreateTagGroupResponse",
    "CreateTagGroupResponseTagGroup",
    "GetTagGroupResponse",
    "GetTagGroupResponseTagGroup",
    "GetTagGroupResponseTagGroupPermissions",
    "GetTagResponse",
    "GetTagResponseTopicList",
    "GetTagResponseTopicListTagsItem",
    "GetTagResponseTopicListTopicsItem",
    "GetTagResponseTopicListTopicsItemPostersItem",
    "GetTagResponseUsersItem",
    "ListTagGroupsResponse",
    "ListTagGroupsResponseTagGroupsItem",
    "ListTagGroupsResponseTagGroupsItemPermissions",
    "ListTagsResponse",
    "ListTagsResponseExtras",
    "ListTagsResponseTagsItem",
    "UpdateTagGroupResponse",
    "UpdateTagGroupResponseTagGroup",
    "UpdateTagGroupResponseTagGroupPermissions",
]

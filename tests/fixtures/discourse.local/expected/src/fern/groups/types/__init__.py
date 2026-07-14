



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_group_members_response import AddGroupMembersResponse
    from .create_group_request_group import CreateGroupRequestGroup
    from .create_group_response import CreateGroupResponse
    from .create_group_response_basic_group import CreateGroupResponseBasicGroup
    from .delete_group_response import DeleteGroupResponse
    from .get_group_response import GetGroupResponse
    from .get_group_response_extras import GetGroupResponseExtras
    from .get_group_response_group import GetGroupResponseGroup
    from .list_group_members_response import ListGroupMembersResponse
    from .list_group_members_response_members_item import ListGroupMembersResponseMembersItem
    from .list_group_members_response_meta import ListGroupMembersResponseMeta
    from .list_group_members_response_owners_item import ListGroupMembersResponseOwnersItem
    from .list_groups_response import ListGroupsResponse
    from .list_groups_response_extras import ListGroupsResponseExtras
    from .list_groups_response_groups_item import ListGroupsResponseGroupsItem
    from .remove_group_members_response import RemoveGroupMembersResponse
    from .update_group_request_group import UpdateGroupRequestGroup
    from .update_group_response import UpdateGroupResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AddGroupMembersResponse": ".add_group_members_response",
    "CreateGroupRequestGroup": ".create_group_request_group",
    "CreateGroupResponse": ".create_group_response",
    "CreateGroupResponseBasicGroup": ".create_group_response_basic_group",
    "DeleteGroupResponse": ".delete_group_response",
    "GetGroupResponse": ".get_group_response",
    "GetGroupResponseExtras": ".get_group_response_extras",
    "GetGroupResponseGroup": ".get_group_response_group",
    "ListGroupMembersResponse": ".list_group_members_response",
    "ListGroupMembersResponseMembersItem": ".list_group_members_response_members_item",
    "ListGroupMembersResponseMeta": ".list_group_members_response_meta",
    "ListGroupMembersResponseOwnersItem": ".list_group_members_response_owners_item",
    "ListGroupsResponse": ".list_groups_response",
    "ListGroupsResponseExtras": ".list_groups_response_extras",
    "ListGroupsResponseGroupsItem": ".list_groups_response_groups_item",
    "RemoveGroupMembersResponse": ".remove_group_members_response",
    "UpdateGroupRequestGroup": ".update_group_request_group",
    "UpdateGroupResponse": ".update_group_response",
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
    "AddGroupMembersResponse",
    "CreateGroupRequestGroup",
    "CreateGroupResponse",
    "CreateGroupResponseBasicGroup",
    "DeleteGroupResponse",
    "GetGroupResponse",
    "GetGroupResponseExtras",
    "GetGroupResponseGroup",
    "ListGroupMembersResponse",
    "ListGroupMembersResponseMembersItem",
    "ListGroupMembersResponseMeta",
    "ListGroupMembersResponseOwnersItem",
    "ListGroupsResponse",
    "ListGroupsResponseExtras",
    "ListGroupsResponseGroupsItem",
    "RemoveGroupMembersResponse",
    "UpdateGroupRequestGroup",
    "UpdateGroupResponse",
]

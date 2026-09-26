

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_group_can_add_members_group import UserGroupCanAddMembersGroup
from .user_group_can_join_group import UserGroupCanJoinGroup
from .user_group_can_leave_group import UserGroupCanLeaveGroup
from .user_group_can_manage_group import UserGroupCanManageGroup
from .user_group_can_mention_group import UserGroupCanMentionGroup
from .user_group_can_remove_members_group import UserGroupCanRemoveMembersGroup


class UserGroup(UniversalBaseModel):
    """
    Object containing the user group's attributes.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the user group.
    """

    date_created: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the user group was created, in UTC seconds.
    
    A `null` value means the user group has no recorded date, which is often
    because the user group is very old, or because it was created via a data
    import tool or [management command][management-commands].
    
    **Changes**: New in Zulip 10.0 (feature level 292).
    [management-commands]: https://zulip.readthedocs.io/en/latest/production/management-commands.html
    """

    creator_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who created this user group.
    
    A `null` value means the user group has no recorded creator, which is often
    because the user group is very old, or because it was created via a data
    import tool or [management command][management-commands].
    
    **Changes**: New in Zulip 10.0 (feature level 292).
    [management-commands]: https://zulip.readthedocs.io/en/latest/production/management-commands.html
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the user group.
    """

    members: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array containing the ID of the users who are
    members of this user group.
    
    **Changes**: Prior to Zulip 10.0 (feature level 303), this
    list also included deactivated users who were members of
    the user group before being deactivated.
    """

    direct_subgroup_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array containing the ID of the direct_subgroups of
    this user group.
    
    **Changes**: New in Zulip 6.0 (feature level 131).
    Introduced in feature level 127 as `subgroups`, but
    clients can ignore older events as this feature level
    predates subgroups being fully implemented.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user group.
    """

    is_system_group: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user group is a system group which cannot be
    directly modified by users.
    
    **Changes**: New in Zulip 5.0 (feature level 93).
    """

    can_add_members_group: typing.Optional[UserGroupCanAddMembersGroup] = pydantic.Field(default=None)
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to add members to this user group.
    
    **Changes**: New in Zulip 10.0 (feature level 305). Previously, this
    permission was controlled by the `can_manage_group` setting.
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    """

    can_join_group: typing.Optional[UserGroupCanJoinGroup] = pydantic.Field(default=None)
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to join this user group.
    
    **Changes**: New in Zulip 10.0 (feature level 301).
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    """

    can_leave_group: typing.Optional[UserGroupCanLeaveGroup] = pydantic.Field(default=None)
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to leave this user group.
    
    **Changes**: New in Zulip 10.0 (feature level 308).
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    """

    can_manage_group: typing.Optional[UserGroupCanManageGroup] = pydantic.Field(default=None)
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to [manage this user group][manage-user-groups].
    
    **Changes**: New in Zulip 10.0 (feature level 283).
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    [manage-user-groups]: /help/manage-user-groups
    """

    can_mention_group: typing.Optional[UserGroupCanMentionGroup] = pydantic.Field(default=None)
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to [mention this user group][mentions].
    
    **Changes**: Before Zulip 9.0 (feature level 258), this setting was
    always the integer form of a [group-setting value][setting-values].
    
    Before Zulip 8.0 (feature level 198), this setting was named
    `can_mention_group_id`.
    
    New in Zulip 8.0 (feature level 191). Previously, groups could be
    mentioned only if they were not [system groups][system-groups].
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    [system-groups]: /api/group-setting-values#system-groups
    [mentions]: /help/mention-a-user-or-group
    """

    can_remove_members_group: typing.Optional[UserGroupCanRemoveMembersGroup] = pydantic.Field(default=None)
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to remove members from this user group.
    
    **Changes**: New in Zulip 10.0 (feature level 324). Previously, this
    permission was controlled by the `can_manage_group` setting.
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    """

    deactivated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user group is deactivated. Deactivated groups
    cannot be used as a subgroup of another group or used for
    any other purpose.
    
    **Changes**: New in Zulip 10.0 (feature level 290).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

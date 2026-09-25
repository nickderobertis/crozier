

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_events_response_events_item_forty_five_data_can_add_members_group import (
    GetEventsResponseEventsItemFortyFiveDataCanAddMembersGroup,
)
from .get_events_response_events_item_forty_five_data_can_join_group import (
    GetEventsResponseEventsItemFortyFiveDataCanJoinGroup,
)
from .get_events_response_events_item_forty_five_data_can_leave_group import (
    GetEventsResponseEventsItemFortyFiveDataCanLeaveGroup,
)
from .get_events_response_events_item_forty_five_data_can_manage_group import (
    GetEventsResponseEventsItemFortyFiveDataCanManageGroup,
)
from .get_events_response_events_item_forty_five_data_can_mention_group import (
    GetEventsResponseEventsItemFortyFiveDataCanMentionGroup,
)
from .get_events_response_events_item_forty_five_data_can_remove_members_group import (
    GetEventsResponseEventsItemFortyFiveDataCanRemoveMembersGroup,
)


class GetEventsResponseEventsItemFortyFiveData(UniversalBaseModel):
    """
    Dictionary containing the changed details of the user group.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new name of the user group. Only present if the group's name changed.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new description of the group. Only present if the description
    changed.
    """

    can_add_members_group: typing.Optional[GetEventsResponseEventsItemFortyFiveDataCanAddMembersGroup] = pydantic.Field(
        default=None
    )
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to add members to this group. Only present if this user
    group permission setting changed.
    
    **Changes**: New in Zulip 10.0 (feature level 305). Previously, this
    permission was controlled by the `can_manage_group` setting.
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    """

    can_join_group: typing.Optional[GetEventsResponseEventsItemFortyFiveDataCanJoinGroup] = pydantic.Field(default=None)
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to join this group. Only present if this user group
    permission setting changed.
    
    **Changes**: New in Zulip 10.0 (feature level 301).
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    """

    can_leave_group: typing.Optional[GetEventsResponseEventsItemFortyFiveDataCanLeaveGroup] = pydantic.Field(
        default=None
    )
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to leave this group. Only present if this user group
    permission setting changed.
    
    **Changes**: New in Zulip 10.0 (feature level 308).
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    """

    can_manage_group: typing.Optional[GetEventsResponseEventsItemFortyFiveDataCanManageGroup] = pydantic.Field(
        default=None
    )
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to [manage this group][manage-user-groups]. Only present
    if this user group permission setting changed.
    
    **Changes**: New in Zulip 10.0 (feature level 283).
    
    Will be one of the following:
    
    [setting-values]: /api/group-setting-values
    [manage-user-groups]: /help/manage-user-groups
    """

    can_mention_group: typing.Optional[GetEventsResponseEventsItemFortyFiveDataCanMentionGroup] = pydantic.Field(
        default=None
    )
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to [mention this user group][mentions]. Only present
    if this user group permission setting changed.
    
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

    can_remove_members_group: typing.Optional[GetEventsResponseEventsItemFortyFiveDataCanRemoveMembersGroup] = (
        pydantic.Field(default=None)
    )
    """
    A [group-setting value][setting-values] defining the set of users who
    have permission to remove members from this group. Only present if this
    user group permission setting changed.
    
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



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_user_group_request_can_remove_members_group_new import UpdateUserGroupRequestCanRemoveMembersGroupNew
from .update_user_group_request_can_remove_members_group_old import UpdateUserGroupRequestCanRemoveMembersGroupOld


class UpdateUserGroupRequestCanRemoveMembersGroup(UniversalBaseModel):
    """
    The set of users who have permission to remove members from this user group
    expressed as an [update to a group-setting value][update-group-setting].

    **Changes**: New in Zulip 10.0 (feature level 324). Previously, this
    permission was controlled by the `can_manage_group` setting.

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values
    [system-groups]: /api/group-setting-values#system-groups
    """

    new: UpdateUserGroupRequestCanRemoveMembersGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateUserGroupRequestCanRemoveMembersGroupOld] = pydantic.Field(default=None)
    """
    The expected current [group-setting value](/api/group-setting-values)
    for who has this permission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

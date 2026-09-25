

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_user_group_request_can_manage_group_new import UpdateUserGroupRequestCanManageGroupNew
from .update_user_group_request_can_manage_group_old import UpdateUserGroupRequestCanManageGroupOld


class UpdateUserGroupRequestCanManageGroup(UniversalBaseModel):
    """
    The set of users who have permission to [manage this user group][manage-user-groups]
    expressed as an [update to a group-setting value][update-group-setting].

    This setting cannot be set to `"role:internet"` and `"role:everyone"`
    [system groups][system-groups].

    **Changes**: New in Zulip 10.0 (feature level 283).

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values
    [system-groups]: /api/group-setting-values#system-groups
    [manage-user-groups]: /help/manage-user-groups
    """

    new: UpdateUserGroupRequestCanManageGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateUserGroupRequestCanManageGroupOld] = pydantic.Field(default=None)
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



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_user_group_request_can_mention_group_new import UpdateUserGroupRequestCanMentionGroupNew
from .update_user_group_request_can_mention_group_old import UpdateUserGroupRequestCanMentionGroupOld


class UpdateUserGroupRequestCanMentionGroup(UniversalBaseModel):
    """
    The set of users who have permission to [mention this group][mentions],
    expressed as an [update to a group-setting value][update-group-setting].

    This setting cannot be set to `"role:internet"` and `"role:owners"`
    [system groups][system-groups].

    **Changes**: In Zulip 9.0 (feature level 260), this parameter was
    updated to only accept an object with the `old` and `new` fields
    described below. Prior to this feature level, this parameter could be
    either of the two forms of a [group-setting value][setting-values].

    Before Zulip 9.0 (feature level 258), this parameter could only be the
    integer form of a [group-setting value][setting-values].

    Before Zulip 8.0 (feature level 198), this parameter was named
    `can_mention_group_id`.

    New in Zulip 8.0 (feature level 191). Previously, groups could be
    mentioned only if they were not [system groups][system-groups].

    [mentions]: /help/mention-a-user-or-group
    [update-group-setting]: /api/group-setting-values#updating-group-setting-values
    [system-groups]: /api/group-setting-values#system-groups
    [setting-values]: /api/group-setting-values
    """

    new: UpdateUserGroupRequestCanMentionGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateUserGroupRequestCanMentionGroupOld] = pydantic.Field(default=None)
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

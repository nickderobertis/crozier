

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_add_subscribers_group_new import UpdateStreamRequestCanAddSubscribersGroupNew
from .update_stream_request_can_add_subscribers_group_old import UpdateStreamRequestCanAddSubscribersGroupOld


class UpdateStreamRequestCanAddSubscribersGroup(UniversalBaseModel):
    """
    The set of users who have permission to add subscribers to this
    channel expressed as an [update to a group-setting
    value][update-group-setting].

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values

    Users who can administer the channel or have similar realm-level
    permissions can add subscribers to a public channel regardless
    of the value of this setting.

    Users in this group need not be subscribed to a private channel to
    add subscribers to it.

    Note that a user must [have content access](/help/channel-permissions)
    to a channel and permission to administer the channel in order to
    modify this setting.

    **Changes**: New in Zulip 10.0 (feature level 342). Previously, there was no
    channel-level setting for this permission.
    """

    new: UpdateStreamRequestCanAddSubscribersGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanAddSubscribersGroupOld] = pydantic.Field(default=None)
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

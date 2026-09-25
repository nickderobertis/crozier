

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_administer_channel_group_new import UpdateStreamRequestCanAdministerChannelGroupNew
from .update_stream_request_can_administer_channel_group_old import UpdateStreamRequestCanAdministerChannelGroupOld


class UpdateStreamRequestCanAdministerChannelGroup(UniversalBaseModel):
    """
    The set of users who have permission to administer this channel
    expressed as an [update to a group-setting value][update-group-setting].

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values

    Organization administrators can administer every channel as though they were
    in this group without being explicitly listed here.

    Note that a user must [have content access](/help/channel-permissions) to a
    channel in order to add other subscribers to the channel.

    **Changes**: Prior to Zulip 10.0 (feature level 349) a user needed to
    [have content access](/help/channel-permissions) to a channel in order
    to modify it. The exception to this rule was that organization
    administrators can edit channel names and descriptions without having
    full access to the channel.

    New in Zulip 10.0 (feature level 325). Prior to this
    change, the permission to administer channels was limited to realm
    administrators.
    """

    new: UpdateStreamRequestCanAdministerChannelGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanAdministerChannelGroupOld] = pydantic.Field(default=None)
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

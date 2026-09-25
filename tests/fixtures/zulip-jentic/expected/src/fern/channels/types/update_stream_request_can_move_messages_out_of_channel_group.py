

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_move_messages_out_of_channel_group_new import (
    UpdateStreamRequestCanMoveMessagesOutOfChannelGroupNew,
)
from .update_stream_request_can_move_messages_out_of_channel_group_old import (
    UpdateStreamRequestCanMoveMessagesOutOfChannelGroupOld,
)


class UpdateStreamRequestCanMoveMessagesOutOfChannelGroup(UniversalBaseModel):
    """
    The set of users who have permission to move messages out of this channel
    expressed as an [update to a group-setting value][update-group-setting].

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values

    Note that a user must [have content access](/help/channel-permissions) to a
    channel in order to move messages out of the channel.

    Channel administrators and users present in the organization-level
    `can_move_messages_between_channels_group` setting can always move messages
    out of the channel if they [have content access](/help/channel-permissions) to
    the channel.

    **Changes**: New in Zulip 11.0 (feature level 396). Prior to this
    change, only the users in `can_move_messages_between_channels_group` were able
    move messages between channels.
    """

    new: UpdateStreamRequestCanMoveMessagesOutOfChannelGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanMoveMessagesOutOfChannelGroupOld] = pydantic.Field(default=None)
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

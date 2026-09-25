

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_move_messages_within_channel_group_new import (
    UpdateStreamRequestCanMoveMessagesWithinChannelGroupNew,
)
from .update_stream_request_can_move_messages_within_channel_group_old import (
    UpdateStreamRequestCanMoveMessagesWithinChannelGroupOld,
)


class UpdateStreamRequestCanMoveMessagesWithinChannelGroup(UniversalBaseModel):
    """
    The set of users who have permission to move messages within this channel
    expressed as an [update to a group-setting value][update-group-setting].

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values

    Note that a user must [have content access](/help/channel-permissions) to a
    channel in order to move messages within the channel.

    Channel administrators and users present in the organization-level
    `can_move_messages_between_topics_group` setting can always move messages
    within the channel if they [have content access](/help/channel-permissions) to
    the channel.

    **Changes**: New in Zulip 11.0 (feature level 396). Prior to this
    change, only the users in `can_move_messages_between_topics_group` were able
    move messages between topics of a channel.
    """

    new: UpdateStreamRequestCanMoveMessagesWithinChannelGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanMoveMessagesWithinChannelGroupOld] = pydantic.Field(default=None)
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

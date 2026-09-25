

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_create_topic_group_new import UpdateStreamRequestCanCreateTopicGroupNew
from .update_stream_request_can_create_topic_group_old import UpdateStreamRequestCanCreateTopicGroupOld


class UpdateStreamRequestCanCreateTopicGroup(UniversalBaseModel):
    """
    The set of users who have permission to create new topics in this channel
    expressed as an [update to a group-setting value][update-group-setting].

    Note that using this permission requires also having permission to send
    messages in the channel.

    For [private channels with protected history](/help/channel-permissions#private-channels),
    this setting can only be set to `role:everyone` [system group][system-groups].

    **Changes**: New in Zulip 12.0 (feature level 441). Previously, if you
    could send messages in a channel, you could create topics in the channel.

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values
    [system-groups]: /api/group-setting-values#system-groups
    """

    new: UpdateStreamRequestCanCreateTopicGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanCreateTopicGroupOld] = pydantic.Field(default=None)
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

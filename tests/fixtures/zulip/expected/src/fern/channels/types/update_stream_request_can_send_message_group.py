

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_stream_request_can_send_message_group_new import UpdateStreamRequestCanSendMessageGroupNew
from .update_stream_request_can_send_message_group_old import UpdateStreamRequestCanSendMessageGroupOld


class UpdateStreamRequestCanSendMessageGroup(UniversalBaseModel):
    """
    The set of users who have permission to post in this channel
    expressed as an [update to a group-setting value][update-group-setting].

    [update-group-setting]: /api/group-setting-values#updating-group-setting-values

    Note that a user must have metadata access to a channel and permission
    to administer the channel in order to modify this setting.

    Note that using this permission to send a message to a new topic requires
    also having permission to create new topics in the channel.

    **Changes**: New in Zulip 10.0 (feature level 333). Previously
    `stream_post_policy` field used to control the permission to
    post in the channel.
    """

    new: UpdateStreamRequestCanSendMessageGroupNew = pydantic.Field()
    """
    The new [group-setting value](/api/group-setting-values) for who would
    have this permission.
    """

    old: typing.Optional[UpdateStreamRequestCanSendMessageGroupOld] = pydantic.Field(default=None)
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

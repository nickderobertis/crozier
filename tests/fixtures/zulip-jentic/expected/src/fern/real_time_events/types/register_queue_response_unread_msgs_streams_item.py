

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseUnreadMsgsStreamsItem(UniversalBaseModel):
    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    The topic under which the messages were sent.
    
    Note that the empty string topic may have been rewritten by the server
    to the value of `realm_empty_topic_display_name` found in the
    [`POST /register`](/api/register-queue) response depending on the value
    of the `empty_topic_name` [client capability][client-capabilities].
    
    **Changes**: The `empty_topic_name` client capability is new in
    Zulip 10.0 (feature level 334).
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the channel to which the messages were sent.
    """

    unread_message_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The message IDs of the recent unread messages sent in this channel,
    sorted in ascending order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

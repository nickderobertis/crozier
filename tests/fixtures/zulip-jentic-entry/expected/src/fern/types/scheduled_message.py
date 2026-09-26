

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_message_to import ScheduledMessageTo
from .scheduled_message_type import ScheduledMessageType


class ScheduledMessage(UniversalBaseModel):
    scheduled_message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique ID of the scheduled message, which can be used to
    modify or delete the scheduled message.
    
    This is different from the unique ID that the message will have
    after it is sent.
    """

    type: typing.Optional[ScheduledMessageType] = pydantic.Field(default=None)
    """
    The type of the scheduled message. Either `"stream"` or `"private"`.
    """

    to: typing.Optional[ScheduledMessageTo] = pydantic.Field(default=None)
    """
    The scheduled message's tentative target audience.
    
    For channel messages, it will be the unique ID of the target
    channel. For direct messages, it will be an array with the
    target users' IDs.
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Only present if `type` is `"stream"`.
    
    The topic for the channel message.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content/body of the scheduled message, in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    rendered_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content/body of the scheduled message rendered in HTML.
    """

    scheduled_delivery_timestamp: typing.Optional[int] = pydantic.Field(default=None)
    """
    The UNIX timestamp for when the message will be sent
    by the server, in UTC seconds.
    """

    failed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the server has tried to send the scheduled message
    and it failed to successfully send.
    
    Clients that support unscheduling and editing scheduled messages
    should display scheduled messages with `"failed": true` with an
    indicator that the server failed to send the message at the
    scheduled time, so that the user is aware of the failure and can
    get the content of the scheduled message.
    
    **Changes**: New in Zulip 7.0 (feature level 181).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

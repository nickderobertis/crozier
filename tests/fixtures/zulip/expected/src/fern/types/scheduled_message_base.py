

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .scheduled_message_base_to import ScheduledMessageBaseTo
from .scheduled_message_base_type import ScheduledMessageBaseType


class ScheduledMessageBase(UniversalBaseModel):
    """
    Object containing details of the scheduled message.
    """

    scheduled_message_id: int = pydantic.Field()
    """
    The unique ID of the scheduled message, which can be used to
    modify or delete the scheduled message.
    
    This is different from the unique ID that the message will have
    after it is sent.
    """

    type: ScheduledMessageBaseType = pydantic.Field()
    """
    The type of the scheduled message. Either `"stream"` or `"private"`.
    """

    to: ScheduledMessageBaseTo = pydantic.Field()
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

    content: str = pydantic.Field()
    """
    The content/body of the scheduled message, in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    rendered_content: str = pydantic.Field()
    """
    The content/body of the scheduled message rendered in HTML.
    """

    scheduled_delivery_timestamp: int = pydantic.Field()
    """
    The UNIX timestamp for when the message will be sent
    by the server, in UTC seconds.
    """

    failed: bool = pydantic.Field()
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

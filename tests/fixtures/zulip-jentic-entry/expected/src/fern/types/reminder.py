

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reminder_type import ReminderType


class Reminder(UniversalBaseModel):
    """
    Object containing details of the scheduled message.
    """

    reminder_id: int = pydantic.Field()
    """
    The unique ID of the reminder, which can be used to
    delete the reminder.
    
    This is different from the unique ID that the message would have
    after being sent.
    """

    type: ReminderType = pydantic.Field()
    """
    The type of the reminder. Always set to `"private"`.
    """

    to: typing.List[int] = pydantic.Field()
    """
    Contains the ID of the user who scheduled the reminder,
    and to which the reminder will be sent.
    """

    content: str = pydantic.Field()
    """
    The content/body of the reminder, in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    rendered_content: str = pydantic.Field()
    """
    The content/body of the reminder rendered in HTML.
    """

    scheduled_delivery_timestamp: int = pydantic.Field()
    """
    The UNIX timestamp for when the message will be sent
    by the server, in UTC seconds.
    """

    failed: bool = pydantic.Field()
    """
    Whether the server has tried to send the reminder
    and it failed to successfully send.
    
    Clients that support unscheduling reminders
    should display scheduled messages with `"failed": true` with an
    indicator that the server failed to send the message at the
    scheduled time, so that the user is aware of the failure and can
    get the content of the scheduled message.
    """

    reminder_target_message_id: int = pydantic.Field()
    """
    The ID of the message that the reminder is created for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

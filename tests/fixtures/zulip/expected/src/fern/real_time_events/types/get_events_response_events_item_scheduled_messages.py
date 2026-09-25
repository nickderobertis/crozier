

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.scheduled_message import ScheduledMessage
from .get_events_response_events_item_scheduled_messages_op import GetEventsResponseEventsItemScheduledMessagesOp
from .get_events_response_events_item_scheduled_messages_type import GetEventsResponseEventsItemScheduledMessagesType


class GetEventsResponseEventsItemScheduledMessages(UniversalBaseModel):
    """
    Event sent to a user's clients when scheduled messages
    are created.

    **Changes**: New in Zulip 7.0 (feature level 179).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemScheduledMessagesType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemScheduledMessagesOp] = None
    scheduled_messages: typing.Optional[typing.List[ScheduledMessage]] = pydantic.Field(default=None)
    """
    An array of objects containing details of the newly created
    scheduled messages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

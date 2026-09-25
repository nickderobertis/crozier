

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.scheduled_message import ScheduledMessage
from .get_events_response_events_item_scheduled_message_op import GetEventsResponseEventsItemScheduledMessageOp
from .get_events_response_events_item_scheduled_message_type import GetEventsResponseEventsItemScheduledMessageType


class GetEventsResponseEventsItemScheduledMessage(UniversalBaseModel):
    """
    Event sent to a user's clients when a scheduled message
    is edited.

    **Changes**: New in Zulip 7.0 (feature level 179).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemScheduledMessageType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemScheduledMessageOp] = None
    scheduled_message: typing.Optional[ScheduledMessage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

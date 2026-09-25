

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_scheduled_message_id_op import GetEventsResponseEventsItemScheduledMessageIdOp
from .get_events_response_events_item_scheduled_message_id_type import GetEventsResponseEventsItemScheduledMessageIdType


class GetEventsResponseEventsItemScheduledMessageId(UniversalBaseModel):
    """
    Event sent to a user's clients when a scheduled message
    is deleted.

    **Changes**: New in Zulip 7.0 (feature level 179).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemScheduledMessageIdType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemScheduledMessageIdOp] = None
    scheduled_message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the scheduled message that was deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

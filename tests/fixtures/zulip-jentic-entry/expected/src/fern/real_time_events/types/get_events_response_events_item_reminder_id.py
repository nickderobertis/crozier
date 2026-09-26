

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_reminder_id_op import GetEventsResponseEventsItemReminderIdOp
from .get_events_response_events_item_reminder_id_type import GetEventsResponseEventsItemReminderIdType


class GetEventsResponseEventsItemReminderId(UniversalBaseModel):
    """
    Event sent to a user's clients when a reminder
    is deleted.

    **Changes**: New in Zulip 11.0 (feature level 399).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemReminderIdType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemReminderIdOp] = None
    reminder_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the reminder that was deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

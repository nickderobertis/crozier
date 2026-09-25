

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.reminder import Reminder
from .get_events_response_events_item_reminders_op import GetEventsResponseEventsItemRemindersOp
from .get_events_response_events_item_reminders_type import GetEventsResponseEventsItemRemindersType


class GetEventsResponseEventsItemReminders(UniversalBaseModel):
    """
    Event sent to a user's clients when a reminder is scheduled.

    **Changes**: New in Zulip 11.0 (feature level 399).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemRemindersType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemRemindersOp] = None
    reminders: typing.Optional[typing.List[Reminder]] = pydantic.Field(default=None)
    """
    An array of objects containing details of the newly created
    reminders.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

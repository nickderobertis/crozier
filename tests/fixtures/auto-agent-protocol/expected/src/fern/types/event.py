

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_event_kind import EventEventKind
from .event_type import EventType


class Event(UniversalBaseModel):
    """
    Minimal AAP event envelope. Used for asynchronous status updates (e.g. lead status changes, appointment confirmations) delivered via A2A push notifications or task status update events.
    """

    type: EventType
    event_kind: EventEventKind = pydantic.Field()
    """
    Concrete event kind. v1.0 defines two kinds; future versions may add more.
    """

    entity_id: str = pydantic.Field()
    """
    Identifier of the affected entity (lead_id or appointment_id).
    """

    status: str = pydantic.Field()
    """
    New status value for the entity. For 'lead.status_changed', one of: received | duplicate | rejected | working | sold_to | lost. For 'appointment.status_changed', one of: requested | proposed | confirmed | rejected | completed | no_show. Conditional `if/then` clauses below enforce the right subset for each `event_kind`.
    """

    occurred_at: dt.datetime = pydantic.Field()
    """
    ISO 8601 / RFC 3339 timestamp at which the event occurred (e.g. '2026-04-30T10:15:30Z'). MUST include a timezone offset (Z or ±HH:MM).
    """

    payload: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Optional event-specific payload. Schema is event-kind-dependent and dealer-defined.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

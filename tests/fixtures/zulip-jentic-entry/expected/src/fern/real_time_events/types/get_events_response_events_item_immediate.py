

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_immediate_type import GetEventsResponseEventsItemImmediateType


class GetEventsResponseEventsItemImmediate(UniversalBaseModel):
    """
    An event which signals the official Zulip web/desktop app to update,
    by reloading the page and fetching a new queue; this will generally
    follow a `restart` event. Clients which do not obtain their code
    from the server (e.g. mobile and terminal clients, which store their
    code locally) should ignore this event.

    Clients choosing to reload the application must implement a random
    delay strategy to spread such restarts over 5 or more minutes to
    avoid creating a synchronized thundering herd effect.

    **Changes**: New in Zulip 9.0 (feature level 240).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemImmediateType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    immediate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the client should fetch a new event queue immediately,
    rather than using a backoff strategy to avoid thundering herds.
    A Zulip development server uses this parameter to reload
    clients immediately.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

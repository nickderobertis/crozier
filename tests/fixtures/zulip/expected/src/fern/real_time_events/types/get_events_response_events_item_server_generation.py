

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_server_generation_type import GetEventsResponseEventsItemServerGenerationType


class GetEventsResponseEventsItemServerGeneration(UniversalBaseModel):
    """
    Event sent to all the users whenever the Zulip server restarts.

    Specifically, this event is sent whenever the Tornado process
    for the user is restarted; in particular, this will always happen
    when the Zulip server is upgraded.

    Clients should use this event to update their tracking of the
    server's capabilities, and to decide if they wish to get a new
    event queue after a server upgrade. Clients doing so must
    implement a random delay strategy to spread such restarts over 5
    minutes or more to avoid creating a synchronized thundering herd
    effect.

    **Changes**: Removed the `immediate` flag, which was only used by
    web clients in development, in Zulip 9.0 (feature level 240).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemServerGenerationType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    zulip_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Zulip version number, in the format where this appears
    in the [server_settings](/api/get-server-settings) and
    [register](/api/register-queue) responses.
    
    **Changes**: New in Zulip 4.0 (feature level 59).
    """

    zulip_merge_base: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Zulip merge base number, in the format where this appears
    in the [server_settings](/api/get-server-settings) and
    [register](/api/register-queue) responses.
    
    **Changes**: New in Zulip 5.0 (feature level 88).
    """

    zulip_feature_level: typing.Optional[int] = pydantic.Field(default=None)
    """
    The [Zulip feature level](/api/changelog) of the server
    after the restart.
    
    Clients should use this to update their tracking of the
    server's capabilities, and may choose to refetch their state
    and create a new event queue when the API feature level has
    changed in a way that the client finds significant. Clients
    choosing to do so must implement a random delay strategy to
    spread such restarts over 5 or more minutes to avoid creating
    a synchronized thundering herd effect.
    
    **Changes**: New in Zulip 4.0 (feature level 59).
    """

    server_generation: typing.Optional[int] = pydantic.Field(default=None)
    """
    The timestamp at which the server started.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

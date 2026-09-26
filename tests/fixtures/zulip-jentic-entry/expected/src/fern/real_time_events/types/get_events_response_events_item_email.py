

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.modern_presence_format import ModernPresenceFormat
from .get_events_response_events_item_email_presence_value import GetEventsResponseEventsItemEmailPresenceValue
from .get_events_response_events_item_email_type import GetEventsResponseEventsItemEmailType


class GetEventsResponseEventsItemEmail(UniversalBaseModel):
    """
    Event sent to all users in an organization when a user comes back
    online after being offline for a while.

    In addition to handling these events, a client that wants to
    maintain presence data must poll the [main presence
    endpoint](https://zulip.com/api/get-presence). Most updates to
    presence data, refreshing the timestamps of users who are already
    online, do not appear in the event queue. This design is an
    optimization by allowing those updates to be batched up, because
    there is no urgency in the information that an already-online user
    is still online.

    These events are provided because when a user transitions from
    offline to online, that is information the client may want to show
    promptly in the UI to avoid showing a confusing state (for example,
    if the newly-online user sends a message or otherwise demonstrates
    they're online).

    If the client supports the `simplified_presence_events` [client
    capability](/api/register-queue#parameter-client_capabilities),
    these events will include the `presences` field, which provides the
    modified user's presence data in the modern format. Clients are
    strongly encouraged to implement this client capability, as legacy
    format support will be removed in a future release.

    If the `CAN_ACCESS_ALL_USERS_GROUP_LIMITS_PRESENCE` server-level
    setting is set to `true`, then the event is only sent to users
    who can access the user who came back online.

    **Changes**: Prior to Zulip 11.0 (feature level 419), the
    `simplified_presence_events` client capability did not exist.
    Therefore, all events were in the legacy format, and did not
    include the `presences` field.

    Prior to Zulip 8.0 (feature level 228), this event was sent to all
    users in the organization.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemEmailType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    presences: typing.Optional[typing.Dict[str, ModernPresenceFormat]] = pydantic.Field(default=None)
    """
    Only present for clients that support the `simplified_presence_events`
    [client capability](/api/register-queue#parameter-client_capabilities).
    
    A dictionary mapping user IDs to the presence data (modern
    format) for the modified user(s). Clients should support
    updating multiple users in a single event.
    
    **Changes**: New in Zulip 11.0 (feature level 419).
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Not present for clients that support the `simplified_presence_events`
    [client capability](/api/register-queue#parameter-client_capabilities).
    
    The ID of the modified user.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Not present for clients that support the `simplified_presence_events`
    [client capability](/api/register-queue#parameter-client_capabilities).
    
    The Zulip API email of the user.
    
    **Deprecated**: This field will be removed in a future
    release as it is redundant with the `user_id`.
    """

    server_timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    Not present for clients that support the `simplified_presence_events`
    [client capability](/api/register-queue#parameter-client_capabilities).
    
    The timestamp of when the Zulip server received the user's
    presence as a UNIX timestamp.
    """

    presence: typing.Optional[typing.Dict[str, GetEventsResponseEventsItemEmailPresenceValue]] = pydantic.Field(
        default=None
    )
    """
    Not present for clients that support the `simplified_presence_events`
    [client capability](/api/register-queue#parameter-client_capabilities).
    
    Object containing the presence data (legacy format) of of the modified
    user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

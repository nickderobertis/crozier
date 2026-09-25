

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.user import User
from .get_events_response_events_item_eleven_op import GetEventsResponseEventsItemElevenOp
from .get_events_response_events_item_eleven_type import GetEventsResponseEventsItemElevenType


class GetEventsResponseEventsItemEleven(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when a new
    user joins or when a guest user gains access to a user.
    Processing this event is important to being able to display
    basic details on other users given only their ID.

    If the current user is a guest whose access to a newly created user
    is limited by a `can_access_all_users_group` policy, and the event
    queue was registered with the `user_list_incomplete` client
    capability, then the event queue will not receive an event for such
    a new user. If a newly created user is inaccessible to the current
    user via such a policy, but the client lacks `user_list_incomplete`
    client capability, then this event will be delivered to the queue,
    with an "Unknown user" object with the usual format but placeholder
    data whose only variable content is the user ID.

    **Changes**: Before Zulip 8.0 (feature level 232), the
    `user_list_incomplete` client capability did not exist, and so all
    clients whose access to a new user was prevented by
    `can_access_all_users_group` policy would receive a fake "Unknown
    user" event for such a user.

    Starting with Zulip 8.0 (feature level 228),
    this event is also sent when a guest user gains access to
    a user.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemElevenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemElevenOp] = None
    person: typing.Optional[User] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

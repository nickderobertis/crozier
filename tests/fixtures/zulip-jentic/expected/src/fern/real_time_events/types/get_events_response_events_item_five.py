

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_five_op import GetEventsResponseEventsItemFiveOp
from .get_events_response_events_item_five_type import GetEventsResponseEventsItemFiveType
from .get_events_response_events_item_five_value import GetEventsResponseEventsItemFiveValue


class GetEventsResponseEventsItemFive(UniversalBaseModel):
    """
    Event sent to a user's clients when a property of the user's
    subscription to a channel has been updated. This event is used
    only for personal properties like `is_muted` or `pin_to_top`.
    See the [`stream op: update` event](/api/get-events#stream-update)
    for updates to global properties of a channel.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFiveType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFiveOp] = None
    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the channel whose subscription details have changed.
    """

    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    The property of the subscription which has changed. For details on the
    various subscription properties that a user can change, see
    [POST /users/me/subscriptions/properties](/api/update-subscription-settings).
    
    Clients should generally handle an unknown property received here without
    crashing, since that will naturally happen when connecting to a Zulip
    server running a new version that adds a new subscription property.
    
    **Changes**: As of Zulip 6.0 (feature level 139), updates to the `is_muted`
    property or the deprecated `in_home_view` property will send two `subscription`
    update events, one for each property, to support clients fully migrating to
    use the `is_muted` property. Prior to this feature level, updates to either
    property only sent one event with the deprecated `in_home_view` property.
    """

    value: typing.Optional[GetEventsResponseEventsItemFiveValue] = pydantic.Field(default=None)
    """
    The new value of the changed property.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

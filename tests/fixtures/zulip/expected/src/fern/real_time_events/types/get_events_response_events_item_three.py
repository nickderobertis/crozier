

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.subscription import Subscription
from .get_events_response_events_item_three_op import GetEventsResponseEventsItemThreeOp
from .get_events_response_events_item_three_type import GetEventsResponseEventsItemThreeType


class GetEventsResponseEventsItemThree(UniversalBaseModel):
    """
    Event sent to a user's clients when that user's channel subscriptions
    have changed (either the set of subscriptions or their properties).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemThreeType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemThreeOp] = None
    subscriptions: typing.Optional[typing.List[Subscription]] = pydantic.Field(default=None)
    """
    A list of dictionaries where each dictionary contains
    information about one of the subscribed channels.
    
    **Changes**: Removed `email_address` field from the dictionary
    in Zulip 8.0 (feature level 226).
    
    Removed `role` field from the dictionary
    in Zulip 6.0 (feature level 133).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

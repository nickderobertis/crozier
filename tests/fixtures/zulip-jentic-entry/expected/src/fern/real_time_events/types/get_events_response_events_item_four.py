

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_four_op import GetEventsResponseEventsItemFourOp
from .get_events_response_events_item_four_subscriptions_item import GetEventsResponseEventsItemFourSubscriptionsItem
from .get_events_response_events_item_four_type import GetEventsResponseEventsItemFourType


class GetEventsResponseEventsItemFour(UniversalBaseModel):
    """
    Event sent to a user's clients when that user has been unsubscribed
    from one or more channels.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFourType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFourOp] = None
    subscriptions: typing.Optional[typing.List[GetEventsResponseEventsItemFourSubscriptionsItem]] = pydantic.Field(
        default=None
    )
    """
    A list of dictionaries, where each dictionary contains
    information about one of the newly unsubscribed channels.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

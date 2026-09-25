

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_muted_topics_muted_topics_item_item import (
    GetEventsResponseEventsItemMutedTopicsMutedTopicsItemItem,
)
from .get_events_response_events_item_muted_topics_type import GetEventsResponseEventsItemMutedTopicsType


class GetEventsResponseEventsItemMutedTopics(UniversalBaseModel):
    """
    Event sent to a user's clients when that user's set of
    configured muted topics have changed.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemMutedTopicsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    muted_topics: typing.Optional[
        typing.List[typing.List[GetEventsResponseEventsItemMutedTopicsMutedTopicsItemItem]]
    ] = pydantic.Field(default=None)
    """
    Array of tuples, where each tuple describes a muted topic.
    The first element of the tuple is the channel name in which the topic
    has to be muted, the second element is the topic name to be muted
    and the third element is an integer UNIX timestamp representing
    when the topic was muted.
    
    **Changes**: Deprecated in Zulip 6.0 (feature level
    134). Starting with this version, clients that explicitly
    requested the replacement `user_topic` event type when
    registering their event queue will not receive this legacy
    event type.
    
    Before Zulip 3.0 (feature level 1), the `muted_topics`
    array objects were 2-item tuples and did not include the timestamp
    information for when the topic was muted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

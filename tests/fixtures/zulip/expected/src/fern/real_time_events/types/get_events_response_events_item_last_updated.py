

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_last_updated_type import GetEventsResponseEventsItemLastUpdatedType


class GetEventsResponseEventsItemLastUpdated(UniversalBaseModel):
    """
    Event sent to a user's clients when the user mutes/unmutes
    a topic, or otherwise modifies their personal per-topic
    configuration.

    **Changes**: New in Zulip 6.0 (feature level 134). Previously,
    clients were notified about changes in muted topic
    configuration via the `muted_topics` event type.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemLastUpdatedType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the channel to which the topic belongs.
    """

    topic_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the topic.
    
    For clients that don't support the `empty_topic_name` [client capability][client-capabilities],
    if the actual topic name is empty string, this field's value will instead
    be the value of `realm_empty_topic_display_name` found in the
    [`POST /register`](/api/register-queue) response.
    
    **Changes**: Before 10.0 (feature level 334), `empty_topic_name`
    client capability didn't exist and empty string as the topic name for
    channel messages wasn't allowed.
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    last_updated: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer UNIX timestamp representing when the user-topic
    relationship was last changed.
    """

    visibility_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer indicating the user's visibility
    preferences for the topic, such as whether the topic
    is muted.
    
    - 0 = None. Used to indicate that the user no
      longer has a special visibility policy for this topic.
    - 1 = Muted. Used to record [muted topics](/help/mute-a-topic).
    - 2 = Unmuted. Used to record unmuted topics.
    - 3 = Followed. Used to record [followed topics](/help/follow-a-topic).
    
    **Changes**: In Zulip 7.0 (feature level 219), added followed as
    a visibility policy option.
    
    In Zulip 7.0 (feature level 170), added unmuted as a visibility
    policy option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

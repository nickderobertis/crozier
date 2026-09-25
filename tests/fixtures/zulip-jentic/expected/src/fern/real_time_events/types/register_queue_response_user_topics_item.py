

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegisterQueueResponseUserTopicsItem(UniversalBaseModel):
    """
    Object describing the user's configuration for a given topic.
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the channel to which the topic belongs.
    """

    topic_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the topic.
    
    Note that the empty string topic may have been rewritten by the server to
    the value of `realm_empty_topic_display_name` found in the [`POST /register`](/api/register-queue)
    response depending on the value of the `empty_topic_name` [client capability][client-capabilities].
    
    **Changes**: The `empty_topic_name` client capability is new in
    Zulip 10.0 (feature level 334).
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    last_updated: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer UNIX timestamp representing when the user-topic
    relationship was changed.
    """

    visibility_policy: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer indicating the user's visibility configuration for
    the topic.
    
    - 1 = Muted. Used to record [muted topics](/help/mute-a-topic).
    - 2 = Unmuted. Used to record [unmuted topics](/help/mute-a-topic).
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

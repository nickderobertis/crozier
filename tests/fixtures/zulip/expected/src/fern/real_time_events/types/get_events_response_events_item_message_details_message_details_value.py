

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_events_response_events_item_message_details_message_details_value_type import (
    GetEventsResponseEventsItemMessageDetailsMessageDetailsValueType,
)


class GetEventsResponseEventsItemMessageDetailsMessageDetailsValue(UniversalBaseModel):
    """
    `{message_id}`: Object containing details about the
    message with the specified ID.
    """

    type: GetEventsResponseEventsItemMessageDetailsMessageDetailsValueType = pydantic.Field()
    """
    The type of this message. Either `"stream"` or `"private"`.
    """

    mentioned: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A flag which indicates whether the message contains a mention
    of the user.
    
    Present only if the message mentions the current user.
    """

    user_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Present only if `type` is `private`.
    
    The user IDs of every recipient of this direct message, excluding yourself.
    Will be the empty list for a message you had sent to only yourself.
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Present only if `type` is `"stream"`.
    
    The ID of the channel where the message was sent.
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present only if `type` is `"stream"`.
    
    Name of the topic where the message was sent.
    
    For clients that don't support the `empty_topic_name` [client capability][client-capabilities],
    if the actual topic name is empty string, this field's value will instead
    be the value of `realm_empty_topic_display_name` found in the
    [`POST /register`](/api/register-queue) response.
    
    **Changes**: Before 10.0 (feature level 334), `empty_topic_name`
    client capability didn't exist and empty string as the topic name for
    channel messages wasn't allowed.
    
    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    unmuted_stream_msg: typing.Optional[bool] = pydantic.Field(default=None)
    """
    **Deprecated** internal implementation detail. Clients should
    ignore this field as it will be removed in the future.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

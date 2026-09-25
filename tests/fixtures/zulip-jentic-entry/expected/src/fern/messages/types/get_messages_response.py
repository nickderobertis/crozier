

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_messages_response_messages_item import GetMessagesResponseMessagesItem


class GetMessagesResponse(UniversalBaseModel):
    result: typing.Any
    msg: typing.Any
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    anchor: typing.Optional[int] = pydantic.Field(default=None)
    """
    The same `anchor` specified in the request (or the computed one, if
    `use_first_unread_anchor` is `true`).
    
    Only present if `message_ids` is not provided.
    """

    found_newest: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the server promises that the `messages` list includes the very
    newest messages matching the narrow (used by clients that paginate their
    requests to decide whether there may be more messages to fetch).
    """

    found_oldest: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the server promises that the `messages` list includes the very
    oldest messages matching the narrow (used by clients that paginate their
    requests to decide whether there may be more messages to fetch).
    """

    found_anchor: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the anchor message is included in the
    response. If the message with the ID specified
    in the request does not exist, did not match
    the narrow, or was excluded via
    `"include_anchor": false`, this will be false.
    """

    history_limited: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the message history was limited due to
    plan restrictions. This flag is set to `true`
    only when the oldest messages(`found_oldest`)
    matching the narrow is fetched.
    """

    messages: typing.List[GetMessagesResponseMessagesItem] = pydantic.Field()
    """
    An array of `message` objects.
    
    **Changes**: In Zulip 3.1 (feature level 26), the
    `sender_short_name` field was removed from message
    objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_history_public_to_subscribers_op import (
    GetEventsResponseEventsItemHistoryPublicToSubscribersOp,
)
from .get_events_response_events_item_history_public_to_subscribers_type import (
    GetEventsResponseEventsItemHistoryPublicToSubscribersType,
)
from .get_events_response_events_item_history_public_to_subscribers_value import (
    GetEventsResponseEventsItemHistoryPublicToSubscribersValue,
)


class GetEventsResponseEventsItemHistoryPublicToSubscribers(UniversalBaseModel):
    """
    Event sent to all users who can see that a channel exists
    when a property of that channel changes. See
    [GET /streams](/api/get-streams#response) response
    for details on the various properties of a channel.

    This event is also sent when archiving or unarchiving a
    channel to all the users who can see that channel exists
    but only to the clients that declared the `archived_channels`
    [client capability][client-capabilities].

    **Changes**: Prior to Zulip 11.0 (feature level 378),
    this event was never sent when archiving or unarchiving
    a channel.

    Before Zulip 9.0 (feature level 256), this event was never
    sent when the `first_message_id` property of a channel was
    updated because the oldest message that had been sent to it
    changed.

    [client-capabilities]: /api/register-queue#parameter-client_capabilities
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemHistoryPublicToSubscribersType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemHistoryPublicToSubscribersOp] = None
    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the channel whose details have changed.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the channel whose details have changed.
    """

    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    The property of the channel which has changed. See
    [GET /streams](/api/get-streams#response) response for details
    on the various properties of a channel.
    
    Clients should handle an "unknown" property received here without
    crashing, since that can happen when connecting to a server running a
    newer version of Zulip with new features.
    """

    value: typing.Optional[GetEventsResponseEventsItemHistoryPublicToSubscribersValue] = pydantic.Field(default=None)
    """
    The new value of the changed property.
    
    **Changes**: Starting with Zulip 11.0 (feature level 389),
    this value can be `null` when a channel is removed from the folder.
    
    Starting with Zulip 10.0 (feature level 320), this
    field can be an object for `can_remove_subscribers_group` property,
    which is a [group-setting value][setting-values], when the setting
    is set to a combination of users and groups.
    
    [setting-values]: /api/group-setting-values
    """

    rendered_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Note: Only present if the changed property was `description`.
    
    The short description of the channel rendered as HTML, intended to
    be used when displaying the channel description in a UI.
    
    One should use the standard Zulip rendered_markdown CSS when
    displaying this content so that emoji, LaTeX, and other syntax
    work correctly. And any client-side security logic for
    user-generated message content should be applied when displaying
    this HTML as though it were the body of a Zulip message.
    
    See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.
    """

    history_public_to_subscribers: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Note: Only present if the changed property was `invite_only`.
    
    Whether the history of the channel is public to its subscribers.
    
    Currently always true for public channels (i.e. `"invite_only": false` implies
    `"history_public_to_subscribers": true`), but clients should not make that
    assumption, as we may change that behavior in the future.
    """

    is_web_public: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Note: Only present if the changed property was `invite_only`.
    
    Whether the channel's history is now readable by web-public spectators.
    
    **Changes**: New in Zulip 5.0 (feature level 71).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

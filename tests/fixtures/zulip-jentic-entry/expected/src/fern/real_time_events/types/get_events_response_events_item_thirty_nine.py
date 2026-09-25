

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_thirty_nine_op import GetEventsResponseEventsItemThirtyNineOp
from .get_events_response_events_item_thirty_nine_recipient import GetEventsResponseEventsItemThirtyNineRecipient
from .get_events_response_events_item_thirty_nine_type import GetEventsResponseEventsItemThirtyNineType


class GetEventsResponseEventsItemThirtyNine(UniversalBaseModel):
    """
    Event sent when a user starts editing a message.
    Event sent when a user starts typing in a textarea to edit the
    content of a message. See the [edit message typing notifications
    endpoint](/api/set-typing-status-for-message-edit).

    Clients requesting `typing_edit_message` event type that have
    `receives_typing_notifications` enabled will receive this event if
    they would have been notified if the message's content edit were to
    be saved (E.g., because they were a direct message recipient or
    are a subscribe to the channel).

    **Changes**: New in Zulip 10.0 (feature level 351). Previously,
    typing notifications were not available when editing messages.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemThirtyNineType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemThirtyNineOp] = None
    sender_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the user who is typing the edit of the
    message.
    
    Clients should be careful to display this user as the person who
    is typing, not that of the sender of the message, in case a
    collaborative editing feature be might be added in the future.
    """

    message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Indicates the message id of the message that is being edited.
    """

    recipient: typing.Optional[GetEventsResponseEventsItemThirtyNineRecipient] = pydantic.Field(default=None)
    """
    Object containing details about recipients of message edit typing notification.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

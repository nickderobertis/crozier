

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_emoji_id_data import GetEventsResponseEventsItemEmojiIdData
from .get_events_response_events_item_emoji_id_op import GetEventsResponseEventsItemEmojiIdOp
from .get_events_response_events_item_emoji_id_type import GetEventsResponseEventsItemEmojiIdType


class GetEventsResponseEventsItemEmojiId(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when
    a property of a [custom emoji](/help/custom-emoji) has
    been changed. Only the fields being updated are included
    in the event.

    Currently, the only property that can be updated is
    `deactivated`, but this may be extended in the future.

    Only sent to clients that set the
    `individual_emoji_changes` client capability.

    **Changes**: New in Zulip 12.0 (feature level 491),
    replacing half of the functionality of the
    `realm_emoji/update` event.
    """

    id: EventIdSchema
    type: GetEventsResponseEventsItemEmojiIdType = pydantic.Field()
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: GetEventsResponseEventsItemEmojiIdOp
    emoji_id: str = pydantic.Field()
    """
    The ID of the custom emoji being updated.
    """

    data: GetEventsResponseEventsItemEmojiIdData = pydantic.Field()
    """
    And object containing the properties that have changed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

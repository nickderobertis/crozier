

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.realm_emoji import RealmEmoji
from .get_events_response_events_item_emoji_op import GetEventsResponseEventsItemEmojiOp
from .get_events_response_events_item_emoji_type import GetEventsResponseEventsItemEmojiType


class GetEventsResponseEventsItemEmoji(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when
    a [custom emoji](/help/custom-emoji) has been added.

    Only sent to clients that set the
    `individual_emoji_changes` client capability.

    **Changes**: New in Zulip 12.0 (feature level 491),
    replacing half of the functionality of the
    `realm_emoji/update` event.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemEmojiType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemEmojiOp] = None
    emoji: typing.Optional[RealmEmoji] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

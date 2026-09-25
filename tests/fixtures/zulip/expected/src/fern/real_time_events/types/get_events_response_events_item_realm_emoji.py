

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.realm_emoji import RealmEmoji
from .get_events_response_events_item_realm_emoji_op import GetEventsResponseEventsItemRealmEmojiOp
from .get_events_response_events_item_realm_emoji_type import GetEventsResponseEventsItemRealmEmojiType


class GetEventsResponseEventsItemRealmEmoji(UniversalBaseModel):
    """
    Event sent to all users in a Zulip organization when
    a [custom emoji](/help/custom-emoji) has been updated,
    typically when a new emoji has been added or an old one
    has been deactivated. The event contains all custom emoji
    configured for the organization, not just the updated
    custom emoji.

    This legacy event is sent to clients that do not set
    the `individual_emoji_changes` client capability.

    **Changes**: Before Zulip 12.0 (feature level
    491), this was the only format of
    `realm_emoji` event sent. Clients should set the
    `individual_emoji_changes` capability and handle
    `realm_emoji/add` and `realm_emoji/edit` events
    instead.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemRealmEmojiType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemRealmEmojiOp] = None
    realm_emoji: typing.Optional[typing.Dict[str, RealmEmoji]] = pydantic.Field(default=None)
    """
    An object in which keys are RealmEmoji ids, and the
    values describe the custom emoji for that id.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_sixty_bot import GetEventsResponseEventsItemSixtyBot
from .get_events_response_events_item_sixty_op import GetEventsResponseEventsItemSixtyOp
from .get_events_response_events_item_sixty_type import GetEventsResponseEventsItemSixtyType


class GetEventsResponseEventsItemSixty(UniversalBaseModel):
    """
    Event sent to users who can administer a bot user when the bot is
    configured. Clients may also receive a `realm_user` event that
    for changes in public data about the bot (name, etc.).

    The `realm_user` events are sufficient for clients that
    only need to interact with the bot; this `realm_bot` event
    type is relevant only for administering bots.

    Only organization administrators and the user who owns the bot will
    receive this event.

    **Changes**: Starting from Zulip 12.0 (feature level 474),
    this event is not sent when updating bot's avatar, email, name or
    owner and also when reactivating or deactivating a bot.

    Starting from Zulip 12.0 (feature level 474), this event is
    no longer sent when a bot's API key is regenerated. Clients now
    use [`GET /bots/{bot_id}/api_key`](/api/get-bot-api-key) to get
    api key for the bot.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSixtyType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSixtyOp] = None
    bot: typing.Optional[GetEventsResponseEventsItemSixtyBot] = pydantic.Field(default=None)
    """
    Object containing details about the changed bot.
    It contains two properties: the user ID of the bot and
    the property to be changed. The changed property is one
    of the remaining properties listed below.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

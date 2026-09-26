

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_sixty_one_bot import GetEventsResponseEventsItemSixtyOneBot
from .get_events_response_events_item_sixty_one_op import GetEventsResponseEventsItemSixtyOneOp
from .get_events_response_events_item_sixty_one_type import GetEventsResponseEventsItemSixtyOneType


class GetEventsResponseEventsItemSixtyOne(UniversalBaseModel):
    """
    Event sent to all users when a bot has been deactivated.

    **Changes**: Deprecated and no longer sent since Zulip 8.0 (feature level 222).

    Previously, this event was sent to all users in a Zulip organization when a
    bot was deactivated.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSixtyOneType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSixtyOneOp] = None
    bot: typing.Optional[GetEventsResponseEventsItemSixtyOneBot] = pydantic.Field(default=None)
    """
    Object containing details about the deactivated bot.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

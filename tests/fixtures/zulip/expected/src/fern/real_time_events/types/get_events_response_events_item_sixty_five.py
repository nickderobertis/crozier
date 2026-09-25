

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_sixty_five_bot import GetEventsResponseEventsItemSixtyFiveBot
from .get_events_response_events_item_sixty_five_op import GetEventsResponseEventsItemSixtyFiveOp
from .get_events_response_events_item_sixty_five_type import GetEventsResponseEventsItemSixtyFiveType


class GetEventsResponseEventsItemSixtyFive(UniversalBaseModel):
    """
    Event sent to all users when a bot has been deactivated.
    Note that this is very similar to the bot_remove event
    and one of them will be removed soon.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSixtyFiveType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSixtyFiveOp] = None
    bot: typing.Optional[GetEventsResponseEventsItemSixtyFiveBot] = pydantic.Field(default=None)
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

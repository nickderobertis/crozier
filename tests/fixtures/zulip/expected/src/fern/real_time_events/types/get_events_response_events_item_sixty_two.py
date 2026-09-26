

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.bot import Bot
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_sixty_two_op import GetEventsResponseEventsItemSixtyTwoOp
from .get_events_response_events_item_sixty_two_type import GetEventsResponseEventsItemSixtyTwoType


class GetEventsResponseEventsItemSixtyTwo(UniversalBaseModel):
    """
    Event sent to users who can administer a newly created bot
    user. Clients will also receive a `realm_user` event that
    contains basic details (but not the API key).

    The `realm_user` events are sufficient for clients that
    only need to interact with the bot; this `realm_bot` event
    type is relevant only for administering bots.

    Only organization administrators and the user who owns the bot will
    receive this event.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSixtyTwoType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSixtyTwoOp] = None
    bot: typing.Optional[Bot] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

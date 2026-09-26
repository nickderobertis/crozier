

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_eighteen_op import GetEventsResponseEventsItemEighteenOp
from .get_events_response_events_item_eighteen_type import GetEventsResponseEventsItemEighteenType


class GetEventsResponseEventsItemEighteen(UniversalBaseModel):
    """
    Event sent when a reaction is removed from a message.
    Sent to all users who were recipients of the message.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemEighteenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemEighteenOp] = None
    message_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the message from which the reaction was
    removed.
    """

    emoji_code: typing.Optional[typing.Any] = None
    emoji_name: typing.Optional[typing.Any] = None
    reaction_type: typing.Optional[typing.Any] = None
    user_id: typing.Optional[typing.Any] = None
    user: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

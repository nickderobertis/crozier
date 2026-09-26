

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_id_op import GetEventsResponseEventsItemIdOp
from .get_events_response_events_item_id_type import GetEventsResponseEventsItemIdType


class GetEventsResponseEventsItemId(UniversalBaseModel):
    """
    Event sent to users in an organization when channel folders are reordered.

    **Changes**: New in Zulip 11.0 (feature level 418).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemIdType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemIdOp] = None
    order: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    A list of channel folder IDs representing the new order.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

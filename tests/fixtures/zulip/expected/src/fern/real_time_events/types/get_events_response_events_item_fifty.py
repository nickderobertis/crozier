

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_fifty_op import GetEventsResponseEventsItemFiftyOp
from .get_events_response_events_item_fifty_type import GetEventsResponseEventsItemFiftyType


class GetEventsResponseEventsItemFifty(UniversalBaseModel):
    """
    Event sent when a user group is deactivated but only to clients
    with `include_deactivated_groups` client capability set to `false`.

    **Changes**: Prior to Zulip 10.0 (feature level 294), this
    event was sent when a user group was deleted.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemFiftyType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemFiftyOp] = None
    group_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the group which has been deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

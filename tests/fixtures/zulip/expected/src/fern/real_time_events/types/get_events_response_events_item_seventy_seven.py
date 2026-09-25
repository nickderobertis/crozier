

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_seventy_seven_op import GetEventsResponseEventsItemSeventySevenOp
from .get_events_response_events_item_seventy_seven_type import GetEventsResponseEventsItemSeventySevenType


class GetEventsResponseEventsItemSeventySeven(UniversalBaseModel):
    """
    Event containing the fragment of a deleted navigation view.

    **Changes**: New in Zulip 11.0 (feature level 390).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSeventySevenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSeventySevenOp] = None
    fragment: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique URL hash of the navigation view that was just deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

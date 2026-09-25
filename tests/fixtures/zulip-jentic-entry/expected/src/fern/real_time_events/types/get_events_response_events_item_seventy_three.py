

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_seventy_three_data import GetEventsResponseEventsItemSeventyThreeData
from .get_events_response_events_item_seventy_three_op import GetEventsResponseEventsItemSeventyThreeOp
from .get_events_response_events_item_seventy_three_type import GetEventsResponseEventsItemSeventyThreeType


class GetEventsResponseEventsItemSeventyThree(UniversalBaseModel):
    """
    Event containing details of an update to an existing navigation view.

    **Changes**: New in Zulip 11.0 (feature level 390).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSeventyThreeType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSeventyThreeOp] = None
    fragment: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique URL hash of the navigation view being updated.
    """

    data: typing.Optional[GetEventsResponseEventsItemSeventyThreeData] = pydantic.Field(default=None)
    """
    A dictionary containing the updated properties of the navigation view.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

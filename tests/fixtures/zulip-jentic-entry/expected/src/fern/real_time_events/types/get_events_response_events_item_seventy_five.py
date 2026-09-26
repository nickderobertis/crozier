

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from ...types.saved_snippet import SavedSnippet
from .get_events_response_events_item_seventy_five_op import GetEventsResponseEventsItemSeventyFiveOp
from .get_events_response_events_item_seventy_five_type import GetEventsResponseEventsItemSeventyFiveType


class GetEventsResponseEventsItemSeventyFive(UniversalBaseModel):
    """
    Event containing details of a newly created saved snippet.

    **Changes**: New in Zulip 10.0 (feature level 297).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSeventyFiveType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSeventyFiveOp] = None
    saved_snippet: typing.Optional[SavedSnippet] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

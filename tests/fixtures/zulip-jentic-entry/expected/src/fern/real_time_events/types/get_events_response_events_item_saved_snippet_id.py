

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_saved_snippet_id_op import GetEventsResponseEventsItemSavedSnippetIdOp
from .get_events_response_events_item_saved_snippet_id_type import GetEventsResponseEventsItemSavedSnippetIdType


class GetEventsResponseEventsItemSavedSnippetId(UniversalBaseModel):
    """
    Event containing the ID of a deleted saved snippet.

    **Changes**: New in Zulip 10.0 (feature level 297).
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemSavedSnippetIdType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemSavedSnippetIdOp] = None
    saved_snippet_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the saved snippet that was just deleted.
    
    **Changes**: New in Zulip 10.0 (feature level 297).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.draft import Draft
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_draft_op import GetEventsResponseEventsItemDraftOp
from .get_events_response_events_item_draft_type import GetEventsResponseEventsItemDraftType


class GetEventsResponseEventsItemDraft(UniversalBaseModel):
    """
    Event containing details for an edited draft.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemDraftType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemDraftOp] = None
    draft: typing.Optional[Draft] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

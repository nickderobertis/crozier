

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_draft_id_op import GetEventsResponseEventsItemDraftIdOp
from .get_events_response_events_item_draft_id_type import GetEventsResponseEventsItemDraftIdType


class GetEventsResponseEventsItemDraftId(UniversalBaseModel):
    """
    Event containing the ID of a deleted draft.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemDraftIdType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemDraftIdOp] = None
    draft_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the draft that was just deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

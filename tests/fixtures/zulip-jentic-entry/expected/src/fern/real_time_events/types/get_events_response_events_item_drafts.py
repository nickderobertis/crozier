

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.draft import Draft
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_drafts_op import GetEventsResponseEventsItemDraftsOp
from .get_events_response_events_item_drafts_type import GetEventsResponseEventsItemDraftsType


class GetEventsResponseEventsItemDrafts(UniversalBaseModel):
    """
    Event containing details of newly created drafts.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemDraftsType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemDraftsOp] = None
    drafts: typing.Optional[typing.List[Draft]] = pydantic.Field(default=None)
    """
    An array containing objects for the newly created drafts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

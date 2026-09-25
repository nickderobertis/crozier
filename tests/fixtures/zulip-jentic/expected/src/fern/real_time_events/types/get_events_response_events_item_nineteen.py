

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.attachment import Attachment
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_nineteen_op import GetEventsResponseEventsItemNineteenOp
from .get_events_response_events_item_nineteen_type import GetEventsResponseEventsItemNineteenType


class GetEventsResponseEventsItemNineteen(UniversalBaseModel):
    """
    Event sent to a user's clients when the user uploads a new file
    in a Zulip message. Useful to implement live update in UI showing all files
    the current user has uploaded.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemNineteenType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemNineteenOp] = None
    attachment: typing.Optional[Attachment] = None
    upload_space_used: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total size of all files uploaded by in the organization,
    in bytes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

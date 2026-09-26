

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.attachment import Attachment
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_twenty_one_op import GetEventsResponseEventsItemTwentyOneOp
from .get_events_response_events_item_twenty_one_type import GetEventsResponseEventsItemTwentyOneType


class GetEventsResponseEventsItemTwentyOne(UniversalBaseModel):
    """
    Event sent to a user's clients when details of a file that user
    uploaded are changed. Most updates will be changes in the list of
    messages that reference the uploaded file.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemTwentyOneType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemTwentyOneOp] = None
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

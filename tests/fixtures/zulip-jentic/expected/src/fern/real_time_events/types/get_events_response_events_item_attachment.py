

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.event_id_schema import EventIdSchema
from .get_events_response_events_item_attachment_attachment import GetEventsResponseEventsItemAttachmentAttachment
from .get_events_response_events_item_attachment_op import GetEventsResponseEventsItemAttachmentOp
from .get_events_response_events_item_attachment_type import GetEventsResponseEventsItemAttachmentType


class GetEventsResponseEventsItemAttachment(UniversalBaseModel):
    """
    Event sent to a user's clients when the user deletes a file
    they had uploaded. Useful primarily for UI showing all the files
    the current user has uploaded.
    """

    id: typing.Optional[EventIdSchema] = None
    type: typing.Optional[GetEventsResponseEventsItemAttachmentType] = pydantic.Field(default=None)
    """
    The event's type, relevant both for client-side dispatch and server-side
    filtering by event type in [POST /register](/api/register-queue).
    """

    op: typing.Optional[GetEventsResponseEventsItemAttachmentOp] = None
    attachment: typing.Optional[GetEventsResponseEventsItemAttachmentAttachment] = pydantic.Field(default=None)
    """
    Dictionary containing the ID of the deleted attachment.
    """

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



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .activity_author_model import ActivityAuthorModel
from .outbound_attachment_model import OutboundAttachmentModel
from .outbound_email_response_email_opened_timestamps_item import OutboundEmailResponseEmailOpenedTimestampsItem


class OutboundEmailResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    author: typing.Optional[ActivityAuthorModel] = None
    timestamp: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    body: typing.Optional[str] = None
    recipients: typing.Optional[typing.List[str]] = None
    cc: typing.Optional[typing.List[str]] = None
    attachments: typing.Optional[typing.List[OutboundAttachmentModel]] = None
    email_opened_timestamps: typing_extensions.Annotated[
        typing.Optional[typing.List[OutboundEmailResponseEmailOpenedTimestampsItem]],
        FieldMetadata(alias="emailOpenedTimestamps"),
        pydantic.Field(alias="emailOpenedTimestamps"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

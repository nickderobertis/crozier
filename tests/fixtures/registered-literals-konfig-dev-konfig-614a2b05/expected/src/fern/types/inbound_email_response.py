

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .activity_author_model import ActivityAuthorModel
from .inbound_attachment_model import InboundAttachmentModel


class InboundEmailResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    email_thread_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="emailThreadId"), pydantic.Field(alias="emailThreadId")
    ] = None
    author: typing.Optional[ActivityAuthorModel] = None
    timestamp: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    body: typing.Optional[str] = None
    attachments: typing.Optional[typing.List[InboundAttachmentModel]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

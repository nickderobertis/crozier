

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_file_attachment_in_reply_to_index_revision_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexRevisionPage,
)


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexRevision(UniversalBaseModel):
    doc_session_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="docSessionId"), pydantic.Field(alias="docSessionId")
    ]
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexRevisionPage
    generation: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

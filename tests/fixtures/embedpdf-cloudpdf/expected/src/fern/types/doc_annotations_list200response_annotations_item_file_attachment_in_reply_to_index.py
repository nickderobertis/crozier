

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_file_attachment_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_file_attachment_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

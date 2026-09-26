

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_text_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemTextInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_text_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemTextInReplyToIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemTextInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemTextInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemTextInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

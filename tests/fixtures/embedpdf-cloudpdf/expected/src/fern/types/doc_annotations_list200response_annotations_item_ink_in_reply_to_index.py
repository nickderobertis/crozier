

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_ink_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemInkInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_ink_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemInkInReplyToIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemInkInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemInkInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemInkInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

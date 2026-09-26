

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_caret_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_caret_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemCaretInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

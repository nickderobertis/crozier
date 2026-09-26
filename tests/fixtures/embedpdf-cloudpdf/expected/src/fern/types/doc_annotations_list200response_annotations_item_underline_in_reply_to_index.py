

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_underline_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_underline_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_free_text_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_free_text_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

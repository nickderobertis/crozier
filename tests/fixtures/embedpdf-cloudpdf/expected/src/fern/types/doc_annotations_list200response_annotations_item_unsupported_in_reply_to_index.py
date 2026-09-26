

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_unsupported_in_reply_to_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToIndexPage,
)
from .doc_annotations_list200response_annotations_item_unsupported_in_reply_to_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

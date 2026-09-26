

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_in_reply_to_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineInReplyToIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_in_reply_to_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineInReplyToIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineInReplyToIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

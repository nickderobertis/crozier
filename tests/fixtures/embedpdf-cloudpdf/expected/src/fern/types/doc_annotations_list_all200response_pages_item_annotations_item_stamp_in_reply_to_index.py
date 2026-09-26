

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_in_reply_to_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampInReplyToIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_in_reply_to_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampInReplyToIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampInReplyToIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

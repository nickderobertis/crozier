

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_in_reply_to_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyInReplyToIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_squiggly_in_reply_to_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyInReplyToIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyInReplyToIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemSquigglyInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

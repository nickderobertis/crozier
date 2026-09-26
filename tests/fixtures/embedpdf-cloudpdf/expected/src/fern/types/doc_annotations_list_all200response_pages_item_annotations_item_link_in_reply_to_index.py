

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_link_in_reply_to_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkInReplyToIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_link_in_reply_to_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkInReplyToIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkInReplyToIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkInReplyToIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLinkInReplyToIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

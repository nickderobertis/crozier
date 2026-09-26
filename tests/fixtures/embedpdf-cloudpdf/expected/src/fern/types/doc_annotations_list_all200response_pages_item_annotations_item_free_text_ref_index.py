

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_free_text_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

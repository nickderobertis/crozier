

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_stamp_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStampRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

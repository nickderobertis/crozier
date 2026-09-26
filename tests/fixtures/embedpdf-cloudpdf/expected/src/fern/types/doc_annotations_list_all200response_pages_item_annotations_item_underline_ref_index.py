

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

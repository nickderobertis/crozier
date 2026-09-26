

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_line_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

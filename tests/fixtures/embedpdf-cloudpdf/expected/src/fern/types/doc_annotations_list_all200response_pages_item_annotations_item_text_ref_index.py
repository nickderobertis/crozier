

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_text_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_text_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemTextRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

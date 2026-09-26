

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_unsupported_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnsupportedRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

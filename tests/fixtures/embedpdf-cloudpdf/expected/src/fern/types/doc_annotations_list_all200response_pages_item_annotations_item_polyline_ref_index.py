

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

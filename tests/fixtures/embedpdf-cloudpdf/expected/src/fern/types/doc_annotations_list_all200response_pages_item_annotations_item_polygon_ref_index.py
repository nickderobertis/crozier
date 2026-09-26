

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_ref_index_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefIndexPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_ref_index_revision import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefIndexRevision,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefIndex(UniversalBaseModel):
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefIndexPage
    index: int
    revision: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

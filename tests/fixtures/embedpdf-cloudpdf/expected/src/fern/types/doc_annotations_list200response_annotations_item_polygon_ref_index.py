

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_polygon_ref_index_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRefIndexPage,
)
from .doc_annotations_list200response_annotations_item_polygon_ref_index_revision import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRefIndexRevision,
)


class DocAnnotationsList200ResponseAnnotationsItemPolygonRefIndex(UniversalBaseModel):
    page: DocAnnotationsList200ResponseAnnotationsItemPolygonRefIndexPage
    index: int
    revision: DocAnnotationsList200ResponseAnnotationsItemPolygonRefIndexRevision

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

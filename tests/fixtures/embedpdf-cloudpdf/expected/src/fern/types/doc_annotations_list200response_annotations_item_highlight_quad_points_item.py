

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_highlight_quad_points_item_p1 import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItemP1,
)
from .doc_annotations_list200response_annotations_item_highlight_quad_points_item_p2 import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItemP2,
)
from .doc_annotations_list200response_annotations_item_highlight_quad_points_item_p3 import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItemP3,
)
from .doc_annotations_list200response_annotations_item_highlight_quad_points_item_p4 import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItemP4,
)


class DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItem(UniversalBaseModel):
    p1: DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItemP1
    p2: DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItemP2
    p3: DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItemP3
    p4: DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItemP4

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

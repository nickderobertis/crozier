

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_underline_quad_points_item_p1 import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItemP1,
)
from .doc_annotations_list200response_annotations_item_underline_quad_points_item_p2 import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItemP2,
)
from .doc_annotations_list200response_annotations_item_underline_quad_points_item_p3 import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItemP3,
)
from .doc_annotations_list200response_annotations_item_underline_quad_points_item_p4 import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItemP4,
)


class DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItem(UniversalBaseModel):
    p1: DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItemP1
    p2: DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItemP2
    p3: DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItemP3
    p4: DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItemP4

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

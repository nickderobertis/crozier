

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_squiggly_quad_points_item_p1 import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItemP1,
)
from .doc_annotations_list200response_annotations_item_squiggly_quad_points_item_p2 import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItemP2,
)
from .doc_annotations_list200response_annotations_item_squiggly_quad_points_item_p3 import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItemP3,
)
from .doc_annotations_list200response_annotations_item_squiggly_quad_points_item_p4 import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItemP4,
)


class DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItem(UniversalBaseModel):
    p1: DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItemP1
    p2: DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItemP2
    p3: DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItemP3
    p4: DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItemP4

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

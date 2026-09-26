

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_strikeout_quad_points_item_p1 import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItemP1,
)
from .doc_annotations_list200response_annotations_item_strikeout_quad_points_item_p2 import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItemP2,
)
from .doc_annotations_list200response_annotations_item_strikeout_quad_points_item_p3 import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItemP3,
)
from .doc_annotations_list200response_annotations_item_strikeout_quad_points_item_p4 import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItemP4,
)


class DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItem(UniversalBaseModel):
    p1: DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItemP1
    p2: DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItemP2
    p3: DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItemP3
    p4: DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItemP4

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

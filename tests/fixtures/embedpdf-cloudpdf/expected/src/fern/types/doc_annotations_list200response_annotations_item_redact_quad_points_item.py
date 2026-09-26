

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_redact_quad_points_item_p1 import (
    DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItemP1,
)
from .doc_annotations_list200response_annotations_item_redact_quad_points_item_p2 import (
    DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItemP2,
)
from .doc_annotations_list200response_annotations_item_redact_quad_points_item_p3 import (
    DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItemP3,
)
from .doc_annotations_list200response_annotations_item_redact_quad_points_item_p4 import (
    DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItemP4,
)


class DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItem(UniversalBaseModel):
    p1: DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItemP1
    p2: DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItemP2
    p3: DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItemP3
    p4: DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItemP4

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

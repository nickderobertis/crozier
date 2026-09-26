

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_quad_points_item_p1 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItemP1,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_quad_points_item_p2 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItemP2,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_quad_points_item_p3 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItemP3,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_underline_quad_points_item_p4 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItemP4,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItem(UniversalBaseModel):
    p1: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItemP1
    p2: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItemP2
    p3: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItemP3
    p4: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemUnderlineQuadPointsItemP4

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

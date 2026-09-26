

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_quad_points_item_p1 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItemP1,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_quad_points_item_p2 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItemP2,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_quad_points_item_p3 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItemP3,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_strikeout_quad_points_item_p4 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItemP4,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItem(UniversalBaseModel):
    p1: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItemP1
    p2: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItemP2
    p3: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItemP3
    p4: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutQuadPointsItemP4

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_quad_points_item_p1 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItemP1,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_quad_points_item_p2 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItemP2,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_quad_points_item_p3 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItemP3,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_quad_points_item_p4 import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItemP4,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItem(UniversalBaseModel):
    p1: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItemP1
    p2: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItemP2
    p3: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItemP3
    p4: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItemP4

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

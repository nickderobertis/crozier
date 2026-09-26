

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_line_line_points_end import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLinePointsEnd,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_line_points_start import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLinePointsStart,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLinePoints(UniversalBaseModel):
    start: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLinePointsStart
    end: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineLinePointsEnd

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_line_line_points_end import (
    DocAnnotationsList200ResponseAnnotationsItemLineLinePointsEnd,
)
from .doc_annotations_list200response_annotations_item_line_line_points_start import (
    DocAnnotationsList200ResponseAnnotationsItemLineLinePointsStart,
)


class DocAnnotationsList200ResponseAnnotationsItemLineLinePoints(UniversalBaseModel):
    start: DocAnnotationsList200ResponseAnnotationsItemLineLinePointsStart
    end: DocAnnotationsList200ResponseAnnotationsItemLineLinePointsEnd

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

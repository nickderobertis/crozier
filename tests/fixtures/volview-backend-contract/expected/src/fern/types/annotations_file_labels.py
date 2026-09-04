

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .annotations_file_labels_polygons_value import AnnotationsFileLabelsPolygonsValue
from .annotations_file_labels_rectangles_value import AnnotationsFileLabelsRectanglesValue
from .annotations_file_labels_rulers_value import AnnotationsFileLabelsRulersValue


class AnnotationsFileLabels(UniversalBaseModel):
    rulers: typing.Optional[typing.Dict[str, AnnotationsFileLabelsRulersValue]] = None
    rectangles: typing.Optional[typing.Dict[str, AnnotationsFileLabelsRectanglesValue]] = None
    polygons: typing.Optional[typing.Dict[str, AnnotationsFileLabelsPolygonsValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

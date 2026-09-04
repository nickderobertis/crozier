

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .annotations_file_tools_polygons_item import AnnotationsFileToolsPolygonsItem
from .annotations_file_tools_rectangles_item import AnnotationsFileToolsRectanglesItem
from .annotations_file_tools_rulers_item import AnnotationsFileToolsRulersItem


class AnnotationsFileTools(UniversalBaseModel):
    rulers: typing.Optional[typing.List[AnnotationsFileToolsRulersItem]] = None
    rectangles: typing.Optional[typing.List[AnnotationsFileToolsRectanglesItem]] = None
    polygons: typing.Optional[typing.List[AnnotationsFileToolsPolygonsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

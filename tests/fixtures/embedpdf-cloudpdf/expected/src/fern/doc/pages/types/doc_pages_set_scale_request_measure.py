

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_set_scale_request_measure_angle_item import DocPagesSetScaleRequestMeasureAngleItem
from .doc_pages_set_scale_request_measure_area_item import DocPagesSetScaleRequestMeasureAreaItem
from .doc_pages_set_scale_request_measure_distance_item import DocPagesSetScaleRequestMeasureDistanceItem
from .doc_pages_set_scale_request_measure_origin import DocPagesSetScaleRequestMeasureOrigin
from .doc_pages_set_scale_request_measure_slope_item import DocPagesSetScaleRequestMeasureSlopeItem
from .doc_pages_set_scale_request_measure_subtype import DocPagesSetScaleRequestMeasureSubtype
from .doc_pages_set_scale_request_measure_x_item import DocPagesSetScaleRequestMeasureXItem
from .doc_pages_set_scale_request_measure_y_item import DocPagesSetScaleRequestMeasureYItem


class DocPagesSetScaleRequestMeasure(UniversalBaseModel):
    subtype: DocPagesSetScaleRequestMeasureSubtype
    ratio: typing.Optional[str] = None
    x: typing.List[DocPagesSetScaleRequestMeasureXItem]
    y: typing.Optional[typing.List[DocPagesSetScaleRequestMeasureYItem]] = None
    distance: typing.List[DocPagesSetScaleRequestMeasureDistanceItem]
    area: typing.List[DocPagesSetScaleRequestMeasureAreaItem]
    angle: typing.Optional[typing.List[DocPagesSetScaleRequestMeasureAngleItem]] = None
    slope: typing.Optional[typing.List[DocPagesSetScaleRequestMeasureSlopeItem]] = None
    origin: typing.Optional[DocPagesSetScaleRequestMeasureOrigin] = None
    cyx: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_polyline_measure_rl_angle_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlAngleItem,
)
from .doc_annotations_list200response_annotations_item_polyline_measure_rl_area_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlAreaItem,
)
from .doc_annotations_list200response_annotations_item_polyline_measure_rl_distance_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlDistanceItem,
)
from .doc_annotations_list200response_annotations_item_polyline_measure_rl_origin import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlOrigin,
)
from .doc_annotations_list200response_annotations_item_polyline_measure_rl_slope_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlSlopeItem,
)
from .doc_annotations_list200response_annotations_item_polyline_measure_rl_x_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlXItem,
)
from .doc_annotations_list200response_annotations_item_polyline_measure_rl_y_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlYItem,
)


class DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRl(UniversalBaseModel):
    ratio: typing.Optional[str] = None
    x: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlXItem]
    y: typing.Optional[typing.List[DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlYItem]] = None
    distance: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlDistanceItem]
    area: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlAreaItem]
    angle: typing.Optional[typing.List[DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlAngleItem]] = None
    slope: typing.Optional[typing.List[DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlSlopeItem]] = None
    origin: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlOrigin] = None
    cyx: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

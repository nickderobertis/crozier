

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_polygon_measure_rl_angle_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlAngleItem,
)
from .doc_annotations_list200response_annotations_item_polygon_measure_rl_area_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlAreaItem,
)
from .doc_annotations_list200response_annotations_item_polygon_measure_rl_distance_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlDistanceItem,
)
from .doc_annotations_list200response_annotations_item_polygon_measure_rl_origin import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlOrigin,
)
from .doc_annotations_list200response_annotations_item_polygon_measure_rl_slope_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlSlopeItem,
)
from .doc_annotations_list200response_annotations_item_polygon_measure_rl_x_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlXItem,
)
from .doc_annotations_list200response_annotations_item_polygon_measure_rl_y_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlYItem,
)


class DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure_Rl(UniversalBaseModel):
    subtype: typing.Literal["RL"] = "RL"
    ratio: typing.Optional[str] = None
    x: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlXItem]
    y: typing.Optional[typing.List[DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlYItem]] = None
    distance: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlDistanceItem]
    area: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlAreaItem]
    angle: typing.Optional[typing.List[DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlAngleItem]] = None
    slope: typing.Optional[typing.List[DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlSlopeItem]] = None
    origin: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlOrigin] = None
    cyx: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure_Geo(UniversalBaseModel):
    subtype: typing.Literal["GEO"] = "GEO"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure_Unknown(UniversalBaseModel):
    subtype: typing.Literal["unknown"] = "unknown"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure_Rl,
        DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure_Geo,
        DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure_Unknown,
    ],
    pydantic.Field(discriminator="subtype"),
]

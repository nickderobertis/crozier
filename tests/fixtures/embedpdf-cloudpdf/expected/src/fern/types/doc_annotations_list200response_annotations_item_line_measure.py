

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list200response_annotations_item_line_measure_rl_angle_item import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItem,
)
from .doc_annotations_list200response_annotations_item_line_measure_rl_area_item import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAreaItem,
)
from .doc_annotations_list200response_annotations_item_line_measure_rl_distance_item import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlDistanceItem,
)
from .doc_annotations_list200response_annotations_item_line_measure_rl_origin import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlOrigin,
)
from .doc_annotations_list200response_annotations_item_line_measure_rl_slope_item import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlSlopeItem,
)
from .doc_annotations_list200response_annotations_item_line_measure_rl_x_item import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlXItem,
)
from .doc_annotations_list200response_annotations_item_line_measure_rl_y_item import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlYItem,
)


class DocAnnotationsList200ResponseAnnotationsItemLineMeasure_Rl(UniversalBaseModel):
    subtype: typing.Literal["RL"] = "RL"
    ratio: typing.Optional[str] = None
    x: typing.List[DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlXItem]
    y: typing.Optional[typing.List[DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlYItem]] = None
    distance: typing.List[DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlDistanceItem]
    area: typing.List[DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAreaItem]
    angle: typing.Optional[typing.List[DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItem]] = None
    slope: typing.Optional[typing.List[DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlSlopeItem]] = None
    origin: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlOrigin] = None
    cyx: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLineMeasure_Geo(UniversalBaseModel):
    subtype: typing.Literal["GEO"] = "GEO"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItemLineMeasure_Unknown(UniversalBaseModel):
    subtype: typing.Literal["unknown"] = "unknown"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItemLineMeasure = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItemLineMeasure_Rl,
        DocAnnotationsList200ResponseAnnotationsItemLineMeasure_Geo,
        DocAnnotationsList200ResponseAnnotationsItemLineMeasure_Unknown,
    ],
    pydantic.Field(discriminator="subtype"),
]

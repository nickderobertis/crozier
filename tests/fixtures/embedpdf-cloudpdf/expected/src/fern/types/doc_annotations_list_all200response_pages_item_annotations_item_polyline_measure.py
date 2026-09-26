

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_measure_rl_angle_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlAngleItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_measure_rl_area_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlAreaItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_measure_rl_distance_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlDistanceItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_measure_rl_origin import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlOrigin,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_measure_rl_slope_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlSlopeItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_measure_rl_x_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlXItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polyline_measure_rl_y_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlYItem,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasure_Rl(UniversalBaseModel):
    subtype: typing.Literal["RL"] = "RL"
    ratio: typing.Optional[str] = None
    x: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlXItem]
    y: typing.Optional[typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlYItem]] = (
        None
    )
    distance: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlDistanceItem]
    area: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlAreaItem]
    angle: typing.Optional[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlAngleItem]
    ] = None
    slope: typing.Optional[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlSlopeItem]
    ] = None
    origin: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlOrigin] = None
    cyx: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasure_Geo(UniversalBaseModel):
    subtype: typing.Literal["GEO"] = "GEO"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasure_Unknown(UniversalBaseModel):
    subtype: typing.Literal["unknown"] = "unknown"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasure = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasure_Rl,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasure_Geo,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasure_Unknown,
    ],
    pydantic.Field(discriminator="subtype"),
]



from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_measure_rl_angle_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlAngleItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_measure_rl_area_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlAreaItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_measure_rl_distance_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlDistanceItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_measure_rl_origin import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlOrigin,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_measure_rl_slope_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlSlopeItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_measure_rl_x_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlXItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_polygon_measure_rl_y_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlYItem,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasure_Rl(UniversalBaseModel):
    subtype: typing.Literal["RL"] = "RL"
    ratio: typing.Optional[str] = None
    x: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlXItem]
    y: typing.Optional[typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlYItem]] = (
        None
    )
    distance: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlDistanceItem]
    area: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlAreaItem]
    angle: typing.Optional[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlAngleItem]
    ] = None
    slope: typing.Optional[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlSlopeItem]
    ] = None
    origin: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasureRlOrigin] = None
    cyx: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasure_Geo(UniversalBaseModel):
    subtype: typing.Literal["GEO"] = "GEO"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasure_Unknown(UniversalBaseModel):
    subtype: typing.Literal["unknown"] = "unknown"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasure = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasure_Rl,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasure_Geo,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolygonMeasure_Unknown,
    ],
    pydantic.Field(discriminator="subtype"),
]

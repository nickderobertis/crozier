

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_annotations_list_all200response_pages_item_annotations_item_line_measure_rl_angle_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAngleItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_measure_rl_area_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAreaItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_measure_rl_distance_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlDistanceItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_measure_rl_origin import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlOrigin,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_measure_rl_slope_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlSlopeItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_measure_rl_x_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlXItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_line_measure_rl_y_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlYItem,
)


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasure_Rl(UniversalBaseModel):
    subtype: typing.Literal["RL"] = "RL"
    ratio: typing.Optional[str] = None
    x: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlXItem]
    y: typing.Optional[typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlYItem]] = None
    distance: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlDistanceItem]
    area: typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAreaItem]
    angle: typing.Optional[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAngleItem]
    ] = None
    slope: typing.Optional[
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlSlopeItem]
    ] = None
    origin: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlOrigin] = None
    cyx: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasure_Geo(UniversalBaseModel):
    subtype: typing.Literal["GEO"] = "GEO"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasure_Unknown(UniversalBaseModel):
    subtype: typing.Literal["unknown"] = "unknown"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasure = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasure_Rl,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasure_Geo,
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasure_Unknown,
    ],
    pydantic.Field(discriminator="subtype"),
]

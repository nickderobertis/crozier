

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .doc_pages_viewports200response_item_measure_rl_angle_item import (
    DocPagesViewports200ResponseItemMeasureRlAngleItem,
)
from .doc_pages_viewports200response_item_measure_rl_area_item import DocPagesViewports200ResponseItemMeasureRlAreaItem
from .doc_pages_viewports200response_item_measure_rl_distance_item import (
    DocPagesViewports200ResponseItemMeasureRlDistanceItem,
)
from .doc_pages_viewports200response_item_measure_rl_origin import DocPagesViewports200ResponseItemMeasureRlOrigin
from .doc_pages_viewports200response_item_measure_rl_slope_item import (
    DocPagesViewports200ResponseItemMeasureRlSlopeItem,
)
from .doc_pages_viewports200response_item_measure_rl_x_item import DocPagesViewports200ResponseItemMeasureRlXItem
from .doc_pages_viewports200response_item_measure_rl_y_item import DocPagesViewports200ResponseItemMeasureRlYItem


class DocPagesViewports200ResponseItemMeasureRl(UniversalBaseModel):
    ratio: typing.Optional[str] = None
    x: typing.List[DocPagesViewports200ResponseItemMeasureRlXItem]
    y: typing.Optional[typing.List[DocPagesViewports200ResponseItemMeasureRlYItem]] = None
    distance: typing.List[DocPagesViewports200ResponseItemMeasureRlDistanceItem]
    area: typing.List[DocPagesViewports200ResponseItemMeasureRlAreaItem]
    angle: typing.Optional[typing.List[DocPagesViewports200ResponseItemMeasureRlAngleItem]] = None
    slope: typing.Optional[typing.List[DocPagesViewports200ResponseItemMeasureRlSlopeItem]] = None
    origin: typing.Optional[DocPagesViewports200ResponseItemMeasureRlOrigin] = None
    cyx: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

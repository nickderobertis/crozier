

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chart_tile_definition import ChartTileDefinition
from .chart_tile_layout import ChartTileLayout


class Tile_Chart(UniversalBaseModel):
    type: typing.Literal["chart"] = "chart"
    layout: ChartTileLayout
    definition: ChartTileDefinition

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Tile = Tile_Chart

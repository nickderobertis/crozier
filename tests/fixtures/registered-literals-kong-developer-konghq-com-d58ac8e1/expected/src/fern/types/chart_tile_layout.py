

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chart_tile_layout_position import ChartTileLayoutPosition
from .chart_tile_layout_size import ChartTileLayoutSize


class ChartTileLayout(UniversalBaseModel):
    """
    Information about how the tile is placed on the dashboard.

    Examples:
    - a tile occupying the first half of the top row: `{ "position": { "col": 0, "row": 0 }, size: { "cols": 3, "rows": 1 } }`
    - a tile occupying the second half of the top row: `{ "position": { "col": 3, "row": 0 }, size: { "cols": 3, "rows": 1 } }`
    """

    position: ChartTileLayoutPosition = pydantic.Field()
    """
    Position of the tile in the dashboard's grid.  Numbering starts at 0, so a tile in the upper left of the dashboard will be at column 0, row 0.
    """

    size: ChartTileLayoutSize = pydantic.Field()
    """
    Number of columns and rows the tile occupies.  A dashboard always has 6 columns, but has as many rows as needed to accommodate the given tiles.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

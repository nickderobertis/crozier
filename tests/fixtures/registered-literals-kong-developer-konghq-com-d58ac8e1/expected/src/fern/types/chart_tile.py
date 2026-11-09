

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chart_tile_definition import ChartTileDefinition
from .chart_tile_layout import ChartTileLayout


class ChartTile(UniversalBaseModel):
    """
    A tile that queries data and renders a chart.
    """

    layout: ChartTileLayout = pydantic.Field()
    """
    Information about how the tile is placed on the dashboard.
    
    Examples:
    - a tile occupying the first half of the top row: `{ "position": { "col": 0, "row": 0 }, size: { "cols": 3, "rows": 1 } }`
    - a tile occupying the second half of the top row: `{ "position": { "col": 3, "row": 0 }, size: { "cols": 3, "rows": 1 } }`
    """

    definition: ChartTileDefinition = pydantic.Field()
    """
    The tile's definition, which consists of a query to fetch data and a chart to render the data.
    Note that some charts expect certain types of queries to render properly.  The documentation for the individual chart types has more information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

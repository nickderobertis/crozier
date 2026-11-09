

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chart import Chart
from .chart_tile_definition_query import ChartTileDefinitionQuery


class ChartTileDefinition(UniversalBaseModel):
    """
    The tile's definition, which consists of a query to fetch data and a chart to render the data.
    Note that some charts expect certain types of queries to render properly.  The documentation for the individual chart types has more information.
    """

    query: ChartTileDefinitionQuery
    chart: Chart

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

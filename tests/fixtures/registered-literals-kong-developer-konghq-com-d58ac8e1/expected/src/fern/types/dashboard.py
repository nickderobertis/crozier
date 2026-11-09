

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .all_filter_items import AllFilterItems
from .tile import Tile


class Dashboard(UniversalBaseModel):
    """
    A JSON object describing a dashboard.

    A dashboard is an array of tiles.  All tiles are of type 'chart', which query data and render a chart displaying that data.

    Dashboards have 6 columns and as many rows as necessary to display their tiles.
    """

    tiles: typing.List[Tile] = pydantic.Field()
    """
    The array of tiles.  We currently support up to 102 tiles, which is 17 rows of 6x1 tiles.
    """

    preset_filters: typing.Optional[typing.List[AllFilterItems]] = pydantic.Field(default=None)
    """
    An optional array of filters that are applied globally to all relevant tiles in the dashboard.
    
    Whether or not a preset filter applies to a tile depends on the filter's dimension.  Some dimensions, like `control_plane`, are common to all datasources; other dimensions may only apply to one datasource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BarChart(UniversalBaseModel):
    """
    A chart that can display non-timeseries data as bars.  This type of chart supports up to 2 dimensions (not `time`).
    To render a bar chart of timeseries data, use a `timeseries_bar` chart instead.
    """

    chart_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the chart, which is displayed in the tile's header.
    """

    stacked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to stack the bars (implicitly adding them together to form a total), or leave them independent from each other.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

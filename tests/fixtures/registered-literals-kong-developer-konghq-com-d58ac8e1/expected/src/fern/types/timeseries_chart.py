

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TimeseriesChart(UniversalBaseModel):
    """
    A chart that can render timeseries data -- data from a query that has `time` as a dimension -- as lines or bars.

    This type of chart can support:

    - One or more metrics: `{ metrics: ["response_latency_p99", "response_latency_p95"], dimensions: ["time"] }`
    - One metric plus one non-time dimension: `{ metrics: ["request_count"], dimensions: ["time", "gateway_service"] }`

    Either way, ensure that `time` is in the list of query dimensions.
    """

    chart_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the chart, which is displayed in the tile's header.
    """

    stacked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to stack the bars or lines (implicitly adding them together to form a total), or leave them independent from each other.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .parameter import Parameter


class AggregationFunction(UniversalBaseModel):
    """
    Preview: An identifier for an aggregation function. Aggregation functions are SQL functions that group or transform data from multiple points to a single point. This is a preview feature and may be subject to change before final release.
    """

    parameters: typing.Optional[typing.List[Parameter]] = pydantic.Field(default=None)
    """
    Optional. Parameters applied to the aggregation function. Only used for functions that require them.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required. The type of aggregation function, must be one of the following: "none" - no function. "percentile" - APPROX_QUANTILES() - 1 parameter numeric value "average" - AVG() "count" - COUNT() "count-distinct" - COUNT(DISTINCT) "count-distinct-approx" - APPROX_COUNT_DISTINCT() "max" - MAX() "min" - MIN() "sum" - SUM()
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

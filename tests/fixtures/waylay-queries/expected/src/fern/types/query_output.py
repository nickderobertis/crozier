

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .alignment import Alignment
from .query_output_aggregation import QueryOutputAggregation
from .query_output_from import QueryOutputFrom
from .query_output_interpolation import QueryOutputInterpolation
from .query_output_until import QueryOutputUntil
from .render import Render
from .series_spec import SeriesSpec


class QueryOutput(UniversalBaseModel):
    """
    Query definition for a Waylay analytics query.

    See also [api docs](https://docs.waylay.io/#/api/query/?id=data-query-json-representation).
    """

    resource: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default resource for the series in the query.
    """

    metric: typing.Optional[str] = pydantic.Field(default=None)
    """
    Default metric for the series in the query.
    """

    aggregation: typing.Optional[QueryOutputAggregation] = pydantic.Field(default=None)
    """
    Default aggregation method(s) for the series in the query.
    """

    interpolation: typing.Optional[QueryOutputInterpolation] = pydantic.Field(default=None)
    """
    Default Interpolation method for the series (if aggregated).
    """

    freq: typing.Optional[str] = pydantic.Field(default=None)
    """
    Interval used to aggregate or regularize data. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[QueryOutputFrom],
        FieldMetadata(alias="from"),
        pydantic.Field(
            alias="from",
            description="The start of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)  specifiers.",
        ),
    ] = None
    """
    The start of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)  specifiers.
    """

    until: typing.Optional[QueryOutputUntil] = pydantic.Field(default=None)
    """
    The end (not-inclusive) of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties)specifiers.
    """

    window: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute size of the time window for which results will be returned. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.
    """

    periods: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of the time window in number of `freq` units. One of the [time line](https://docs.waylay.io/#/api/query/?id=time-line-properties) specifiers.
    """

    align: typing.Optional[Alignment] = None
    data: typing.Optional[typing.List[SeriesSpec]] = pydantic.Field(default=None)
    """
    List of series specifications. When not specified, a single default series specification is assumed(`[{}]`, using the default `metric`,`resource`, ... ).
    """

    render: typing.Optional[Render] = None
    lookback: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If enabled, the **last-known value** for each of the series will be taken into account in the result. 
    For **unaggregated** series, that value will be included as is (with a timestamp before the result window).
    For **aggregated** series, that value will be used at the first timestamp, but only if
     * no aggregated value on the first timestamp could be computed
     * and the aggregation is compatible with the value, i.e. in mean, min, max, first, last, median
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

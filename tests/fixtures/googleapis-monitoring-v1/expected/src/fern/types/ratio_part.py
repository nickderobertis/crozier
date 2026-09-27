

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .aggregation import Aggregation


class RatioPart(UniversalBaseModel):
    """
    Describes a query to build the numerator or denominator of a TimeSeriesFilterRatio.
    """

    aggregation: typing.Optional[Aggregation] = pydantic.Field(default=None)
    """
    By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.
    """

    filter: typing.Optional[str] = pydantic.Field(default=None)
    """
    Required. The monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

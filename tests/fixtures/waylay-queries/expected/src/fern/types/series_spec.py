

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .series_spec_interpolation import SeriesSpecInterpolation


class SeriesSpec(UniversalBaseModel):
    """
    Query specification for a single series.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional alias name for the series. This name is used when exporting the dataset to CSV format.
    """

    resource: typing.Optional[str] = pydantic.Field(default=None)
    """
    Resource id for the series, required unless it is specified as a query default.
    """

    metric: typing.Optional[str] = pydantic.Field(default=None)
    """
    Metric name for the series, required unless it is specified as a query default.
    """

    aggregration: typing.Optional[str] = pydantic.Field(default=None)
    """
    Aggregation method for the series (if aggregated). If missing, the query default is used.
    """

    interpolation: typing.Optional[SeriesSpecInterpolation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .table_display_options import TableDisplayOptions
from .time_series_query import TimeSeriesQuery


class TableDataSet(UniversalBaseModel):
    """
    Groups a time series query definition with table options.
    """

    min_alignment_period: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minAlignmentPeriod"),
        pydantic.Field(
            alias="minAlignmentPeriod",
            description="Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query For example, if the data is published once every 10 minutes, the min_alignment_period should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.",
        ),
    ] = None
    """
    Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query For example, if the data is published once every 10 minutes, the min_alignment_period should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.
    """

    table_display_options: typing_extensions.Annotated[
        typing.Optional[TableDisplayOptions],
        FieldMetadata(alias="tableDisplayOptions"),
        pydantic.Field(
            alias="tableDisplayOptions",
            description="Optional. Table display options for configuring how the table is rendered.",
        ),
    ] = None
    """
    Optional. Table display options for configuring how the table is rendered.
    """

    table_template: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tableTemplate"),
        pydantic.Field(
            alias="tableTemplate",
            description='Optional. A template string for naming TimeSeries in the resulting data set. This should be a string with interpolations of the form ${label_name}, which will resolve to the label\'s value i.e. "${resource.labels.project_id}."',
        ),
    ] = None
    """
    Optional. A template string for naming TimeSeries in the resulting data set. This should be a string with interpolations of the form ${label_name}, which will resolve to the label's value i.e. "${resource.labels.project_id}."
    """

    time_series_query: typing_extensions.Annotated[
        typing.Optional[TimeSeriesQuery],
        FieldMetadata(alias="timeSeriesQuery"),
        pydantic.Field(
            alias="timeSeriesQuery",
            description="Required. Fields for querying time series data from the Stackdriver metrics API.",
        ),
    ] = None
    """
    Required. Fields for querying time series data from the Stackdriver metrics API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

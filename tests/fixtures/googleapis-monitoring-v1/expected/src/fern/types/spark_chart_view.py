

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .spark_chart_view_spark_chart_type import SparkChartViewSparkChartType


class SparkChartView(UniversalBaseModel):
    """
    A sparkChart is a small chart suitable for inclusion in a table-cell or inline in text. This message contains the configuration for a sparkChart to show up on a Scorecard, showing recent trends of the scorecard's timeseries.
    """

    min_alignment_period: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minAlignmentPeriod"),
        pydantic.Field(
            alias="minAlignmentPeriod",
            description="The lower bound on data point frequency in the chart implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes it would not make sense to fetch and align data at one minute intervals. This field is optional and exists only as a hint.",
        ),
    ] = None
    """
    The lower bound on data point frequency in the chart implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes it would not make sense to fetch and align data at one minute intervals. This field is optional and exists only as a hint.
    """

    spark_chart_type: typing_extensions.Annotated[
        typing.Optional[SparkChartViewSparkChartType],
        FieldMetadata(alias="sparkChartType"),
        pydantic.Field(
            alias="sparkChartType", description="Required. The type of sparkchart to show in this chartView."
        ),
    ] = None
    """
    Required. The type of sparkchart to show in this chartView.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

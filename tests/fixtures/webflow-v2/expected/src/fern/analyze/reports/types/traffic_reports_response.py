

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .traffic_reports_response_bucketing import TrafficReportsResponseBucketing
from .traffic_reports_response_data_item import TrafficReportsResponseDataItem
from .traffic_reports_response_filter import TrafficReportsResponseFilter
from .traffic_reports_response_metric_scope import TrafficReportsResponseMetricScope
from .traffic_reports_response_report import TrafficReportsResponseReport
from .traffic_reports_response_window import TrafficReportsResponseWindow


class TrafficReportsResponse(UniversalBaseModel):
    """
    Response payload for the traffic report.
    """

    report: TrafficReportsResponseReport = pydantic.Field()
    """
    Discriminator identifying the report type.
    """

    window: TrafficReportsResponseWindow = pydantic.Field()
    """
    A reporting time window. `endTime` must be greater than `startTime`.
    """

    metric_scope: typing_extensions.Annotated[
        TrafficReportsResponseMetricScope,
        FieldMetadata(alias="metricScope"),
        pydantic.Field(
            alias="metricScope",
            description="The unit each `count` data point is measured in.\n- `session`: number of sessions.\n- `user`: number of unique users.\n- `pageview`: number of pageviews.",
        ),
    ]
    """
    The unit each `count` data point is measured in.
    - `session`: number of sessions.
    - `user`: number of unique users.
    - `pageview`: number of pageviews.
    """

    bucketing: TrafficReportsResponseBucketing = pydantic.Field()
    """
    Daily bucketing applied to a response.
    """

    data: typing.List[TrafficReportsResponseDataItem] = pydantic.Field()
    """
    Time-ordered series of data points covering the requested window.
    """

    filter: typing.Optional[TrafficReportsResponseFilter] = pydantic.Field(default=None)
    """
    Filter the traffic report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

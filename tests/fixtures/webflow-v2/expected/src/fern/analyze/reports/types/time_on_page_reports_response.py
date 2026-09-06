

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .time_on_page_reports_response_bucketing import TimeOnPageReportsResponseBucketing
from .time_on_page_reports_response_data_item import TimeOnPageReportsResponseDataItem
from .time_on_page_reports_response_filter import TimeOnPageReportsResponseFilter
from .time_on_page_reports_response_metric_scope import TimeOnPageReportsResponseMetricScope
from .time_on_page_reports_response_report import TimeOnPageReportsResponseReport
from .time_on_page_reports_response_window import TimeOnPageReportsResponseWindow


class TimeOnPageReportsResponse(UniversalBaseModel):
    """
    Response payload for the time on page report.
    """

    report: TimeOnPageReportsResponseReport = pydantic.Field()
    """
    Discriminator identifying the report type.
    """

    window: TimeOnPageReportsResponseWindow = pydantic.Field()
    """
    A reporting time window. `endTime` must be greater than `startTime`.
    """

    metric_scope: typing_extensions.Annotated[
        TimeOnPageReportsResponseMetricScope,
        FieldMetadata(alias="metricScope"),
        pydantic.Field(
            alias="metricScope",
            description="The unit each `averageSeconds` value is averaged over.\n- `session`: average time on page per session.\n- `user`: average time on page per unique user.\n- `pageview`: average time on page per pageview.",
        ),
    ]
    """
    The unit each `averageSeconds` value is averaged over.
    - `session`: average time on page per session.
    - `user`: average time on page per unique user.
    - `pageview`: average time on page per pageview.
    """

    bucketing: typing.Optional[TimeOnPageReportsResponseBucketing] = pydantic.Field(default=None)
    """
    Bucketing applied to a time on page response.
    """

    data: typing.List[TimeOnPageReportsResponseDataItem] = pydantic.Field()
    """
    Average time on page over the requested window — one aggregate point when `timeseries` is omitted, otherwise one point per bucket.
    """

    filter: typing.Optional[TimeOnPageReportsResponseFilter] = pydantic.Field(default=None)
    """
    Filter the time on page report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

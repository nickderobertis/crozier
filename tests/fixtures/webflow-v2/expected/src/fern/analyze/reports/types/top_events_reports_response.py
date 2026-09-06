

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .top_events_reports_response_bucketing import TopEventsReportsResponseBucketing
from .top_events_reports_response_data_item import TopEventsReportsResponseDataItem
from .top_events_reports_response_filter import TopEventsReportsResponseFilter
from .top_events_reports_response_report import TopEventsReportsResponseReport
from .top_events_reports_response_window import TopEventsReportsResponseWindow


class TopEventsReportsResponse(UniversalBaseModel):
    """
    Response payload for the top events report.
    """

    report: TopEventsReportsResponseReport = pydantic.Field()
    """
    Discriminator identifying the report type.
    """

    window: TopEventsReportsResponseWindow = pydantic.Field()
    """
    A reporting time window. `endTime` must be greater than `startTime`.
    """

    limit: int = pydantic.Field()
    """
    The row cap that was applied to this response (echoes the resolved request value, including the default).
    """

    bucketing: typing.Optional[TopEventsReportsResponseBucketing] = pydantic.Field(default=None)
    """
    Daily bucketing applied to a response.
    """

    data: typing.List[TopEventsReportsResponseDataItem] = pydantic.Field()
    """
    Events ranked by `count`, descending. At most `limit` rows.
    """

    filter: typing.Optional[TopEventsReportsResponseFilter] = pydantic.Field(default=None)
    """
    Filter the top events report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

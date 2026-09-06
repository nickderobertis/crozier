

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .top_pages_reports_response_bucketing import TopPagesReportsResponseBucketing
from .top_pages_reports_response_data_item import TopPagesReportsResponseDataItem
from .top_pages_reports_response_filter import TopPagesReportsResponseFilter
from .top_pages_reports_response_report import TopPagesReportsResponseReport
from .top_pages_reports_response_sort_by import TopPagesReportsResponseSortBy
from .top_pages_reports_response_window import TopPagesReportsResponseWindow


class TopPagesReportsResponse(UniversalBaseModel):
    """
    Response payload for the top pages report.
    """

    report: TopPagesReportsResponseReport = pydantic.Field()
    """
    Discriminator identifying the report type.
    """

    window: TopPagesReportsResponseWindow = pydantic.Field()
    """
    A reporting time window. `endTime` must be greater than `startTime`.
    """

    sort_by: typing_extensions.Annotated[
        TopPagesReportsResponseSortBy,
        FieldMetadata(alias="sortBy"),
        pydantic.Field(
            alias="sortBy",
            description="The metric used to rank rows in the response, descending. Row-level `sessionCount`, `userCount`, and `pageviewCount` are always all returned regardless of `sortBy`.\n- `session`: rank by session count (default).\n- `user`: rank by unique user count.\n- `pageview`: rank by pageview count.",
        ),
    ]
    """
    The metric used to rank rows in the response, descending. Row-level `sessionCount`, `userCount`, and `pageviewCount` are always all returned regardless of `sortBy`.
    - `session`: rank by session count (default).
    - `user`: rank by unique user count.
    - `pageview`: rank by pageview count.
    """

    limit: int = pydantic.Field()
    """
    The row cap that was applied to this response (echoes the resolved request value, including the default).
    """

    bucketing: typing.Optional[TopPagesReportsResponseBucketing] = pydantic.Field(default=None)
    """
    Daily bucketing applied to a response.
    """

    data: typing.List[TopPagesReportsResponseDataItem] = pydantic.Field()
    """
    Pages ranked by `sortBy`, descending. At most `limit` rows.
    """

    filter: typing.Optional[TopPagesReportsResponseFilter] = pydantic.Field(default=None)
    """
    Filter the top pages report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

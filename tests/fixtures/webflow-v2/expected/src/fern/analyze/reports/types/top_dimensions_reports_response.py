

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .top_dimensions_reports_response_data_item import TopDimensionsReportsResponseDataItem
from .top_dimensions_reports_response_dimension import TopDimensionsReportsResponseDimension
from .top_dimensions_reports_response_filter import TopDimensionsReportsResponseFilter
from .top_dimensions_reports_response_metric_scope import TopDimensionsReportsResponseMetricScope
from .top_dimensions_reports_response_report import TopDimensionsReportsResponseReport
from .top_dimensions_reports_response_window import TopDimensionsReportsResponseWindow


class TopDimensionsReportsResponse(UniversalBaseModel):
    """
    Response payload for the top dimensions report.
    """

    report: TopDimensionsReportsResponseReport = pydantic.Field()
    """
    Discriminator identifying the report type.
    """

    window: TopDimensionsReportsResponseWindow = pydantic.Field()
    """
    A reporting time window. `endTime` must be greater than `startTime`.
    """

    dimension: TopDimensionsReportsResponseDimension = pydantic.Field()
    """
    The dimension whose top values are ranked.
    - `country`: ISO 3166-1 alpha-2 country code (e.g., `US`).
    - `region`: first-level subdivision below country, keyed by ISO 3166-2 code (e.g., `US-CA`, with `name` `California, United States`).
    - `deviceType`: `desktop`, `mobile`, or `tablet`.
    - `os`: operating system name (e.g., `iOS`, `Windows NT`).
    - `browser`: browser name (e.g., `Chrome`, `Safari`).
    - `language`: the visitor's stated language preference (from the `Accept-Language` request header).
    - `locale`: the locale declared on the visited page (the page's `<html lang>` value).
    - `referrer`: referrer domain (e.g., `google.com`).
    - `trafficSource`: traffic source category, keyed by a code: `DN` Direct, `SP` Paid Search, `SO` Organic Search, `CP` Paid Social, `CO` Organic Social, `EM` Email, `RC` Recirculation, `OP` Other Paid, `OT` Other, `AI` Generative AI. `attributeKey` is the code; `name` is the label.
    - `utmCampaign`: `utm_campaign` value.
    - `utmContent`: `utm_content` value.
    - `utmMedium`: `utm_medium` value.
    - `utmSource`: `utm_source` value.
    - `utmTerm`: `utm_term` value.
    - `audienceIds`: Webflow audience identifier. For this dimension, `attributeKey` is the audience ID and `name` is the audience's display name (falling back to the ID if no display name is set).
    """

    metric_scope: typing_extensions.Annotated[
        TopDimensionsReportsResponseMetricScope,
        FieldMetadata(alias="metricScope"),
        pydantic.Field(
            alias="metricScope",
            description="The unit each row's `count` is measured in.\n- `session`: number of sessions attributed to the dimension value.\n- `user`: number of unique users attributed to the dimension value.",
        ),
    ]
    """
    The unit each row's `count` is measured in.
    - `session`: number of sessions attributed to the dimension value.
    - `user`: number of unique users attributed to the dimension value.
    """

    limit: int = pydantic.Field()
    """
    The row cap that was applied to this response (echoes the resolved request value, including the default).
    """

    data: typing.List[TopDimensionsReportsResponseDataItem] = pydantic.Field()
    """
    Dimension values ranked by `count`, descending. At most `limit` rows.
    """

    filter: typing.Optional[TopDimensionsReportsResponseFilter] = pydantic.Field(default=None)
    """
    Filter the top dimensions report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

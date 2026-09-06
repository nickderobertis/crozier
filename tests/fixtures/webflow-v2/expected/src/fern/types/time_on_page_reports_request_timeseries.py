

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .time_on_page_reports_request_timeseries_granularity_period import (
    TimeOnPageReportsRequestTimeseriesGranularityPeriod,
)


class TimeOnPageReportsRequestTimeseries(UniversalBaseModel):
    """
    Options that opt the time on page report into bucketed timeseries data.
    """

    granularity_period: typing_extensions.Annotated[
        TimeOnPageReportsRequestTimeseriesGranularityPeriod,
        FieldMetadata(alias="granularityPeriod"),
        pydantic.Field(
            alias="granularityPeriod",
            description="Bucket size for a time on page timeseries. `day` returns one value per day and `week` returns one value per week.",
        ),
    ]
    """
    Bucket size for a time on page timeseries. `day` returns one value per day and `week` returns one value per week.
    """

    bucket_time_zone: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="bucketTimeZone"),
        pydantic.Field(
            alias="bucketTimeZone",
            description="Valid IANA time zone used to align time bucket boundaries. Use canonical names such as `UTC` or `America/New_York`. Bucket timestamps are returned as UTC instants for local bucket starts in this time zone; for example, `America/New_York` local midnight on April 1, 2026 is returned as `2026-04-01T04:00:00.000Z`.",
        ),
    ]
    """
    Valid IANA time zone used to align time bucket boundaries. Use canonical names such as `UTC` or `America/New_York`. Bucket timestamps are returned as UTC instants for local bucket starts in this time zone; for example, `America/New_York` local midnight on April 1, 2026 is returned as `2026-04-01T04:00:00.000Z`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

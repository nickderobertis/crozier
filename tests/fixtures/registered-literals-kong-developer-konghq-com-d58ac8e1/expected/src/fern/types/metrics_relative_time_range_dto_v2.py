

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_relative_time_range_dto_v2time_range import MetricsRelativeTimeRangeDtoV2TimeRange


class MetricsRelativeTimeRangeDtoV2(UniversalBaseModel):
    """
    A duration representing a relative-to-now span of time. Generally the start time is floored to the requested granularity. Eg 7d from now, with 1day granularity initiated at 2024-01-08T17:11:00+05:00 will query for the time range from 2024-01-01T00:00:00+05:00 to 2024-01-08T17:11:00+05:00. The exact start and end timestamps are returned in the result query in the meta.start and meta.end fields. If the granularity for the previous query was 1hour, it would query a time range from 2024-01-01T17:00:00+05:00 to 2024-01-08T17:11:00+05:00.
    """

    tz: typing.Optional[str] = None
    time_range: MetricsRelativeTimeRangeDtoV2TimeRange

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

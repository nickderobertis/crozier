

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .telemetry_stats_response_pageviews import TelemetryStatsResponsePageviews
from .telemetry_stats_response_uniques import TelemetryStatsResponseUniques


class TelemetryStatsResponse(UniversalBaseModel):
    pageviews: TelemetryStatsResponsePageviews
    uniques: TelemetryStatsResponseUniques

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

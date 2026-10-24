

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .briefing_metric_format import BriefingMetricFormat
from .briefing_metric_series_item import BriefingMetricSeriesItem
from .briefing_metric_time_grain import BriefingMetricTimeGrain
from .briefing_metric_trend_mode import BriefingMetricTrendMode
from .briefing_metric_unit import BriefingMetricUnit


class BriefingMetric(UniversalBaseModel):
    key: str
    series_id: str
    label: str
    format: BriefingMetricFormat
    trend_mode: BriefingMetricTrendMode
    value: float
    currency: typing.Optional[str] = None
    unit: BriefingMetricUnit
    time_grain: BriefingMetricTimeGrain
    dimensions: typing.Dict[str, str]
    change_percent: typing.Optional[float] = None
    observed_at: dt.datetime
    source_import_id: str
    series: typing.List[BriefingMetricSeriesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

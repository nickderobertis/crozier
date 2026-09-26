

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_metrics_chart_chart_type import SessionMetricsChartChartType
from .session_metrics_chart_name import SessionMetricsChartName


class SessionMetricsChart(UniversalBaseModel):
    chart_type: SessionMetricsChartChartType
    description: str
    display_name: str
    name: SessionMetricsChartName

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

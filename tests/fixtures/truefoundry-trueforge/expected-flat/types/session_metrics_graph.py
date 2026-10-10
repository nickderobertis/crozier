

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_unit import MetricsUnit
from .session_metrics_chart_name import SessionMetricsChartName
from .session_metrics_graph_chart_type import SessionMetricsGraphChartType
from .session_metrics_graph_line import SessionMetricsGraphLine


class SessionMetricsGraph(UniversalBaseModel):
    chart_type: SessionMetricsGraphChartType
    description: str
    display_name: str
    graph_lines: typing.List[SessionMetricsGraphLine]
    name: SessionMetricsChartName
    unit: MetricsUnit

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

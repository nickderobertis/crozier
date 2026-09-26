

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_table_get_column_summaries_output_stats_value_max import MarimoTableGetColumnSummariesOutputStatsValueMax
from .marimo_table_get_column_summaries_output_stats_value_mean import MarimoTableGetColumnSummariesOutputStatsValueMean
from .marimo_table_get_column_summaries_output_stats_value_median import (
    MarimoTableGetColumnSummariesOutputStatsValueMedian,
)
from .marimo_table_get_column_summaries_output_stats_value_min import MarimoTableGetColumnSummariesOutputStatsValueMin
from .marimo_table_get_column_summaries_output_stats_value_p5 import MarimoTableGetColumnSummariesOutputStatsValueP5
from .marimo_table_get_column_summaries_output_stats_value_p25 import MarimoTableGetColumnSummariesOutputStatsValueP25
from .marimo_table_get_column_summaries_output_stats_value_p75 import MarimoTableGetColumnSummariesOutputStatsValueP75
from .marimo_table_get_column_summaries_output_stats_value_p95 import MarimoTableGetColumnSummariesOutputStatsValueP95
from .marimo_table_get_column_summaries_output_stats_value_std import MarimoTableGetColumnSummariesOutputStatsValueStd


class MarimoTableGetColumnSummariesOutputStatsValue(UniversalBaseModel):
    total: typing.Optional[float] = None
    nulls: typing.Optional[float] = None
    unique: typing.Optional[float] = None
    true: typing.Optional[float] = None
    false: typing.Optional[float] = None
    min: typing.Optional[MarimoTableGetColumnSummariesOutputStatsValueMin] = None
    max: typing.Optional[MarimoTableGetColumnSummariesOutputStatsValueMax] = None
    std: typing.Optional[MarimoTableGetColumnSummariesOutputStatsValueStd] = None
    mean: typing.Optional[MarimoTableGetColumnSummariesOutputStatsValueMean] = None
    median: typing.Optional[MarimoTableGetColumnSummariesOutputStatsValueMedian] = None
    p5: typing.Optional[MarimoTableGetColumnSummariesOutputStatsValueP5] = None
    p25: typing.Optional[MarimoTableGetColumnSummariesOutputStatsValueP25] = None
    p75: typing.Optional[MarimoTableGetColumnSummariesOutputStatsValueP75] = None
    p95: typing.Optional[MarimoTableGetColumnSummariesOutputStatsValueP95] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

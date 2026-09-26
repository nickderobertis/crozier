

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_table_preview_column_output_stats_max import MarimoTablePreviewColumnOutputStatsMax
from .marimo_table_preview_column_output_stats_mean import MarimoTablePreviewColumnOutputStatsMean
from .marimo_table_preview_column_output_stats_median import MarimoTablePreviewColumnOutputStatsMedian
from .marimo_table_preview_column_output_stats_min import MarimoTablePreviewColumnOutputStatsMin
from .marimo_table_preview_column_output_stats_p5 import MarimoTablePreviewColumnOutputStatsP5
from .marimo_table_preview_column_output_stats_p25 import MarimoTablePreviewColumnOutputStatsP25
from .marimo_table_preview_column_output_stats_p75 import MarimoTablePreviewColumnOutputStatsP75
from .marimo_table_preview_column_output_stats_p95 import MarimoTablePreviewColumnOutputStatsP95
from .marimo_table_preview_column_output_stats_std import MarimoTablePreviewColumnOutputStatsStd


class MarimoTablePreviewColumnOutputStats(UniversalBaseModel):
    total: typing.Optional[float] = None
    nulls: typing.Optional[float] = None
    unique: typing.Optional[float] = None
    true: typing.Optional[float] = None
    false: typing.Optional[float] = None
    min: typing.Optional[MarimoTablePreviewColumnOutputStatsMin] = None
    max: typing.Optional[MarimoTablePreviewColumnOutputStatsMax] = None
    std: typing.Optional[MarimoTablePreviewColumnOutputStatsStd] = None
    mean: typing.Optional[MarimoTablePreviewColumnOutputStatsMean] = None
    median: typing.Optional[MarimoTablePreviewColumnOutputStatsMedian] = None
    p5: typing.Optional[MarimoTablePreviewColumnOutputStatsP5] = None
    p25: typing.Optional[MarimoTablePreviewColumnOutputStatsP25] = None
    p75: typing.Optional[MarimoTablePreviewColumnOutputStatsP75] = None
    p95: typing.Optional[MarimoTablePreviewColumnOutputStatsP95] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

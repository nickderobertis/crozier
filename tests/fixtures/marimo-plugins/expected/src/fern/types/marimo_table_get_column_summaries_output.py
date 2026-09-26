

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_table_get_column_summaries_output_bin_values_value_item import (
    MarimoTableGetColumnSummariesOutputBinValuesValueItem,
)
from .marimo_table_get_column_summaries_output_data import MarimoTableGetColumnSummariesOutputData
from .marimo_table_get_column_summaries_output_stats_value import MarimoTableGetColumnSummariesOutputStatsValue
from .marimo_table_get_column_summaries_output_value_counts_value_item import (
    MarimoTableGetColumnSummariesOutputValueCountsValueItem,
)


class MarimoTableGetColumnSummariesOutput(UniversalBaseModel):
    data: typing.Optional[MarimoTableGetColumnSummariesOutputData] = None
    stats: typing.Dict[str, MarimoTableGetColumnSummariesOutputStatsValue]
    bin_values: typing.Dict[str, typing.List[MarimoTableGetColumnSummariesOutputBinValuesValueItem]]
    value_counts: typing.Dict[str, typing.List[MarimoTableGetColumnSummariesOutputValueCountsValueItem]]
    show_charts: bool
    is_disabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

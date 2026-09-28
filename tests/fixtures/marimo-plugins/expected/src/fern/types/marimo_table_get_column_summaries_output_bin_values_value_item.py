

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_table_get_column_summaries_output_bin_values_value_item_bin_end import (
    MarimoTableGetColumnSummariesOutputBinValuesValueItemBinEnd,
)
from .marimo_table_get_column_summaries_output_bin_values_value_item_bin_start import (
    MarimoTableGetColumnSummariesOutputBinValuesValueItemBinStart,
)


class MarimoTableGetColumnSummariesOutputBinValuesValueItem(UniversalBaseModel):
    bin_start: MarimoTableGetColumnSummariesOutputBinValuesValueItemBinStart
    bin_end: MarimoTableGetColumnSummariesOutputBinValuesValueItemBinEnd
    count: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .view_options_chart_annotations_symbol_grouping_type import ViewOptionsChartAnnotationsSymbolGroupingType


class ViewOptionsChartAnnotationsSymbolGrouping(UniversalBaseModel):
    type: ViewOptionsChartAnnotationsSymbolGroupingType
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

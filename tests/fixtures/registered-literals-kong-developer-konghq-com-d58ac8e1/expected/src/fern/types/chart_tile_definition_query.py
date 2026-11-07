

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .advanced_filters import AdvancedFilters
from .advanced_metrics import AdvancedMetrics
from .advanced_query_dimensions_item import AdvancedQueryDimensionsItem
from .granularity import Granularity
from .llm_filters import LlmFilters
from .llm_metrics import LlmMetrics
from .llm_query_dimensions_item import LlmQueryDimensionsItem
from .time_range import TimeRange


class ChartTileDefinitionQuery_ApiUsage(UniversalBaseModel):
    datasource: typing.Literal["api_usage"] = "api_usage"
    metrics: typing.Optional[AdvancedMetrics] = None
    dimensions: typing.Optional[typing.List[AdvancedQueryDimensionsItem]] = None
    filters: typing.Optional[AdvancedFilters] = None
    granularity: typing.Optional[Granularity] = None
    time_range: typing.Optional[TimeRange] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChartTileDefinitionQuery_LlmUsage(UniversalBaseModel):
    datasource: typing.Literal["llm_usage"] = "llm_usage"
    metrics: typing.Optional[LlmMetrics] = None
    dimensions: typing.Optional[typing.List[LlmQueryDimensionsItem]] = None
    filters: typing.Optional[LlmFilters] = None
    granularity: typing.Optional[Granularity] = None
    time_range: typing.Optional[TimeRange] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChartTileDefinitionQuery = typing_extensions.Annotated[
    typing.Union[ChartTileDefinitionQuery_ApiUsage, ChartTileDefinitionQuery_LlmUsage],
    pydantic.Field(discriminator="datasource"),
]

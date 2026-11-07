

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .granularity import Granularity
from .llm_filters import LlmFilters
from .llm_metrics import LlmMetrics
from .llm_query_dimensions_item import LlmQueryDimensionsItem
from .time_range import TimeRange


class LlmQuery(UniversalBaseModel):
    """
    A query targeting the LLM usage analytics datasource.
    """

    metrics: typing.Optional[LlmMetrics] = None
    dimensions: typing.Optional[typing.List[LlmQueryDimensionsItem]] = pydantic.Field(default=None)
    """
    List of attributes or entity types to group by.
    """

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

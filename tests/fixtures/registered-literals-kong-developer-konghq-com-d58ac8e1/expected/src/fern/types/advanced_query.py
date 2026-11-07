

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .advanced_filters import AdvancedFilters
from .advanced_metrics import AdvancedMetrics
from .advanced_query_dimensions_item import AdvancedQueryDimensionsItem
from .granularity import Granularity
from .time_range import TimeRange


class AdvancedQuery(UniversalBaseModel):
    """
    A query targeting the API usage analytics datasource.
    """

    metrics: typing.Optional[AdvancedMetrics] = None
    dimensions: typing.Optional[typing.List[AdvancedQueryDimensionsItem]] = pydantic.Field(default=None)
    """
    List of attributes or entity types to group by.
    """

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

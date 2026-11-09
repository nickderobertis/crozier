

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_llm_cache_status_filter_by_field_one_field import MetricsLlmCacheStatusFilterByFieldOneField
from .requests_filter_type_empty import RequestsFilterTypeEmpty


class MetricsLlmCacheStatusFilterByFieldOne(UniversalBaseModel):
    operator: RequestsFilterTypeEmpty
    field: MetricsLlmCacheStatusFilterByFieldOneField = pydantic.Field()
    """
    The field to filter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

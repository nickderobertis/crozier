

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_upstream_status_code_grouped_filter_by_field_one_field import (
    MetricsUpstreamStatusCodeGroupedFilterByFieldOneField,
)
from .requests_filter_type_empty import RequestsFilterTypeEmpty


class MetricsUpstreamStatusCodeGroupedFilterByFieldOne(UniversalBaseModel):
    operator: RequestsFilterTypeEmpty
    field: MetricsUpstreamStatusCodeGroupedFilterByFieldOneField = pydantic.Field()
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

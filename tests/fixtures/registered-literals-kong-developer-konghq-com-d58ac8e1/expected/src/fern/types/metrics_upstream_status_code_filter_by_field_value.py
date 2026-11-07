

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_upstream_status_code_filter_by_field_value_field import MetricsUpstreamStatusCodeFilterByFieldValueField
from .requests_filter_type import RequestsFilterType


class MetricsUpstreamStatusCodeFilterByFieldValue(UniversalBaseModel):
    operator: RequestsFilterType
    value: typing.List[int] = pydantic.Field()
    """
    The codes to include in the results.
    """

    field: MetricsUpstreamStatusCodeFilterByFieldValueField = pydantic.Field()
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



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_ai_response_model_filter_by_field_value_field import MetricsAiResponseModelFilterByFieldValueField
from .requests_filter_type import RequestsFilterType


class MetricsAiResponseModelFilterByFieldValue(UniversalBaseModel):
    operator: RequestsFilterType
    value: typing.List[str] = pydantic.Field()
    """
    The values to include in the results.
    """

    field: MetricsAiResponseModelFilterByFieldValueField = pydantic.Field()
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

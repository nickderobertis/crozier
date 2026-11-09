

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_api_product_version_filter_by_field_value_field import MetricsApiProductVersionFilterByFieldValueField
from .requests_filter_type import RequestsFilterType
from .unscoped_uuid import UnscopedUuid


class MetricsApiProductVersionFilterByFieldValue(UniversalBaseModel):
    operator: RequestsFilterType
    value: typing.List[UnscopedUuid] = pydantic.Field()
    """
    The IDs to include in the results.
    """

    field: MetricsApiProductVersionFilterByFieldValueField = pydantic.Field()
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

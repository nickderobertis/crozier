

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1alpha1metrics_bucket_value_explicit_bounds_item import V1Alpha1MetricsBucketValueExplicitBoundsItem
from .v1alpha1metrics_bucket_value_max import V1Alpha1MetricsBucketValueMax
from .v1alpha1metrics_bucket_value_min import V1Alpha1MetricsBucketValueMin
from .v1alpha1metrics_bucket_value_sum import V1Alpha1MetricsBucketValueSum


class V1Alpha1MetricsBucketValue(UniversalBaseModel):
    attributes: typing.Dict[str, typing.Any]
    start_time_unix_nano: int
    time_unix_nano: int
    count: int
    bucket_counts: typing.List[int]
    explicit_bounds: typing.List[V1Alpha1MetricsBucketValueExplicitBoundsItem]
    sum: V1Alpha1MetricsBucketValueSum
    min: V1Alpha1MetricsBucketValueMin
    max: V1Alpha1MetricsBucketValueMax

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

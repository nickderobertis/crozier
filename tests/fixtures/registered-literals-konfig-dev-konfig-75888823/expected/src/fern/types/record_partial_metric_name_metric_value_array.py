

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metric_value import MetricValue


class RecordPartialMetricNameMetricValueArray(UniversalBaseModel):
    """
    Construct a type with a set of properties K of type T
    """

    cpu: typing.Optional[typing.List[MetricValue]] = None
    memory: typing.Optional[typing.List[MetricValue]] = None
    rate_egress: typing.Optional[typing.List[MetricValue]] = None
    total_egress: typing.Optional[typing.List[MetricValue]] = None
    active_connections: typing.Optional[typing.List[MetricValue]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

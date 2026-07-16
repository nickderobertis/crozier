

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WeightedMetricValue(UniversalBaseModel):
    """
    Value of a metric with an associated weight
    """

    name: str = pydantic.Field()
    """
    Metric name or serie name
    """

    value: int = pydantic.Field()
    """
    The value of this metric
    """

    weight: int = pydantic.Field()
    """
    Weight of this metric value (typically a percentage)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

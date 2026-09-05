

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MetricSummary(UniversalBaseModel):
    """
    Summary of a metric's performance
    """

    name: str = pydantic.Field()
    """
    Name of the metric
    """

    metric: float = pydantic.Field()
    """
    Average metric across all examples
    """

    unit: str = pydantic.Field()
    """
    Unit label for the metric
    """

    diff: typing.Optional[float] = pydantic.Field(default=None)
    """
    Difference in metric between the current and comparison experiment
    """

    improvements: int = pydantic.Field()
    """
    Number of improvements in the metric
    """

    regressions: int = pydantic.Field()
    """
    Number of regressions in the metric
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

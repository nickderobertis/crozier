

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InsightsGetProjectWorkflowMetricsResponseItemsItemMetricsDurationMetrics(UniversalBaseModel):
    """
    Metrics relating to the duration of runs for a workflow.
    """

    min: int = pydantic.Field()
    """
    The minimum duration, in seconds, among a group of runs.
    """

    mean: int = pydantic.Field()
    """
    The mean duration, in seconds, among a group of runs.
    """

    median: int = pydantic.Field()
    """
    The median duration, in seconds, among a group of runs.
    """

    p95: int = pydantic.Field()
    """
    The 95th percentile duration, in seconds, among a group of runs.
    """

    max: int = pydantic.Field()
    """
    The max duration, in seconds, among a group of runs.
    """

    standard_deviation: float = pydantic.Field()
    """
    The standard deviation, in seconds, among a group of runs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

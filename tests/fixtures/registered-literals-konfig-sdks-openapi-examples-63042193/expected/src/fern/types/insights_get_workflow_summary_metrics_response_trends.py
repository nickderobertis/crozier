

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InsightsGetWorkflowSummaryMetricsResponseTrends(UniversalBaseModel):
    """
    Trends for aggregated metrics across a workflow for a given time window.
    """

    total_runs: float = pydantic.Field()
    """
    The trend value for total number of runs.
    """

    failed_runs: float = pydantic.Field()
    """
    The trend value for number of failed runs.
    """

    success_rate: float = pydantic.Field()
    """
    The trend value for the success rate.
    """

    p95duration_secs: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="p95_duration_secs"),
        pydantic.Field(
            alias="p95_duration_secs",
            description="Trend value for the 95th percentile duration for a workflow for a given time window.",
        ),
    ]
    """
    Trend value for the 95th percentile duration for a workflow for a given time window.
    """

    median_duration_secs: float = pydantic.Field()
    """
    Trend value for the 50th percentile duration for a workflow for a given time window.
    """

    total_credits_used: float = pydantic.Field()
    """
    The trend value for total credits consumed.
    """

    mttr: float = pydantic.Field()
    """
    trend for mean time to recovery (mean time between failures and their next success).
    """

    throughput: float = pydantic.Field()
    """
    Trend value for the average number of runs per day.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

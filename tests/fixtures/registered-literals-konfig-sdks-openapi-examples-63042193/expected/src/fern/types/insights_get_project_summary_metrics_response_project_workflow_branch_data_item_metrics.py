

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InsightsGetProjectSummaryMetricsResponseProjectWorkflowBranchDataItemMetrics(UniversalBaseModel):
    """
    Metrics aggregated across a workflow or branchfor a project.
    """

    total_credits_used: int = pydantic.Field()
    """
    The total credits consumed over the current timeseries interval.
    """

    p95duration_secs: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="p95_duration_secs"),
        pydantic.Field(
            alias="p95_duration_secs", description="The 95th percentile duration among a group of workflow runs."
        ),
    ]
    """
    The 95th percentile duration among a group of workflow runs.
    """

    total_runs: int = pydantic.Field()
    """
    The total number of runs, including runs that are still on-hold or running.
    """

    success_rate: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

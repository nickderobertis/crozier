

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InsightsGetProjectSummaryMetricsResponseProjectWorkflowDataItemTrends(UniversalBaseModel):
    """
    Trends aggregated across a workflow or branch for a project.
    """

    total_credits_used: float = pydantic.Field()
    """
    The trend value for total credits consumed.
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

    total_runs: float = pydantic.Field()
    """
    The trend value for total number of runs.
    """

    success_rate: float = pydantic.Field()
    """
    The trend value for the success rate.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

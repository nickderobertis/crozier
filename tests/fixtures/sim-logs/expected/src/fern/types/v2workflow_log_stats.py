

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2log_stats_segment import V2LogStatsSegment


class V2WorkflowLogStats(UniversalBaseModel):
    """
    Bucketed run counts and success rate for one workflow.
    """

    workflow_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflowId"),
        pydantic.Field(
            alias="workflowId",
            description="Workflow identifier, or the literal `deleted` for the single series that collects runs whose workflow no longer exists.",
        ),
    ]
    """
    Workflow identifier, or the literal `deleted` for the single series that collects runs whose workflow no longer exists.
    """

    workflow_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflowName"),
        pydantic.Field(alias="workflowName", description="Workflow name, or `Deleted Workflow`."),
    ]
    """
    Workflow name, or `Deleted Workflow`.
    """

    segments: typing.List[V2LogStatsSegment] = pydantic.Field()
    """
    One entry per bucket, in order, including buckets with no runs.
    """

    total_executions: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalExecutions"),
        pydantic.Field(alias="totalExecutions", description="Runs for this workflow across the window."),
    ]
    """
    Runs for this workflow across the window.
    """

    total_successful: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalSuccessful"),
        pydantic.Field(alias="totalSuccessful", description="Runs for this workflow that did not error."),
    ]
    """
    Runs for this workflow that did not error.
    """

    overall_success_rate: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="overallSuccessRate"),
        pydantic.Field(
            alias="overallSuccessRate",
            description="Percentage of runs that did not error, from 0 to 100. 100 when there were no runs.",
        ),
    ]
    """
    Percentage of runs that did not error, from 0 to 100. 100 when there were no runs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

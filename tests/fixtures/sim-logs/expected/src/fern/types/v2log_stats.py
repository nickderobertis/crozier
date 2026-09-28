

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2log_stats_segment import V2LogStatsSegment
from .v2log_stats_time_bounds import V2LogStatsTimeBounds
from .v2workflow_log_stats import V2WorkflowLogStats


class V2LogStats(UniversalBaseModel):
    """
    Bucketed success rate, error count, and latency for a workspace and each of its workflows.
    """

    workflows: typing.List[V2WorkflowLogStats] = pydantic.Field()
    """
    Per-workflow series, ordered by error rate descending then by name, capped at 200 entries.
    """

    workflows_truncated: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="workflowsTruncated"),
        pydantic.Field(
            alias="workflowsTruncated",
            description="Whether `workflows` was cut to 200 entries. The workspace totals and `aggregateSegments` are computed from every workflow before the cut, so they stay exact either way.",
        ),
    ]
    """
    Whether `workflows` was cut to 200 entries. The workspace totals and `aggregateSegments` are computed from every workflow before the cut, so they stay exact either way.
    """

    aggregate_segments: typing_extensions.Annotated[
        typing.List[V2LogStatsSegment],
        FieldMetadata(alias="aggregateSegments"),
        pydantic.Field(
            alias="aggregateSegments",
            description="Workspace-wide totals per bucket, in the same order as each workflow series.",
        ),
    ]
    """
    Workspace-wide totals per bucket, in the same order as each workflow series.
    """

    total_runs: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalRuns"),
        pydantic.Field(alias="totalRuns", description="Runs in the window across the whole workspace."),
    ]
    """
    Runs in the window across the whole workspace.
    """

    total_errors: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="totalErrors"),
        pydantic.Field(alias="totalErrors", description="Runs in the window that errored."),
    ]
    """
    Runs in the window that errored.
    """

    avg_latency: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="avgLatency"),
        pydantic.Field(
            alias="avgLatency",
            description="Mean run duration in milliseconds across the window, weighted by run count.",
        ),
    ]
    """
    Mean run duration in milliseconds across the window, weighted by run count.
    """

    time_bounds: typing_extensions.Annotated[
        V2LogStatsTimeBounds,
        FieldMetadata(alias="timeBounds"),
        pydantic.Field(
            alias="timeBounds",
            description="Actual bucket window. Supplied bounds are exact. Without `startDate`, the left edge is the oldest match, or 24 hours before the right edge when no run matches. Without `endDate`, the right edge is at least now. `startDate` alone spans through now.",
        ),
    ]
    """
    Actual bucket window. Supplied bounds are exact. Without `startDate`, the left edge is the oldest match, or 24 hours before the right edge when no run matches. Without `endDate`, the right edge is at least now. `startDate` alone spans through now.
    """

    segment_ms: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="segmentMs"),
        pydantic.Field(alias="segmentMs", description="Width of one bucket in milliseconds."),
    ]
    """
    Width of one bucket in milliseconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

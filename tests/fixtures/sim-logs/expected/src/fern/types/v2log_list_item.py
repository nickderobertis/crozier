

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .v2log_file import V2LogFile
from .v2log_list_item_cost import V2LogListItemCost
from .v2log_list_item_kind import V2LogListItemKind
from .v2log_list_item_status import V2LogListItemStatus
from .v2log_list_item_workflow import V2LogListItemWorkflow


class V2LogListItem(UniversalBaseModel):
    """
    Summary information for one workflow execution log.
    """

    kind: V2LogListItemKind = pydantic.Field()
    """
    Whether the run executed a workflow or a Chat / Sim-agent job. Job runs appear only when `includeJobRuns=true`.
    """

    run_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="runId"), pydantic.Field(alias="runId", description="Unique run identifier.")
    ]
    """
    Unique run identifier.
    """

    workflow_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workflowId"),
        pydantic.Field(alias="workflowId", description="Workflow identifier, or null when unavailable."),
    ] = None
    """
    Workflow identifier, or null when unavailable.
    """

    deployment_version_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="deploymentVersionId"),
        pydantic.Field(
            alias="deploymentVersionId", description="Deployment version identifier, or null when unavailable."
        ),
    ] = None
    """
    Deployment version identifier, or null when unavailable.
    """

    status: V2LogListItemStatus = pydantic.Field()
    """
    Current execution status, reported as persisted. `redacting` is transient while run output is scrubbed. `paused` is reported only when a resume attempt did not complete; a run held at a human-in-the-loop pause point reads `pending` here, and `paused` on the workflow run resources. Use those when the pause state matters.
    """

    level: str = pydantic.Field()
    """
    Log severity level.
    """

    trigger: str = pydantic.Field()
    """
    Trigger that started the run.
    """

    started_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startedAt"),
        pydantic.Field(alias="startedAt", description="ISO 8601 execution start timestamp."),
    ]
    """
    ISO 8601 execution start timestamp.
    """

    ended_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="endedAt"),
        pydantic.Field(
            alias="endedAt", description="ISO 8601 execution end timestamp, or null while the run is active."
        ),
    ] = None
    """
    ISO 8601 execution end timestamp, or null while the run is active.
    """

    total_duration_ms: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="totalDurationMs"),
        pydantic.Field(
            alias="totalDurationMs", description="Total execution duration in milliseconds, or null while unavailable."
        ),
    ] = None
    """
    Total execution duration in milliseconds, or null while unavailable.
    """

    cost: typing.Optional[V2LogListItemCost] = pydantic.Field(default=None)
    """
    Cost charged for the run, or null when the run has neither a recorded total nor an itemized ledger.
    """

    files: typing.Optional[typing.List[V2LogFile]] = pydantic.Field(default=None)
    """
    Files the run produced, or null when none are recorded. Only the run's own output files appear; input attachments a caller supplied are addressed through the files API instead.
    """

    workflow: typing.Optional[V2LogListItemWorkflow] = pydantic.Field(default=None)
    """
    Workflow summary for a full-detail result.
    """

    final_output: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="finalOutput"),
        pydantic.Field(alias="finalOutput", description="Final workflow output."),
    ] = None
    """
    Final workflow output.
    """

    trace_spans: typing_extensions.Annotated[
        typing.Optional[typing.List["LogTraceSpan"]],
        FieldMetadata(alias="traceSpans"),
        pydantic.Field(alias="traceSpans", description="Block-level execution trace spans."),
    ] = None
    """
    Block-level execution trace spans.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .log_trace_span import LogTraceSpan

update_forward_refs(V2LogListItem, LogTraceSpan=LogTraceSpan)

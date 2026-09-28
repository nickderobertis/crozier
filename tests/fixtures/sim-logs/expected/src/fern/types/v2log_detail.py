

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .v2log_detail_cost import V2LogDetailCost
from .v2log_detail_status import V2LogDetailStatus
from .v2log_detail_workflow import V2LogDetailWorkflow
from .v2log_file import V2LogFile


class V2LogDetail(UniversalBaseModel):
    """
    Detailed workflow execution log including state, trace, output, and cost.
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

    status: V2LogDetailStatus = pydantic.Field()
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

    files: typing.Optional[typing.List[V2LogFile]] = pydantic.Field(default=None)
    """
    Files the run produced, or null when none are recorded. Only the run's own output files appear; input attachments a caller supplied are addressed through the files API instead.
    """

    executed_by_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="executedByEmail"),
        pydantic.Field(
            alias="executedByEmail",
            description="Email of the identity the run executed as: the caller for an interactive or personal-API-key run, and the workspace billing account for a schedule, webhook, deployed chat, or public API call. Null when the run failed before an identity was resolved.",
        ),
    ] = None
    """
    Email of the identity the run executed as: the caller for an interactive or personal-API-key run, and the workspace billing account for a schedule, webhook, deployed chat, or public API call. Null when the run failed before an identity was resolved.
    """

    workflow: V2LogDetailWorkflow = pydantic.Field()
    """
    Workflow snapshot associated with the execution.
    """

    workflow_state: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="workflowState"),
        pydantic.Field(
            alias="workflowState",
            description="Workflow graph captured for the run, or null if unavailable. Sensitive values are redacted to null; environment-variable references may be preserved.",
        ),
    ] = None
    """
    Workflow graph captured for the run, or null if unavailable. Sensitive values are redacted to null; environment-variable references may be preserved.
    """

    trace_spans: typing_extensions.Annotated[
        typing.List["LogTraceSpan"],
        FieldMetadata(alias="traceSpans"),
        pydantic.Field(alias="traceSpans", description="Materialized block-level execution trace spans."),
    ]
    """
    Materialized block-level execution trace spans.
    """

    final_output: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="finalOutput"),
        pydantic.Field(
            alias="finalOutput", description="Materialized final workflow output, or null when none was produced."
        ),
    ] = None
    """
    Materialized final workflow output, or null when none was produced.
    """

    cost: typing.Optional[V2LogDetailCost] = pydantic.Field(default=None)
    """
    Cost charged for the run, or null when unavailable.
    """

    workflow_input: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="workflowInput"),
        pydantic.Field(
            alias="workflowInput",
            description="Input the run was triggered with, or null when the run recorded none. Credential-bearing and PII-masked values are redacted the same way `finalOutput` is.",
        ),
    ] = None
    """
    Input the run was triggered with, or null when the run recorded none. Credential-bearing and PII-masked values are redacted the same way `finalOutput` is.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="ISO 8601 log creation timestamp."),
    ]
    """
    ISO 8601 log creation timestamp.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .log_trace_span import LogTraceSpan

update_forward_refs(V2LogDetail, LogTraceSpan=LogTraceSpan)

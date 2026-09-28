

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .load_check_result import LoadCheckResult
from .load_scenario import LoadScenario
from .load_scenario_list_entry_stage_type import LoadScenarioListEntryStageType
from .load_scenario_list_entry_state import LoadScenarioListEntryState
from .load_scenario_list_entry_threshold_results_item import LoadScenarioListEntryThresholdResultsItem
from .load_scenario_list_entry_verdict import LoadScenarioListEntryVerdict


class LoadScenarioListEntry(UniversalBaseModel):
    """
    a registered load scenario with its lifecycle state, start delay, definition, and live/terminal status fields
    """

    name: typing.Optional[str] = None
    state: typing.Optional[LoadScenarioListEntryState] = None
    start_delay_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="startDelayMillis"), pydantic.Field(alias="startDelayMillis")
    ] = None
    definition: typing.Optional[LoadScenario] = None
    elapsed_millis: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="elapsedMillis"), pydantic.Field(alias="elapsedMillis")
    ] = None
    current_vus: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentVus"),
        pydantic.Field(alias="currentVus", description="live count of active virtual users (present when running)"),
    ] = None
    """
    live count of active virtual users (present when running)
    """

    stage_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="stageIndex"),
        pydantic.Field(
            alias="stageIndex", description="0-based index of the currently-running stage (present when running)"
        ),
    ] = None
    """
    0-based index of the currently-running stage (present when running)
    """

    stage_type: typing_extensions.Annotated[
        typing.Optional[LoadScenarioListEntryStageType],
        FieldMetadata(alias="stageType"),
        pydantic.Field(alias="stageType"),
    ] = None
    current_target: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="currentTarget"),
        pydantic.Field(
            alias="currentTarget",
            description="current setpoint for the running stage: target virtual users (VU), arrival rate in iterations/second (RATE), or 0 (PAUSE)",
        ),
    ] = None
    """
    current setpoint for the running stage: target virtual users (VU), arrival rate in iterations/second (RATE), or 0 (PAUSE)
    """

    requests_sent: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="requestsSent"), pydantic.Field(alias="requestsSent")
    ] = None
    succeeded: typing.Optional[int] = None
    failed: typing.Optional[int] = None
    p50millis: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="p50Millis"), pydantic.Field(alias="p50Millis")
    ] = None
    p95millis: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="p95Millis"), pydantic.Field(alias="p95Millis")
    ] = None
    p99millis: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="p99Millis"), pydantic.Field(alias="p99Millis")
    ] = None
    p999millis: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="p999Millis"),
        pydantic.Field(
            alias="p999Millis",
            description="99.9th-percentile coordinated-omission-corrected latency (ms), from the per-run HDR histogram; available even when metrics are disabled",
        ),
    ] = None
    """
    99.9th-percentile coordinated-omission-corrected latency (ms), from the per-run HDR histogram; available even when metrics are disabled
    """

    dropped_iterations: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="droppedIterations"),
        pydantic.Field(
            alias="droppedIterations",
            description="iterations that were due but never dispatched because a safety cap was hit (sum of rate_limit and inflight_cap throttles for this run)",
        ),
    ] = None
    """
    iterations that were due but never dispatched because a safety cap was hit (sum of rate_limit and inflight_cap throttles for this run)
    """

    verdict: typing.Optional[LoadScenarioListEntryVerdict] = pydantic.Field(default=None)
    """
    in-run threshold verdict: PASS (all thresholds satisfied) or FAIL (any breached); absent when the scenario has no thresholds or none has been evaluated yet. A terminal FAIL should be mapped by clients to a non-zero CI exit code.
    """

    aborted_by_threshold: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="abortedByThreshold"),
        pydantic.Field(
            alias="abortedByThreshold",
            description="true when this run was terminated early by an abortOnFail threshold breach; absent means false",
        ),
    ] = None
    """
    true when this run was terminated early by an abortOnFail threshold breach; absent means false
    """

    threshold_results: typing_extensions.Annotated[
        typing.Optional[typing.List[LoadScenarioListEntryThresholdResultsItem]],
        FieldMetadata(alias="thresholdResults"),
        pydantic.Field(
            alias="thresholdResults",
            description="per-threshold results behind the verdict (present when thresholds were evaluated)",
        ),
    ] = None
    """
    per-threshold results behind the verdict (present when thresholds were evaluated)
    """

    check_results: typing_extensions.Annotated[
        typing.Optional[typing.List[LoadCheckResult]],
        FieldMetadata(alias="checkResults"),
        pydantic.Field(
            alias="checkResults",
            description="per-distinct-check pass/fail aggregates for the run's per-step checks (present when any check was evaluated)",
        ),
    ] = None
    """
    per-distinct-check pass/fail aggregates for the run's per-step checks (present when any check was evaluated)
    """

    run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="runId"), pydantic.Field(alias="runId")
    ] = None
    started_at: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    ended_at: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="endedAt"), pydantic.Field(alias="endedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(LoadScenarioListEntry)

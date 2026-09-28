

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .load_check_result import LoadCheckResult
from .load_scenario_report_counts import LoadScenarioReportCounts
from .load_scenario_report_latency_millis import LoadScenarioReportLatencyMillis
from .load_scenario_report_state import LoadScenarioReportState
from .load_scenario_report_threshold_results_item import LoadScenarioReportThresholdResultsItem
from .load_scenario_report_timing import LoadScenarioReportTiming
from .load_scenario_report_verdict import LoadScenarioReportVerdict


class LoadScenarioReport(UniversalBaseModel):
    """
    end-of-run summary report for a load scenario run (JSON form). A JUnit-XML rendering of the same data is returned instead when the report endpoint is called with ?format=junit (Content-Type application/xml).
    """

    scenario: typing.Optional[str] = None
    run_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="runId"), pydantic.Field(alias="runId")
    ] = None
    state: typing.Optional[LoadScenarioReportState] = None
    verdict: typing.Optional[LoadScenarioReportVerdict] = pydantic.Field(default=None)
    """
    in-run threshold verdict; absent when the scenario has no thresholds or none has been evaluated yet
    """

    aborted_by_threshold: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="abortedByThreshold"),
        pydantic.Field(
            alias="abortedByThreshold",
            description="true when this run was terminated early by an abortOnFail threshold breach",
        ),
    ] = None
    """
    true when this run was terminated early by an abortOnFail threshold breach
    """

    timing: typing.Optional[LoadScenarioReportTiming] = None
    counts: typing.Optional[LoadScenarioReportCounts] = None
    latency_millis: typing_extensions.Annotated[
        typing.Optional[LoadScenarioReportLatencyMillis],
        FieldMetadata(alias="latencyMillis"),
        pydantic.Field(alias="latencyMillis"),
    ] = None
    threshold_results: typing_extensions.Annotated[
        typing.Optional[typing.List[LoadScenarioReportThresholdResultsItem]],
        FieldMetadata(alias="thresholdResults"),
        pydantic.Field(alias="thresholdResults", description="per-threshold results behind the verdict"),
    ] = None
    """
    per-threshold results behind the verdict
    """

    check_results: typing_extensions.Annotated[
        typing.Optional[typing.List[LoadCheckResult]],
        FieldMetadata(alias="checkResults"),
        pydantic.Field(
            alias="checkResults",
            description="per-distinct-check pass/fail aggregates for the run's per-step response checks",
        ),
    ] = None
    """
    per-distinct-check pass/fail aggregates for the run's per-step response checks
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

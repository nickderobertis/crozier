

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .load_feeder import LoadFeeder
from .load_pacing import LoadPacing
from .load_profile import LoadProfile
from .load_scenario_step_selection import LoadScenarioStepSelection
from .load_scenario_template_type import LoadScenarioTemplateType
from .load_step import LoadStep
from .load_threshold import LoadThreshold


class LoadScenario(UniversalBaseModel):
    """
    an API-driven load scenario: ordered templated steps driven at a target concurrency. The name is the unique registry key — PUT loads (registers) it; PUT /loadScenario/start triggers it to run.
    """

    name: str = pydantic.Field()
    """
    scenario name — the unique registry key. Loading the same name replaces the prior definition.
    """

    template_type: typing_extensions.Annotated[
        typing.Optional[LoadScenarioTemplateType],
        FieldMetadata(alias="templateType"),
        pydantic.Field(
            alias="templateType",
            description="template engine used to render the per-iteration request path and body; only VELOCITY and MUSTACHE are supported for load steps (JAVASCRIPT is rejected)",
        ),
    ] = None
    """
    template engine used to render the per-iteration request path and body; only VELOCITY and MUSTACHE are supported for load steps (JAVASCRIPT is rejected)
    """

    max_requests: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxRequests"),
        pydantic.Field(alias="maxRequests", description="optional hard cap on the total number of requests dispatched"),
    ] = None
    """
    optional hard cap on the total number of requests dispatched
    """

    start_delay_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="startDelayMillis"),
        pydantic.Field(
            alias="startDelayMillis",
            description="delay in milliseconds, applied after this scenario is triggered to start, before its iterations begin. A positive value means the scenario is PENDING until the delay elapses, then RUNNING; 0 (default) starts immediately on trigger. Lets several triggered scenarios begin at staggered offsets.",
        ),
    ] = None
    """
    delay in milliseconds, applied after this scenario is triggered to start, before its iterations begin. A positive value means the scenario is PENDING until the delay elapses, then RUNNING; 0 (default) starts immediately on trigger. Lets several triggered scenarios begin at staggered offsets.
    """

    labels: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    optional scenario-level custom annotation labels; exported as OpenTelemetry attributes on every load measurement and (for keys named in the loadGenerationMetricLabels allowlist) as extra Prometheus labels
    """

    thresholds: typing.Optional[typing.List[LoadThreshold]] = pydantic.Field(default=None)
    """
    optional in-run pass/fail thresholds; the run carries a PASS verdict iff all hold, FAIL otherwise. Empty/omitted means no verdict is computed.
    """

    abort_on_fail: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="abortOnFail"),
        pydantic.Field(
            alias="abortOnFail",
            description="when true, a FAIL verdict aborts the run early (terminal STOPPED state, abortedByThreshold set); default false (the run always finishes its stages and carries a final verdict)",
        ),
    ] = None
    """
    when true, a FAIL verdict aborts the run early (terminal STOPPED state, abortedByThreshold set); default false (the run always finishes its stages and carries a final verdict)
    """

    abort_grace_millis: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="abortGraceMillis"),
        pydantic.Field(
            alias="abortGraceMillis",
            description="suppress abortOnFail for the first N milliseconds of the run so noisy startup samples cannot trigger a premature abort (thresholds are still evaluated and a verdict still reported during the grace window — only the abort action is deferred)",
        ),
    ] = None
    """
    suppress abortOnFail for the first N milliseconds of the run so noisy startup samples cannot trigger a premature abort (thresholds are still evaluated and a verdict still reported during the grace window — only the abort action is deferred)
    """

    pacing: typing.Optional[LoadPacing] = None
    feeder: typing.Optional[LoadFeeder] = None
    profile: LoadProfile
    step_selection: typing_extensions.Annotated[
        typing.Optional[LoadScenarioStepSelection],
        FieldMetadata(alias="stepSelection"),
        pydantic.Field(
            alias="stepSelection",
            description="how each iteration selects which steps to run: SEQUENTIAL (default) runs ALL steps in declared order (a multi-step user journey); WEIGHTED runs exactly ONE step per iteration chosen at random proportional to each step's weight (mixed-workload modelling, e.g. 70% browse / 20% search / 10% checkout). Cross-step captures are meaningful only under SEQUENTIAL (a WEIGHTED iteration runs a single step); feeder data and pacing apply to both.",
        ),
    ] = None
    """
    how each iteration selects which steps to run: SEQUENTIAL (default) runs ALL steps in declared order (a multi-step user journey); WEIGHTED runs exactly ONE step per iteration chosen at random proportional to each step's weight (mixed-workload modelling, e.g. 70% browse / 20% search / 10% checkout). Cross-step captures are meaningful only under SEQUENTIAL (a WEIGHTED iteration runs a single step); feeder data and pacing apply to both.
    """

    steps: typing.List[LoadStep] = pydantic.Field()
    """
    ordered list of request steps. Under SEQUENTIAL stepSelection (default) all steps are fired in sequence each iteration; under WEIGHTED one step is chosen per iteration by weight (max 50)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(LoadScenario)

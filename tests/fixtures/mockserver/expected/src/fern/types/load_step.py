

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .http_request import HttpRequest
from .load_capture import LoadCapture
from .load_check import LoadCheck
from .load_step_think_time import LoadStepThinkTime


class LoadStep(UniversalBaseModel):
    """
    a single templated request step in a load scenario
    """

    request: HttpRequest
    think_time: typing_extensions.Annotated[
        typing.Optional[LoadStepThinkTime],
        FieldMetadata(alias="thinkTime"),
        pydantic.Field(alias="thinkTime", description="optional inter-step pause (a Delay)"),
    ] = None
    """
    optional inter-step pause (a Delay)
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional human label for this step; used as the 'step' metric label (otherwise the step index is used) and may be used as the low-cardinality 'route' metric label in place of the templatised request path
    """

    labels: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    optional step-level custom annotation labels, merged over the scenario labels (step keys win); exported as OpenTelemetry attributes on every load measurement and as allowlisted Prometheus labels
    """

    captures: typing.Optional[typing.List[LoadCapture]] = pydantic.Field(default=None)
    """
    optional cross-step capture rules applied to this step's response. Each binds an extracted value to a variable name visible to SUBSEQUENT steps in the same iteration via $iteration.captured.<name> (Velocity) / {{iteration.captured.<name>}} (Mustache), in path, body and header templates. Scope is per-iteration (one virtual user's single pass through the steps).
    """

    checks: typing.Optional[typing.List[LoadCheck]] = pydantic.Field(default=None)
    """
    optional per-step response assertions (k6 'check' parity). Each check extracts a value from this step's response and compares it against an expected value; pass/fail outcomes feed the mock_server_load_checks metric, the end-of-run report and the CHECK_FAILURE_RATE threshold. Observational — a failing check never fails an individual request or stops dispatch. Omitted (the default) leaves behaviour unchanged.
    """

    weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    relative selection weight, used only when the scenario's stepSelection is WEIGHTED: each iteration runs exactly ONE step chosen at random with probability proportional to its weight (e.g. weights 7 / 2 / 1 model a 70% / 20% / 10% mixed workload). Omitted means 1.0 in WEIGHTED mode; must be > 0 when WEIGHTED. Ignored under the default SEQUENTIAL mode (all steps run in order).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(LoadStep)

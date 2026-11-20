

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .glazing_step_kind import GlazingStepKind
from .step_config_reason import StepConfigReason
from .step_state import StepState


class GlazingStep(StepState):
    kind: typing.Optional[GlazingStepKind] = None
    coats: typing.Optional[int] = None
    id: typing.Optional[str] = None
    reason: typing.Optional[StepConfigReason] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_object_delta_step_details import RunStepDeltaObjectDeltaStepDetails


class RunStepDeltaObjectDelta(UniversalBaseModel):
    """
    The delta containing the fields that have changed on the run step.
    """

    step_details: typing.Optional[RunStepDeltaObjectDeltaStepDetails] = pydantic.Field(default=None)
    """
    The details of the run step.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

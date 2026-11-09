

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_object_delta import RunStepDeltaObjectDelta
from .run_step_delta_object_object import RunStepDeltaObjectObject


class RunStepDeltaObject(UniversalBaseModel):
    """
    Represents a run step delta i.e. any changed fields on a run step during streaming.
    """

    id: str = pydantic.Field()
    """
    The identifier of the run step, which can be referenced in API endpoints.
    """

    object: RunStepDeltaObjectObject = pydantic.Field()
    """
    The object type, which is always `thread.run.step.delta`.
    """

    delta: RunStepDeltaObjectDelta = pydantic.Field()
    """
    The delta containing the fields that have changed on the run step.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

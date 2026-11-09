

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_step_details_message_creation_object_message_creation import (
    RunStepDeltaStepDetailsMessageCreationObjectMessageCreation,
)


class RunStepDeltaStepDetailsMessageCreationObject(UniversalBaseModel):
    """
    Details of the message creation by the run step.
    """

    message_creation: typing.Optional[RunStepDeltaStepDetailsMessageCreationObjectMessageCreation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

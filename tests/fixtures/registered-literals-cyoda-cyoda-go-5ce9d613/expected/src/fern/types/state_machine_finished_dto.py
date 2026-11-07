

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflow_stop_reason_dto import WorkflowStopReasonDto


class StateMachineFinishedDto(UniversalBaseModel):
    state: str = pydantic.Field()
    """
    The state of the entity when the state machine flow was finished
    """

    success: bool = pydantic.Field()
    """
    Whether the state machine execution was successful
    """

    stop_reason: typing_extensions.Annotated[
        WorkflowStopReasonDto, FieldMetadata(alias="stopReason"), pydantic.Field(alias="stopReason")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .state_machine_event_dto import StateMachineEventDto


class StateMachineTransitionNotFoundDto(StateMachineEventDto):
    workflow_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflowName"),
        pydantic.Field(alias="workflowName", description="Name of the workflow"),
    ]
    """
    Name of the workflow
    """

    transition: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the transition that was not found
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

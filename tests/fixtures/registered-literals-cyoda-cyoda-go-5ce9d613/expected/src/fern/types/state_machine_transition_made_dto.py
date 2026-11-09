

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .state_machine_event_dto import StateMachineEventDto


class StateMachineTransitionMadeDto(StateMachineEventDto):
    workflow_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflowName"),
        pydantic.Field(alias="workflowName", description="Name of the workflow"),
    ]
    """
    Name of the workflow
    """

    transition: str = pydantic.Field()
    """
    Name of the transition that was made
    """

    new_state: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="newState"),
        pydantic.Field(alias="newState", description="New state after the transition"),
    ]
    """
    New state after the transition
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow



import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .state_machine_event_dto import StateMachineEventDto


class StateMachineTransitionCriterionNotMatchedDto(StateMachineEventDto):
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
    Name of the transition
    """

    criterion: str = pydantic.Field()
    """
    Name of the criterion that was not matched
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Why the criterion blocked the passage: the criteria compute node's explanation, or "criterion did not match" when none was supplied. Present on events recorded since this field was introduced; older audit events omit it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

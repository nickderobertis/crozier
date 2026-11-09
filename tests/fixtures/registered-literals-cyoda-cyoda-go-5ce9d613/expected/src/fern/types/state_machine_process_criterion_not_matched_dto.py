

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .state_machine_event_dto import StateMachineEventDto


class StateMachineProcessCriterionNotMatchedDto(StateMachineEventDto):
    workflow_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workflowName"),
        pydantic.Field(alias="workflowName", description="Name of the workflow"),
    ]
    """
    Name of the workflow
    """

    processor_class_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="processorClassName"),
        pydantic.Field(alias="processorClassName", description="Fully qualified class name of the processor"),
    ]
    """
    Fully qualified class name of the processor
    """

    criterion: str = pydantic.Field()
    """
    Name of the criterion that was not matched
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason why the criterion was not matched
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

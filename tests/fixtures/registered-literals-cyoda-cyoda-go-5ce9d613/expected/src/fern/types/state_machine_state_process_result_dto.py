

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .state_machine_event_dto import StateMachineEventDto
from .state_machine_state_process_result_dto_state_process_type import StateMachineStateProcessResultDtoStateProcessType
from .state_process_id_dto import StateProcessIdDto


class StateMachineStateProcessResultDto(StateMachineEventDto):
    state_process_id: typing_extensions.Annotated[
        StateProcessIdDto, FieldMetadata(alias="stateProcessId"), pydantic.Field(alias="stateProcessId")
    ]
    state_process_class_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="stateProcessClassName"),
        pydantic.Field(alias="stateProcessClassName", description="Fully qualified class name of the state process"),
    ]
    """
    Fully qualified class name of the state process
    """

    state_process_type: typing_extensions.Annotated[
        StateMachineStateProcessResultDtoStateProcessType,
        FieldMetadata(alias="stateProcessType"),
        pydantic.Field(alias="stateProcessType"),
    ]
    fail_reason: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="failReason"),
        pydantic.Field(alias="failReason", description="Reason for failure, if applicable"),
    ] = None
    """
    Reason for failure, if applicable
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

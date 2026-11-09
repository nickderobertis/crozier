

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .audit_event_dto import AuditEventDto
from .state_machine_audit_event_dto_data import StateMachineAuditEventDtoData
from .state_machine_audit_event_dto_event_type import StateMachineAuditEventDtoEventType


class StateMachineAuditEventDto(AuditEventDto):
    state: str = pydantic.Field()
    """
    State of the entity where the event occurred within the state machine
    """

    event_type: typing_extensions.Annotated[
        StateMachineAuditEventDtoEventType,
        FieldMetadata(alias="eventType"),
        pydantic.Field(alias="eventType", description="Type of the state machine event"),
    ]
    """
    Type of the state machine event
    """

    data: typing.Optional[StateMachineAuditEventDtoData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

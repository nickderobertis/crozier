

import typing

from .entity_change_audit_event_dto import EntityChangeAuditEventDto
from .state_machine_audit_event_dto import StateMachineAuditEventDto
from .system_audit_event_dto import SystemAuditEventDto

EntityAuditEventsResponseDtoItemsItem = typing.Union[
    EntityChangeAuditEventDto, StateMachineAuditEventDto, SystemAuditEventDto
]

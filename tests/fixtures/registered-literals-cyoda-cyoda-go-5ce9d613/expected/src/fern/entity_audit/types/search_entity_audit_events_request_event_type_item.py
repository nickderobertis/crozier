

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchEntityAuditEventsRequestEventTypeItem(enum.StrEnum):
    STATE_MACHINE = "StateMachine"
    ENTITY_CHANGE = "EntityChange"
    SYSTEM = "System"

    def visit(
        self,
        state_machine: typing.Callable[[], T_Result],
        entity_change: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchEntityAuditEventsRequestEventTypeItem.STATE_MACHINE:
            return state_machine()
        if self is SearchEntityAuditEventsRequestEventTypeItem.ENTITY_CHANGE:
            return entity_change()
        if self is SearchEntityAuditEventsRequestEventTypeItem.SYSTEM:
            return system()

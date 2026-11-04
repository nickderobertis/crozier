

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MaintenanceReason(enum.StrEnum):
    SCHEDULED = "Scheduled"
    INCIDENT = "Incident"
    CAPACITY = "Capacity"

    def visit(
        self,
        scheduled: typing.Callable[[], T_Result],
        incident: typing.Callable[[], T_Result],
        capacity: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MaintenanceReason.SCHEDULED:
            return scheduled()
        if self is MaintenanceReason.INCIDENT:
            return incident()
        if self is MaintenanceReason.CAPACITY:
            return capacity()

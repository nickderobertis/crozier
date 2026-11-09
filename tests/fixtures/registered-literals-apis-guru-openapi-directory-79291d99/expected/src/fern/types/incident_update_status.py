

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IncidentUpdateStatus(enum.StrEnum):
    """
    The status of the incident.
    """

    INVESTIGATING = "INVESTIGATING"
    IDENTIFIED = "IDENTIFIED"
    SCHEDULED = "SCHEDULED"
    RESOLVED = "RESOLVED"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        investigating: typing.Callable[[], T_Result],
        identified: typing.Callable[[], T_Result],
        scheduled: typing.Callable[[], T_Result],
        resolved: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IncidentUpdateStatus.INVESTIGATING:
            return investigating()
        if self is IncidentUpdateStatus.IDENTIFIED:
            return identified()
        if self is IncidentUpdateStatus.SCHEDULED:
            return scheduled()
        if self is IncidentUpdateStatus.RESOLVED:
            return resolved()
        if self is IncidentUpdateStatus.UNKNOWN:
            return unknown()

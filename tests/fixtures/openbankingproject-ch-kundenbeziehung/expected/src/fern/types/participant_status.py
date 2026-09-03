

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        suspended: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantStatus.ACTIVE:
            return active()
        if self is ParticipantStatus.INACTIVE:
            return inactive()
        if self is ParticipantStatus.SUSPENDED:
            return suspended()

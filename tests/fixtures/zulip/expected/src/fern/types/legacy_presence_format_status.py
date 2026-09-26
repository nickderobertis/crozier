

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LegacyPresenceFormatStatus(enum.StrEnum):
    """
    The status of the user on this client. Will be either `"idle"`
    or `"active"`.
    """

    IDLE = "idle"
    ACTIVE = "active"

    def visit(self, idle: typing.Callable[[], T_Result], active: typing.Callable[[], T_Result]) -> T_Result:
        if self is LegacyPresenceFormatStatus.IDLE:
            return idle()
        if self is LegacyPresenceFormatStatus.ACTIVE:
            return active()

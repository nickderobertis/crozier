

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PipelinesUpdateRequestDesiredStatus(enum.StrEnum):
    """
    Set to "paused" to pause, "active" to resume, "deleted" to tear down.
    """

    ACTIVE = "active"
    PAUSED = "paused"
    DELETED = "deleted"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PipelinesUpdateRequestDesiredStatus.ACTIVE:
            return active()
        if self is PipelinesUpdateRequestDesiredStatus.PAUSED:
            return paused()
        if self is PipelinesUpdateRequestDesiredStatus.DELETED:
            return deleted()

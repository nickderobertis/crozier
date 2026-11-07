

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineDesiredStatus(enum.StrEnum):
    """
    User-controlled lifecycle state. Set via PATCH to pause, resume, or delete.
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
        if self is PipelineDesiredStatus.ACTIVE:
            return active()
        if self is PipelineDesiredStatus.PAUSED:
            return paused()
        if self is PipelineDesiredStatus.DELETED:
            return deleted()

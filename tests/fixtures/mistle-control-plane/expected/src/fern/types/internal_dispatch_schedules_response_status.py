

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InternalDispatchSchedulesResponseStatus(enum.StrEnum):
    QUEUED = "queued"

    def visit(self, queued: typing.Callable[[], T_Result]) -> T_Result:
        if self is InternalDispatchSchedulesResponseStatus.QUEUED:
            return queued()

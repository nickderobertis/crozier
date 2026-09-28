

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReviewDraftStatus(enum.StrEnum):
    GENERATING = "generating"
    READY = "ready"
    FAILED = "failed"

    def visit(
        self,
        generating: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReviewDraftStatus.GENERATING:
            return generating()
        if self is ReviewDraftStatus.READY:
            return ready()
        if self is ReviewDraftStatus.FAILED:
            return failed()

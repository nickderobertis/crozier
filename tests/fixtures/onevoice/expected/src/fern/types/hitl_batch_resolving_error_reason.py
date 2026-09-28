

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HitlBatchResolvingErrorReason(enum.StrEnum):
    CONCURRENT_RESOLVE_IN_PROGRESS = "concurrent resolve in progress"

    def visit(self, concurrent_resolve_in_progress: typing.Callable[[], T_Result]) -> T_Result:
        if self is HitlBatchResolvingErrorReason.CONCURRENT_RESOLVE_IN_PROGRESS:
            return concurrent_resolve_in_progress()

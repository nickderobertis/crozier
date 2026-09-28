

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HitlBatchResolvingErrorError(enum.StrEnum):
    BATCH_RESOLVING = "batch resolving"

    def visit(self, batch_resolving: typing.Callable[[], T_Result]) -> T_Result:
        if self is HitlBatchResolvingErrorError.BATCH_RESOLVING:
            return batch_resolving()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HitlAlreadyResolvedErrorError(enum.StrEnum):
    BATCH_ALREADY_RESOLVED = "batch already resolved"

    def visit(self, batch_already_resolved: typing.Callable[[], T_Result]) -> T_Result:
        if self is HitlAlreadyResolvedErrorError.BATCH_ALREADY_RESOLVED:
            return batch_already_resolved()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HitlAlreadyResolvedErrorReason(enum.StrEnum):
    ALREADY_RESOLVED = "already_resolved"

    def visit(self, already_resolved: typing.Callable[[], T_Result]) -> T_Result:
        if self is HitlAlreadyResolvedErrorReason.ALREADY_RESOLVED:
            return already_resolved()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MissionResetReason(enum.StrEnum):
    RETENTION_GAP = "retention_gap"

    def visit(self, retention_gap: typing.Callable[[], T_Result]) -> T_Result:
        if self is MissionResetReason.RETENTION_GAP:
            return retention_gap()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class N2InfoNotifyReason(enum.StrEnum):
    HANDOVER_COMPLETED = "HANDOVER_COMPLETED"

    def visit(self, handover_completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is N2InfoNotifyReason.HANDOVER_COMPLETED:
            return handover_completed()

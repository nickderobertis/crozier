

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreemptionCapability(enum.StrEnum):
    NOT_PREEMPT = "NOT_PREEMPT"
    MAY_PREEMPT = "MAY_PREEMPT"

    def visit(self, not_preempt: typing.Callable[[], T_Result], may_preempt: typing.Callable[[], T_Result]) -> T_Result:
        if self is PreemptionCapability.NOT_PREEMPT:
            return not_preempt()
        if self is PreemptionCapability.MAY_PREEMPT:
            return may_preempt()

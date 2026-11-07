

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyDecisionV2Decision(enum.StrEnum):
    APPROVE = "approve"
    ESCALATE = "escalate"
    BLOCK = "block"

    def visit(
        self,
        approve: typing.Callable[[], T_Result],
        escalate: typing.Callable[[], T_Result],
        block: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PolicyDecisionV2Decision.APPROVE:
            return approve()
        if self is PolicyDecisionV2Decision.ESCALATE:
            return escalate()
        if self is PolicyDecisionV2Decision.BLOCK:
            return block()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApprovalInteractionKind(enum.StrEnum):
    APPROVAL = "approval"

    def visit(self, approval: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApprovalInteractionKind.APPROVAL:
            return approval()

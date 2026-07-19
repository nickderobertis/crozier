

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApprovalCreateType(enum.StrEnum):
    """
    The message type to be created.
    """

    APPROVAL = "approval"

    def visit(self, approval: typing.Callable[[], T_Result]) -> T_Result:
        if self is ApprovalCreateType.APPROVAL:
            return approval()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActApproveActionResponseType(enum.StrEnum):
    APPROVE = "approve"

    def visit(self, approve: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActApproveActionResponseType.APPROVE:
            return approve()

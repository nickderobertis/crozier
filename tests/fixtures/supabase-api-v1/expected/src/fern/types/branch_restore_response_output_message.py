

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BranchRestoreResponseOutputMessage(enum.StrEnum):
    BRANCH_RESTORATION_INITIATED = "Branch restoration initiated"

    def visit(self, branch_restoration_initiated: typing.Callable[[], T_Result]) -> T_Result:
        if self is BranchRestoreResponseOutputMessage.BRANCH_RESTORATION_INITIATED:
            return branch_restoration_initiated()

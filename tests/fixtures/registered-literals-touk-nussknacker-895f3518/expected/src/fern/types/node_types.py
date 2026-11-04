

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTypes(enum.StrEnum):
    BRANCH_END_DATA = "BranchEndData"

    def visit(self, branch_end_data: typing.Callable[[], T_Result]) -> T_Result:
        if self is NodeTypes.BRANCH_END_DATA:
            return branch_end_data()

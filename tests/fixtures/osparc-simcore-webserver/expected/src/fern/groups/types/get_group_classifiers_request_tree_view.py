

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetGroupClassifiersRequestTreeView(enum.StrEnum):
    STD = "std"

    def visit(self, std: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetGroupClassifiersRequestTreeView.STD:
            return std()

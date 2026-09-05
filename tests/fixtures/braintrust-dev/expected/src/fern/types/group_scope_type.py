

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GroupScopeType(enum.StrEnum):
    GROUP = "group"

    def visit(self, group: typing.Callable[[], T_Result]) -> T_Result:
        if self is GroupScopeType.GROUP:
            return group()

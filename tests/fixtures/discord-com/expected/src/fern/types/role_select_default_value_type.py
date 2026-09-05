

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoleSelectDefaultValueType(enum.StrEnum):
    ROLE = "role"

    def visit(self, role: typing.Callable[[], T_Result]) -> T_Result:
        if self is RoleSelectDefaultValueType.ROLE:
            return role()

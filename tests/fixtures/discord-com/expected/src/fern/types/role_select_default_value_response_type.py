

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoleSelectDefaultValueResponseType(enum.StrEnum):
    ROLE = "role"

    def visit(self, role: typing.Callable[[], T_Result]) -> T_Result:
        if self is RoleSelectDefaultValueResponseType.ROLE:
            return role()

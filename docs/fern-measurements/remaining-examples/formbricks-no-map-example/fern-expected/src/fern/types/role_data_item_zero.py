

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoleDataItemZero(enum.StrEnum):
    OWNER = "owner"

    def visit(self, owner: typing.Callable[[], T_Result]) -> T_Result:
        if self is RoleDataItemZero.OWNER:
            return owner()

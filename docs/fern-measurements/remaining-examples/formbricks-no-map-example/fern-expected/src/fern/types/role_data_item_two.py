

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoleDataItemTwo(enum.StrEnum):
    MEMBER = "member"

    def visit(self, member: typing.Callable[[], T_Result]) -> T_Result:
        if self is RoleDataItemTwo.MEMBER:
            return member()

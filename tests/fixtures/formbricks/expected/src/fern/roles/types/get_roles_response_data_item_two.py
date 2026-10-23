

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetRolesResponseDataItemTwo(enum.StrEnum):
    MEMBER = "member"

    def visit(self, member: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRolesResponseDataItemTwo.MEMBER:
            return member()

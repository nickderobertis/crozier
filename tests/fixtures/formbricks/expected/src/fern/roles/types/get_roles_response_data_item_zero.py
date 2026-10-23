

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetRolesResponseDataItemZero(enum.StrEnum):
    OWNER = "owner"

    def visit(self, owner: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRolesResponseDataItemZero.OWNER:
            return owner()

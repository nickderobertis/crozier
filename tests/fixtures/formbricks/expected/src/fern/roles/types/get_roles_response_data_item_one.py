

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetRolesResponseDataItemOne(enum.StrEnum):
    MANAGER = "manager"

    def visit(self, manager: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRolesResponseDataItemOne.MANAGER:
            return manager()

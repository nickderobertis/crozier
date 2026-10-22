

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoleDataItemThree(enum.StrEnum):
    BILLING = "billing"

    def visit(self, billing: typing.Callable[[], T_Result]) -> T_Result:
        if self is RoleDataItemThree.BILLING:
            return billing()

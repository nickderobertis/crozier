

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetDeleteStackSetRequestCallAs(enum.StrEnum):
    SELF = "SELF"
    DELEGATED_ADMIN = "DELEGATED_ADMIN"

    def visit(self, self_: typing.Callable[[], T_Result], delegated_admin: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDeleteStackSetRequestCallAs.SELF:
            return self_()
        if self is GetDeleteStackSetRequestCallAs.DELEGATED_ADMIN:
            return delegated_admin()

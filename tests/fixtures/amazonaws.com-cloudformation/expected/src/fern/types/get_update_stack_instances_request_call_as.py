

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetUpdateStackInstancesRequestCallAs(enum.StrEnum):
    SELF = "SELF"
    DELEGATED_ADMIN = "DELEGATED_ADMIN"

    def visit(self, self_: typing.Callable[[], T_Result], delegated_admin: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetUpdateStackInstancesRequestCallAs.SELF:
            return self_()
        if self is GetUpdateStackInstancesRequestCallAs.DELEGATED_ADMIN:
            return delegated_admin()

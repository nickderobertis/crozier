

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDescribeStackInstanceRequestCallAs(str, enum.Enum):
    SELF = "SELF"
    DELEGATED_ADMIN = "DELEGATED_ADMIN"

    def visit(self, self_: typing.Callable[[], T_Result], delegated_admin: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDescribeStackInstanceRequestCallAs.SELF:
            return self_()
        if self is GetDescribeStackInstanceRequestCallAs.DELEGATED_ADMIN:
            return delegated_admin()

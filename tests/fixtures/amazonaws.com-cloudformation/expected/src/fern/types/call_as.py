

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CallAs(str, enum.Enum):
    SELF = "SELF"
    DELEGATED_ADMIN = "DELEGATED_ADMIN"

    def visit(self, self_: typing.Callable[[], T_Result], delegated_admin: typing.Callable[[], T_Result]) -> T_Result:
        if self is CallAs.SELF:
            return self_()
        if self is CallAs.DELEGATED_ADMIN:
            return delegated_admin()



import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AdminListUsersRequestAsc(str, enum.Enum):
    TRUE = "true"

    def visit(self, true: typing.Callable[[], T_Result]) -> T_Result:
        if self is AdminListUsersRequestAsc.TRUE:
            return true()

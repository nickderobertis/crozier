

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AdminListUsersRequestAsc(enum.StrEnum):
    TRUE = "true"

    def visit(self, true: typing.Callable[[], T_Result]) -> T_Result:
        if self is AdminListUsersRequestAsc.TRUE:
            return true()

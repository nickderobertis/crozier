

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListUsersRequestFilter(enum.StrEnum):
    DELETED = "deleted"

    def visit(self, deleted: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListUsersRequestFilter.DELETED:
            return deleted()

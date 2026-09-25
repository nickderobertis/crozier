

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsSortBy(enum.StrEnum):
    CREATED_TIME = "createdTime"

    def visit(self, created_time: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocumentsSortBy.CREATED_TIME:
            return created_time()



import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostGetStatusRequestOperation(enum.StrEnum):
    GET_STATUS = "GetStatus"

    def visit(self, get_status: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostGetStatusRequestOperation.GET_STATUS:
            return get_status()

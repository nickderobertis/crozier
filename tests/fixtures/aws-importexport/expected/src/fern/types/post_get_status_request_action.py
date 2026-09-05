

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostGetStatusRequestAction(enum.StrEnum):
    GET_STATUS = "GetStatus"

    def visit(self, get_status: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostGetStatusRequestAction.GET_STATUS:
            return get_status()

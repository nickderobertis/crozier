

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetGetStatusRequestOperation(enum.StrEnum):
    GET_STATUS = "GetStatus"

    def visit(self, get_status: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetGetStatusRequestOperation.GET_STATUS:
            return get_status()

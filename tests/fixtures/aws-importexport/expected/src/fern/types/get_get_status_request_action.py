

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetGetStatusRequestAction(enum.StrEnum):
    GET_STATUS = "GetStatus"

    def visit(self, get_status: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetGetStatusRequestAction.GET_STATUS:
            return get_status()

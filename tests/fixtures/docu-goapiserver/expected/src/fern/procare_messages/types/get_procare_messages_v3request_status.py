

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetProcareMessagesV3RequestStatus(enum.StrEnum):
    INCOMPLETE = "incomplete"

    def visit(self, incomplete: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetProcareMessagesV3RequestStatus.INCOMPLETE:
            return incomplete()

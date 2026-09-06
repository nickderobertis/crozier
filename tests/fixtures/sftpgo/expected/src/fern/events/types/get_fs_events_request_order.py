

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFsEventsRequestOrder(enum.StrEnum):
    ASC = "ASC"
    DESC = "DESC"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetFsEventsRequestOrder.ASC:
            return asc()
        if self is GetFsEventsRequestOrder.DESC:
            return desc()

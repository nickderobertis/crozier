

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCausesOfActionRequestOrder(enum.StrEnum):
    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetCausesOfActionRequestOrder.ASC:
            return asc()
        if self is GetCausesOfActionRequestOrder.DESC:
            return desc()

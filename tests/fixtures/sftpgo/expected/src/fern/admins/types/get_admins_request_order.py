

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAdminsRequestOrder(enum.StrEnum):
    ASC = "ASC"
    DESC = "DESC"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetAdminsRequestOrder.ASC:
            return asc()
        if self is GetAdminsRequestOrder.DESC:
            return desc()

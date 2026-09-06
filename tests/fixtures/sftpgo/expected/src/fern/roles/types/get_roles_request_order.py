

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetRolesRequestOrder(enum.StrEnum):
    ASC = "ASC"
    DESC = "DESC"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRolesRequestOrder.ASC:
            return asc()
        if self is GetRolesRequestOrder.DESC:
            return desc()

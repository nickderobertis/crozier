

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetIpListEntriesRequestOrder(enum.StrEnum):
    ASC = "ASC"
    DESC = "DESC"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetIpListEntriesRequestOrder.ASC:
            return asc()
        if self is GetIpListEntriesRequestOrder.DESC:
            return desc()

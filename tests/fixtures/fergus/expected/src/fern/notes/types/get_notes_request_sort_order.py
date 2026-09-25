

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetNotesRequestSortOrder(enum.StrEnum):
    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetNotesRequestSortOrder.ASC:
            return asc()
        if self is GetNotesRequestSortOrder.DESC:
            return desc()

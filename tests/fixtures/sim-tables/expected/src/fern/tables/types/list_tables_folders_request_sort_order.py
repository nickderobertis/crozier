

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTablesFoldersRequestSortOrder(enum.StrEnum):
    """
    Sort direction.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListTablesFoldersRequestSortOrder.ASC:
            return asc()
        if self is ListTablesFoldersRequestSortOrder.DESC:
            return desc()

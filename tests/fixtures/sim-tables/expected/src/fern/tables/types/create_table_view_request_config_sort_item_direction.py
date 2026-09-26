

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTableViewRequestConfigSortItemDirection(enum.StrEnum):
    """
    Sort direction for this column.
    """

    ASC = "asc"
    DESC = "desc"

    def visit(self, asc: typing.Callable[[], T_Result], desc: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateTableViewRequestConfigSortItemDirection.ASC:
            return asc()
        if self is CreateTableViewRequestConfigSortItemDirection.DESC:
            return desc()

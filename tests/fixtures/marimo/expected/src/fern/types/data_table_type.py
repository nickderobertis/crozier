

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataTableType(enum.StrEnum):
    TABLE = "table"
    VIEW = "view"

    def visit(self, table: typing.Callable[[], T_Result], view: typing.Callable[[], T_Result]) -> T_Result:
        if self is DataTableType.TABLE:
            return table()
        if self is DataTableType.VIEW:
            return view()

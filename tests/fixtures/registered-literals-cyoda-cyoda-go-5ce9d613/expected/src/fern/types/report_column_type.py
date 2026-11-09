

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportColumnType(enum.StrEnum):
    SIMPLE_COLUMN = "SIMPLE_COLUMN"
    ALIAS = "ALIAS"

    def visit(self, simple_column: typing.Callable[[], T_Result], alias: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReportColumnType.SIMPLE_COLUMN:
            return simple_column()
        if self is ReportColumnType.ALIAS:
            return alias()

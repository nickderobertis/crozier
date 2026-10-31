

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TableCellRole(enum.StrEnum):
    BODY = "body"
    COLUMN_HEADER = "column_header"
    ROW_HEADER = "row_header"
    STUB = "stub"
    TITLE = "title"
    FOOTER = "footer"

    def visit(
        self,
        body: typing.Callable[[], T_Result],
        column_header: typing.Callable[[], T_Result],
        row_header: typing.Callable[[], T_Result],
        stub: typing.Callable[[], T_Result],
        title: typing.Callable[[], T_Result],
        footer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TableCellRole.BODY:
            return body()
        if self is TableCellRole.COLUMN_HEADER:
            return column_header()
        if self is TableCellRole.ROW_HEADER:
            return row_header()
        if self is TableCellRole.STUB:
            return stub()
        if self is TableCellRole.TITLE:
            return title()
        if self is TableCellRole.FOOTER:
            return footer()

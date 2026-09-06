

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class BookImportBatchDtoCopyMode(enum.StrEnum):
    MOVE = "MOVE"
    COPY = "COPY"
    HARDLINK = "HARDLINK"

    def visit(
        self,
        move: typing.Callable[[], T_Result],
        copy: typing.Callable[[], T_Result],
        hardlink: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BookImportBatchDtoCopyMode.MOVE:
            return move()
        if self is BookImportBatchDtoCopyMode.COPY:
            return copy()
        if self is BookImportBatchDtoCopyMode.HARDLINK:
            return hardlink()

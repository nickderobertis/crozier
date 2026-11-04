

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GoogleSheetsWriteBlockWriteMode(enum.StrEnum):
    APPEND = "append"
    UPDATE = "update"

    def visit(self, append: typing.Callable[[], T_Result], update: typing.Callable[[], T_Result]) -> T_Result:
        if self is GoogleSheetsWriteBlockWriteMode.APPEND:
            return append()
        if self is GoogleSheetsWriteBlockWriteMode.UPDATE:
            return update()

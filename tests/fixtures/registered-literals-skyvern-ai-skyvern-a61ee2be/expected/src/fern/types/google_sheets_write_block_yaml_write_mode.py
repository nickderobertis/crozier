

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GoogleSheetsWriteBlockYamlWriteMode(enum.StrEnum):
    APPEND = "append"
    UPDATE = "update"

    def visit(self, append: typing.Callable[[], T_Result], update: typing.Callable[[], T_Result]) -> T_Result:
        if self is GoogleSheetsWriteBlockYamlWriteMode.APPEND:
            return append()
        if self is GoogleSheetsWriteBlockYamlWriteMode.UPDATE:
            return update()

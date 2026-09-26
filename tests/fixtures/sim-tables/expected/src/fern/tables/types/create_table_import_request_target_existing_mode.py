

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTableImportRequestTargetExistingMode(enum.StrEnum):
    """
    Whether to append rows or replace existing rows.
    """

    APPEND = "append"
    REPLACE = "replace"

    def visit(self, append: typing.Callable[[], T_Result], replace: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateTableImportRequestTargetExistingMode.APPEND:
            return append()
        if self is CreateTableImportRequestTargetExistingMode.REPLACE:
            return replace()

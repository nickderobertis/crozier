

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableImportTargetExistingMode(enum.StrEnum):
    """
    Whether to append rows or replace existing rows.
    """

    APPEND = "append"
    REPLACE = "replace"

    def visit(self, append: typing.Callable[[], T_Result], replace: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2TableImportTargetExistingMode.APPEND:
            return append()
        if self is V2TableImportTargetExistingMode.REPLACE:
            return replace()

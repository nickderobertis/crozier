

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetFour(enum.StrEnum):
    OUTLINE = "outline"

    def visit(self, outline: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetFour.OUTLINE:
            return outline()

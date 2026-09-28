

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetFour(enum.StrEnum):
    OUTLINE = "outline"

    def visit(self, outline: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetFour.OUTLINE:
            return outline()

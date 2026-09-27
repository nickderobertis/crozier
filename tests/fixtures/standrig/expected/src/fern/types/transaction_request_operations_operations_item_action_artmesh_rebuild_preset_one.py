

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetOne(enum.StrEnum):
    MOUTH = "mouth"

    def visit(self, mouth: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionArtmeshRebuildPresetOne.MOUTH:
            return mouth()

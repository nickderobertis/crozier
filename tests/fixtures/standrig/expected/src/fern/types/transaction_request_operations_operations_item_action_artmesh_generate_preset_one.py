

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetOne(enum.StrEnum):
    MOUTH = "mouth"

    def visit(self, mouth: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransactionRequestOperationsOperationsItemActionArtmeshGeneratePresetOne.MOUTH:
            return mouth()
